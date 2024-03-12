from termcolor import colored
import sys
import os

file_name = ""
problem_name = ""
testsets = []


def test_cpp():
    # compile cpp file
    os.system(f"g++ {file_name} -o {problem_name}")

    # test the code on each testset
    test = 1
    for testset in testsets:
        os.system(
            f"{problem_name} < {problem_name}_folder/{testset} > {problem_name}_folder/{testset[:len(testset)-4]}.out"
        )

        output = ""
        expected_output = ""

        with open(f"{problem_name}_folder/{testset[:len(testset)-4]}.out", "r") as f:
            output = f.read()

        with open(f"{problem_name}_folder/out{str(test)}.txt", "r") as f:
            expected_output = f.read()

        if output == expected_output:
            print(f"Test {str(test)}: {colored('OK', 'green')}")
        else:
            print(f"Test {str(test)}: {colored('Failed', 'red')}")
            print()

            print("Expected Output:")
            print(expected_output)
            print()

            print("Your Output:")
            print(output)
            print()

        os.chdir(f"{problem_name}_folder")
        os.system(f"rm {testset[:len(testset)-4]}.out")
        os.chdir("..")

        test += 1

    os.system(f"rm {problem_name}")


def test_py():
    # test the code on each testset
    test = 1
    for testset in testsets:
        os.system(
            f"python3 {problem_name}.py < {problem_name}_folder/{testset} > {problem_name}_folder/{testset[:len(testset)-4]}.out"
        )

        output = ""
        expected_output = ""

        with open(f"{problem_name}_folder/{testset[:len(testset)-4]}.out", "r") as f:
            output = f.read()

        with open(f"{problem_name}_folder/out{str(test)}.txt", "r") as f:
            expected_output = f.read()

        if output == expected_output:
            print(f"Test {str(test)}: {colored('OK', 'green')}")
        else:
            print(f"Test {str(test)}: {colored('Failed', 'red')}")
            print()

            print("Expected Output:")
            print(expected_output)
            print()

            print("Your Output:")
            print(output)
            print()

        os.chdir(f"{problem_name}_folder")
        os.system(f"rm {testset[:len(testset)-4]}.out")
        os.chdir("..")

        test += 1


if __name__ == "__main__":
    file_name = sys.argv[1]
    extension = file_name.split(".")[-1]
    problem_name = file_name.split(".")[0]

    testsets = os.listdir(f"{problem_name}_folder")
    testsets = [testset for testset in testsets if testset[:2] == "in"]

    if extension == "cpp":
        test_cpp()

    elif extension == "py":
        test_py()
