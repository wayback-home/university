import argparse
import subprocess
import sys
from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_sample_data(problem_number):
    sample_data = []

    bs = BeautifulSoup(
        urlopen("https://www.acmicpc.net/problem/%s" % problem_number).read(),
        "html.parser",
    )
    bs_sample_data = bs.find_all("pre", "sampledata")

    for i in range(0, len(bs_sample_data), 2):
        sample_data.append([bs_sample_data[i].string, bs_sample_data[i + 1].string])

    return sample_data


def get_code_result(file_name, example_input):
    return subprocess.run(
        ["python", file_name], input=example_input.encode(), capture_output=True
    )


def get_test_result(sample_data, file_name):
    index = 1
    for example_input, example_output in sample_data:
        code_result = get_code_result(file_name, example_input)

        if code_result.returncode == 0:
            if code_result.stdout.decode().strip() == example_output.strip():
                print("예제 입력 ", index, " 테스트: 성공")
            else:
                print("예제 입력 ", index, " 테스트: 실패")
                print("예상: ", example_output)
                print("결과: ", code_result.stdout.decode().strip())
        else:
            print("예제 입력 ", index, " 테스트: 실패")
            # WINDOWS: 'euc-kr'
            # LINUX or MAC: 'utf-8'
            print("stderr: ", code_result.stderr.decode("euc-kr"))

        index += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", required=True)
    parser.add_argument("-n", "--number", required=True)
    args = parser.parse_args()

    file_name = args.filename
    problem_number = args.number

    get_test_result(get_sample_data(problem_number), file_name)
