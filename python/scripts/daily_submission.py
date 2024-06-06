import argparse
import json
import os
import sys
import traceback
from typing import Optional

from dotenv import load_dotenv

from daily_auto import write_question

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import python.lc_libs as lc_libs
from python.constants import constant
from python.utils import get_default_folder, send_text_message, check_problem_solved_and_write


def main(problem_folder: str, user_slug: str, cookie: Optional[str], languages: list[str]):
    try:
        if not lc_libs.check_user_exist(user_slug):
            print(f"User not exist: {user_slug}")
            return 1
        daily_info = lc_libs.get_daily_question()
        if not daily_info:
            print(f"Unable to get daily question")
            return 1
        daily_question = daily_info['questionId']
        finish_daily = False
        plan_questions_slug = set()
        finished_plan_questions = []
        if cookie:
            plans = lc_libs.get_user_study_plans(cookie)
            if plans is None:
                if not send_text_message("The LeetCode in GitHub secrets might be expired, please check!",
                                         "Currently might not be able to fetch submission."):
                    print("Unable to send PushDeer notification!")
                print("The LeetCode cookie might be expired!")
            elif plans:
                for plan_slug in plans:
                    plan_prog = lc_libs.get_user_study_plan_progress(plan_slug, cookie, 0)
                    plan_questions_slug = plan_questions_slug.union(plan_prog["all_solved"])
        submit_dict = lc_libs.check_accepted_submission_all(cookie) if cookie \
            else lc_libs.check_accepted_submission(user_slug)
        root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        sys.path.insert(0, os.path.join(root_path, "python"))
        for question_id, submits in submit_dict.items():
            cache = set()
            dir_path = os.path.join(root_path, problem_folder, f"{problem_folder}_{question_id}")
            if question_id == daily_question and not os.path.exists(dir_path):
                os.mkdir(dir_path)
                write_question(dir_path, daily_question, daily_info['questionNameEn'],
                               daily_info['questionSlug'], list(languages))
            elif not os.path.exists(dir_path):
                info = lc_libs.get_question_info(submits[0][1])
                os.mkdir(dir_path)
                write_question(dir_path, question_id, info["title"], submits[0][1], list(languages))
            default_code = lc_libs.get_question_code(submits[0][1], lang_slugs=languages, cookie=cookie)
            for submit_id, question_slug, language in submits:
                if language in cache:
                    continue
                detail = lc_libs.get_submission_detail(submit_id, cookie)
                if not detail:
                    print(f"Unable to get submission detail for {submit_id}")
                    continue
                code = detail["code"]
                func = getattr(lc_libs, "write_solution_{}".format(language), None)
                test_func = getattr(lc_libs, "change_test_{}".format(language), None)
                if check_problem_solved_and_write(question_id,
                                                  detail["lang"],
                                                  root_path,
                                                  dir_path,
                                                  True,
                                                  func,
                                                  (default_code[detail["lang"]], code, question_id),
                                                  test_func):
                    print(f"Already solved problem: {question_id}, language: {language}")
                cache.add(language)
                if question_id == daily_question:
                    finish_daily = True
                elif question_slug in plan_questions_slug and question_slug not in finished_plan_questions:
                    finished_plan_questions.append(question_slug)
        print("Daily Question {}: {}, Study plan problem solved today: {}"
              .format(daily_question, "DONE" if finish_daily else "TODO", finished_plan_questions))
        if not finish_daily:
            return 1
    except Exception as e:
        print("Exception caught: ", str(e))
        traceback.print_exc()
        return 1
    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--user', required=True, type=str, help='The user slug in LeetCode.')
    args = parser.parse_args()
    try:
        load_dotenv()
    except Exception as e:
        print(f"Load Env exception, {e}")
        traceback.print_exc()
    cke = os.getenv(constant.COOKIE)
    pf = os.getenv(constant.PROBLEM_FOLDER, get_default_folder())
    try:
        langs = os.getenv(constant.LANGUAGES, "python3").split(",")
    except Exception as _:
        traceback.print_exc()
        langs = ["python3"]
    exec_res = main(pf, args.user, cke, langs)
    sys.exit(exec_res)
