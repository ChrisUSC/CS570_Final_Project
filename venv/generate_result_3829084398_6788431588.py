import os
import argparse
import contextlib
import generate_string_3829084398_6788431588 as gs
import profiler_3829084398_6788431588 as profiler
from alignment_params_3829084398_6788431588 import compute_score


def get_output_filename(input_filename, replace_with="output"):
    # Prepare the output file to be in same location as input
    # Replace the phrase "input" with "output" and retain the rest of the file name
    final_name = os.path.basename(input_filename)
    if "input" not in final_name:
        raise ValueError("Input file does not contain the phrase 'input' in it.")
    final_name = final_name.replace("input", replace_with)
    return os.path.join(os.path.dirname(input_filename), final_name)


def write_output(output_filename, response):
    with open(output_filename, "w") as file:
        alignment1, alignment2 = response["output"]
        file.writelines([
            f'{alignment1[:50]} {alignment2[:50]}\n',  # Prints the entire alignment if it is less than 50 characters
            f'{alignment1[-50:]} {alignment2[-50:]}\n',
            f'{compute_score(alignment1, alignment2)}\n',
            f'{round(response["time"], 3)}\n',  # In seconds
            f'{response["memory"]}',  # In kB
        ])


def read_output(output_filename):
    with open(output_filename, "r") as file:
        lines = file.readlines()
        al1_part1, al2_part1 = lines[0].rstrip().split(" ")
        al1_part2, al2_part2 = lines[1].rstrip().split(" ")
        return al1_part1, al2_part1, al1_part2, al2_part2


def compare_expected(output_filename, expected_filename):
    with open(output_filename, "r") as file:
        op_score = float(file.readlines()[2].strip())

    with open(expected_filename, "r") as file:
        exp_score = float(file.readlines()[2].strip())

    print(f'Our score: {op_score}\nExpected score: {exp_score}')
    return op_score == exp_score


def parse_cli_and_run(algo_func):
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="file containing input strings")
    parser.add_argument("--verbose", "-v", action="store_true", help="enable prints in console")
    parser.add_argument("--diff", "-d", action="store_true", help="compare output with expected result")
    args = parser.parse_args()

    string1, string2 = gs.read_input(args.input_file)
    output_filename = get_output_filename(args.input_file)
    if args.verbose:
        response = {
            "output": algo_func(string1, string2),
            "time": 0,
            "memory": 0
        }
    else:
        # Disable any print statements as it will slow down execution
        with contextlib.redirect_stdout(None):
            response = profiler.run_with_profiler(algo_func, string1, string2)
    write_output(output_filename, response)
    if args.diff:
        expected_filename = get_output_filename(args.input_file, replace_with="expected")
        is_match = compare_expected(output_filename, expected_filename)
        print(f'Our output and expected output have {"same" if is_match else "different"} score!')
