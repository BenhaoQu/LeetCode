import os
import sys
import traceback
import logging
from typing import Optional

from dotenv import load_dotenv

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from python.lc_libs import (get_daily_question, get_question_desc, get_question_testcases, Python3Writer,
                            extract_outputs_from_md, get_user_study_plans, get_user_study_plan_progress,
                            get_question_info, get_question_code, get_question_desc_cn)
import python.lc_libs as lc_libs
from python.constants import constant
from python.utils import get_default_folder, send_text_message


def check_remain_languages(dir_path, languages: list[str]) -> list[str]:
    remain_languages = list(languages)
    for _, _, files in os.walk(dir_path):
        for f in files:
            try:
                match f:
                    case "Solution.cpp":
                        remain_languages.remove("cpp")
                    case "solution.go":
                        remain_languages.remove("golang")
                    case "Solution.java":
                        remain_languages.remove("java")
                    case "solution.py":
                        remain_languages.remove("python3")
                    case "solution.ts":
                        remain_languages.remove("typescript")
                    case "solution.rs":
                        remain_languages.remove("rust")
                    case _:
                        continue
            except ValueError as _:
                continue
        break
    return remain_languages


def write_question(dir_path, problem_folder: str, question_id: str, question_name: str,
                   slug: str, languages: list[str] = None, cookie: str = None):
    desc = get_question_desc(slug, cookie)
    cn_result = get_question_desc_cn(slug, cookie)
    cn_desc = None
    question_rating = lc_libs.get_rating(question_id)
    if cn_result is not None and cn_result[0] is not None:
        cn_desc, cn_title = cn_result
        with open(f"{dir_path}/problem_zh.md", "w", encoding="utf-8") as f:
            f.write(Python3Writer.write_problem_md(question_id, cn_title, cn_desc, True, rating=question_rating))
    if desc is not None:
        is_chinese = False
        if "English description is not available for the problem. Please switch to Chinese." in desc:
            desc = cn_desc if cn_desc else ""
            is_chinese = True
        else:
            with open(f"{dir_path}/problem.md", "w", encoding="utf-8") as f:
                f.write(Python3Writer.write_problem_md(question_id, question_name, desc, rating=question_rating))
        testcases, testcase_str = get_question_testcases(slug)
        if testcases is not None:
            outputs = extract_outputs_from_md(desc, is_chinese)
            logging.debug(f"Parse question_id: {question_id}, teat cases outputs: {outputs}")
            if (not languages or "python3" in languages) and not os.path.exists(f"{dir_path}/testcase.py"):
                with open(f"{dir_path}/testcase.py", "w", encoding="utf-8") as f:
                    f.write(Python3Writer.write_testcase(testcases, outputs))
            if not os.path.exists(f"{dir_path}/testcase"):
                with open(f"{dir_path}/testcase", "w", encoding="utf-8") as f:
                    f.writelines([testcase_str, "\n",
                                  str(outputs).replace("None", "null")
                                 .replace("True", "true").replace("False", "false")
                                 .replace("'", "\"")])
    if not languages:
        return
    code_map = get_question_code(slug, lang_slugs=languages, cookie=cookie)
    if code_map is None:
        return
    for language in languages:
        try:
            code = code_map[language]
            cls = getattr(lc_libs, f"{language.capitalize()}Writer", None)
            if not cls:
                logging.warning(f"{language} Language Writer not supported yet")
                continue
            obj: lc_libs.LanguageWriter = cls()
            solution_file = obj.solution_file
            with open(os.path.join(dir_path, solution_file), "w", encoding="utf-8") as f:
                f.write(obj.write_solution(code, None, question_id, problem_folder))
            if isinstance(obj, lc_libs.RustWriter):
                obj.write_cargo_toml(dir_path, question_id)
        except Exception as _:
            logging.error(f"Failed to write [{question_id}] {language}solution", exc_info=True)
            continue
    logging.info(f"Add question: [{question_id}]{slug}")


def process_daily(languages: list[str], problem_folder: str = None):
    daily_info = get_daily_question()
    if not daily_info:
        return 1
    root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    question_id = daily_info['questionId']
    tmp = get_default_folder(paid_only=daily_info['paidOnly']) if not problem_folder else problem_folder
    dir_path = os.path.join(root_path, tmp, f"{tmp}_{question_id}")
    logging.info("Daily: {}, id: {}".format(daily_info['questionNameEn'], question_id))
    if not os.path.exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)
        write_question(dir_path, tmp, question_id, daily_info['questionNameEn'], daily_info['questionSlug'],
                       languages)
    else:
        logging.warning("Already solved {} before".format(daily_info['questionId']))
        remain_languages = check_remain_languages(dir_path, languages)
        write_question(dir_path, tmp, question_id, daily_info['questionNameEn'], daily_info['questionSlug'],
                       remain_languages)
    for lang in languages:
        try:
            cls = getattr(lc_libs, f"{lang.capitalize()}Writer", None)
            if not cls:
                logging.warning(f"{lang} Language Writer not supported yet")
                continue
            obj: lc_libs.LanguageWriter = cls()
            obj.change_test(root_path, tmp, question_id)
        except Exception as _:
            logging.error(f"Failed to change daily test for {lang}", exc_info=True)
            continue


def process_plans(cookie: str, languages: list[str] = None, problem_folder: str = None):
    plans = get_user_study_plans(cookie)
    if plans is None:
        if not send_text_message("The LeetCode in GitHub secrets might be expired, please check!",
                                 "Currently not be able to load user study plan, skip."):
            logging.error("Unable to send PushDeer notification!")
        logging.error("The LeetCode cookie might be expired, unable to check study plans!")
        return
    problem_ids = []
    root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    for slug in plans:
        plan_prog = get_user_study_plan_progress(slug, cookie)
        logging.info("Plan: {}, total: {}, cur: {}".format(slug, plan_prog["total"], plan_prog["finished"]))
        for question_slug in plan_prog["recommend"]:
            info = get_question_info(question_slug, cookie)
            if not info:
                logging.warning(f"Unable to find the recommended question [{question_slug}], skip!")
                continue
            question_id = info["questionFrontendId"]
            paid_only = info.get("isPaidOnly", False)
            tmp_folder = problem_folder if problem_folder else get_default_folder(paid_only=paid_only)
            dir_path = os.path.join(root_path, tmp_folder, f"{tmp_folder}_{question_id}")
            if not os.path.exists(dir_path):
                os.makedirs(dir_path, exist_ok=True)
                write_question(dir_path, tmp_folder, question_id, info["title"], question_slug, languages, cookie)
            else:
                remain_languages = check_remain_languages(dir_path, languages)
                write_question(dir_path, tmp_folder, question_id, info["title"], question_slug, remain_languages,
                               cookie)
            problem_ids.append([question_id, tmp_folder])
    if problem_ids:
        for lang in languages:
            try:
                cls = getattr(lc_libs, f"{lang.capitalize()}Writer", None)
                if not cls:
                    logging.warning(f"{lang} writer is not supported yet!")
                    continue
                obj: lc_libs.LanguageWriter = cls()
                obj.change_tests(root_path, problem_ids)
            except Exception as _:
                logging.error(f"Failed to change tests for {lang}", exc_info=True)
                continue
    else:
        logging.info("No recommended questions in the study plan today!")


def main(problem_folder: str = None, cookie: Optional[str] = None, languages: list[str] = None):
    try:
        process_daily(languages, problem_folder)
        if cookie is not None and len(cookie) > 0:
            process_plans(cookie, languages, problem_folder)
    except Exception as _:
        logging.error("Failed to process daily and plans", exc_info=True)
        return 1
    return 0


if __name__ == '__main__':
    rp = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    sys.path.insert(0, os.path.join(rp, "python"))
    try:
        load_dotenv()
    except Exception as e:
        print(f"Load Env exception, {e}")
        traceback.print_exc()
    cke = os.getenv(constant.COOKIE)
    pf = os.getenv(constant.PROBLEM_FOLDER, None)
    log_level = os.getenv(constant.LOG_LEVEL, "INFO")
    logging.basicConfig(level=log_level.upper(), format=constant.LOGGING_FORMAT, datefmt=constant.DATE_FORMAT)
    try:
        langs_str = os.getenv(constant.LANGUAGES, "python3")
        if not langs_str:
            langs_str = "python3"
        langs = langs_str.split(",")
    except Exception as ex:
        logging.debug("Failed to get languages from env, use default python3", exc_info=True)
        langs = ["python3"]
    exec_res = main(pf, cke, langs)
    sys.exit(exec_res)
