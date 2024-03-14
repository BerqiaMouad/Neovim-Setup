from robobrowser import RoboBrowser
from termcolor import colored
import os
import sys
import werkzeug
import time
import pickle
import requests


if __name__ == "__main__":
    contestNumber = os.getcwd().split("/")[-1]
    problemName = sys.argv[1]
    lang = sys.argv[2]
    contestUrl = (
        "https://codeforces.com/contest/" + contestNumber + "/submit/" + problemName
    )

    session = None
    browser = None
    HOME = os.getenv("HOME")
    infos_user = open(
        f"{HOME}/.config/nvim/mouad_codeforces_tool/auth_codeforces.txt", "r"
    )
    user_name = infos_user.readline().strip()
    password = infos_user.readline().strip()
    infos_user.close()

    try:
        with open("session.pickle", "rb") as f:
            session = pickle.load(f)

        browser = RoboBrowser(parser="html.parser", session=session)

    except:
        browser = RoboBrowser(parser="html.parser")

        browser = RoboBrowser(parser="html.parser")

        browser.open("https://codeforces.com/enter?back=%2F")

        loginForm = browser.get_form(id="enterForm")

        loginForm["handleOrEmail"].value = user_name
        loginForm["password"].value = password

        browser.submit_form(loginForm)

        if browser.url != "https://codeforces.com/":
            print("Login failed")
            exit(0)

    browser.open(contestUrl)

    if browser.url != contestUrl:
        print(colored("Problem Does not exist", "red"))
        exit(0)

    submitForm = browser.get_form(class_="submit-form")

    if lang == "cpp":
        submitForm["sourceFile"].value = open(problemName + ".cpp", "rb")
        submitForm["programTypeId"].value = "GNU G++17 7.3.0"
    elif lang == "python":
        submitForm["sourceFile"].value = open(problemName + ".py", "rb")
        submitForm["programTypeId"].value = "PyPy 3.9.10 (7.3.9, 64bit)"

    browser.submit_form(submitForm)

    statusUrl = (
        f"https://codeforces.com/api/user.status?handle={user_name}&from=1&count=1"
    )

    time.sleep(2)

    response = requests.get(statusUrl).json()

    verdict = response["result"][0]["verdict"]
    tests_passed = response["result"][0]["passedTestCount"]

    while (
        response["result"][0]["contestId"] != int(contestNumber) or verdict == "TESTING"
    ):
        time.sleep(0.2)

        response = requests.get(statusUrl).json()

        verdict = response["result"][0]["verdict"]

        tests_passed = response["result"][0]["passedTestCount"]

    if verdict == "OK":
        print(f"Accepted, {tests_passed} tests passed")
    elif verdict == "WRONG_ANSWER":
        print(f"Wrong Answer on test {tests_passed + 1}")
    elif verdict == "TIME_LIMIT_EXCEEDED":
        print(f"Time Limit Exceeded on test {tests_passed + 1}")
    elif verdict == "MEMORY_LIMIT_EXCEEDED":
        print(f"Memory Limit Exceeded on test {tests_passed + 1}")
    else:
        print(f"{' '.join(verdict.split('_'))}")
