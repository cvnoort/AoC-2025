#!/usr/bin/python3
import sys
import numpy as np
import numpy.typing as npt


def get_math_problems(file) -> npt.NDArray:
    with open(file) as file: 
        problems_vertical = np.array( [line.split() for line in file] )
        problems = np.rot90(problems_vertical)
    return problems

def evaluate_problem(problem: list) -> int:
    operator = problem[len(problem) - 1]
    problem_string = operator.join(problem[0:len(problem) - 1])
    answer = eval(problem_string)
    return answer


if __name__ == "__main__":
    all_problems = get_math_problems(sys.argv[1])
    answers = [evaluate_problem(problem) for problem in all_problems]
    print("The grand total of all the answers to the math problems is", 
          sum(answers))
