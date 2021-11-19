import os
import argparse
import contextlib
import generate_string as gs
import profiler


def get_output_filename(input_filename):
    # Prepare the output file to be in same location as input
    # Replace the phrase "input" with "output" and retain the rest of the file name
    final_name = os.path.basename(input_filename)
    if "input" not in final_name:
        raise ValueError("Input file does not contain the phrase 'input' in it.")
    final_name = final_name.replace("input", "output")
    return os.path.join(os.path.dirname(input_filename), final_name)


def write_output(output_filename, response):
    with open(output_filename, "w") as file:
        alignment1, alignment2 = response["output"]
        file.writelines([
            f'{alignment1[:50]} {alignment2[:50]}\n',  # Prints the entire alignment if it is less than 50 characters
            f'{alignment1[-50:]} {alignment2[-50:]}\n',
            f'{round(response["time"] * 1000, 3)}ms\n',
            f'{response["memory"]}kB\n',
        ])


def parse_cli_and_run(algo_func):
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="file containing input strings")
    parser.add_argument("--debug", action="store_true", help="enable prints in console and disable profiling")
    args = parser.parse_args()

    string1, string2 = gs.read_input(args.input_file)
    if args.debug:
        alignment1, alignment2 = algo_func(string1, string2)
    else:
        # Disable any print statements as it will slow down execution
        with contextlib.redirect_stdout(None):
            response = profiler.run_with_profiler(algo_func, string1, string2)
            output_filename = get_output_filename(args.input_file)
            write_output(output_filename, response)
