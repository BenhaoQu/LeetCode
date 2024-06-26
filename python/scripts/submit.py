import asyncio
import os
import sys
import traceback
import argparse
from typing import Optional

from dotenv import load_dotenv

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import python.lc_libs as lc_libs
from python.constants import constant
from python.utils import get_default_folder


async def main(root_path, problem_id: str, lang: str, cookie: str, problem_folder: str = None):
    load_code = False
    code = ""
    code_func = getattr(lc_libs, "get_solution_code_{}".format(lang), None)
    if not code_func:
        print(f"{lang} is not supported yet!")
        return
    if not problem_id:
        if not problem_folder:
            problem_folder = get_default_folder()
        origin_problem_id, problem_id = problem_id, problem_id.replace(" ", "_")
        code, problem_id = code_func(root_path, problem_folder, problem_id)
        load_code = True
        if not code:
            print("No solution yet!")
            return
        if not problem_id:
            print("Unable to get problem_id")
            return
    else:
        origin_problem_id, problem_id = problem_id, problem_id.replace(" ", "_")
    questions = lc_libs.get_questions_by_key_word(origin_problem_id)
    if not questions:
        print(f"Unable to find any questions with problem_id {origin_problem_id}")
        return
    problem_slug = None
    for question in questions:
        if question["paidOnly"] and not cookie:
            continue
        if question["frontendQuestionId"] == origin_problem_id:
            problem_slug = question["titleSlug"]
            break
    if not problem_slug:
        print(f"Unable to find any questions with problem_id {problem_id}, possible questions: {questions}")
        return
    problem_info = lc_libs.get_question_info(problem_slug, cookie)
    if not problem_info:
        print(f"Unable to get problem info: {problem_id}")
        return
    is_paid_only = problem_info["isPaidOnly"]
    if not problem_folder:
        problem_folder = get_default_folder(paid_only=is_paid_only)
    if not load_code:
        code, _ = code_func(root_path, problem_folder, problem_id)
        if not code:
            print("No solution yet!")
            return
    lc_question_id = problem_info["questionId"]
    plans = lc_libs.get_user_study_plans(cookie)
    result = None
    exists = False
    for plan in plans:
        all_problems = lc_libs.get_user_study_plan_progress(plan, cookie, 0).get("all_problems", set())
        if problem_slug in all_problems:
            result = await lc_libs.submit_code(root_path, problem_folder, problem_id, problem_slug, cookie, lang, lc_question_id, code, plan)
            exists = True
    if not exists:
        result = await lc_libs.submit_code(root_path, problem_folder, problem_id, problem_slug, cookie, lang, lc_question_id, code)
    return result


if __name__ == '__main__':
    rp = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    sys.path.insert(0, os.path.join(rp, "python"))
    parser = argparse.ArgumentParser()
    parser.add_argument("-id", required=False, type=str, help="The id of question to submit.", default="")
    parser.add_argument("lang", type=str, help="The language to submit.")
    args = parser.parse_args()
    try:
        load_dotenv()
    except Exception as e:
        print(f"Load Env exception, {e}")
        traceback.print_exc()
    question_id = args.id
    cke = os.getenv(constant.COOKIE)
    try:
        langs = os.getenv(constant.LANGUAGES, "python3").split(",")
    except Exception as _:
        traceback.print_exc()
        langs = ["python3"]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(rp, question_id, args.lang, cke))
    sys.exit(0)
