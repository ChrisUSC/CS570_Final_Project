import os
import glob
import subprocess

import pandas as pd
import matplotlib.pyplot as plt

import generate_string_3829084398_6788431588 as gs
import generate_result_3829084398_6788431588 as gr
from basic_3829084398_6788431588 import basic_solution
from efficient_3829084398_6788431588 import efficient_solution


def find_input_files(folder):
    return glob.glob(os.path.join(folder, "*input*.txt"))


def collect_stats(input_files, repeat=5):
    records = []

    for input_file in input_files:
        string1, string2 = gs.read_input(input_file)
        for algo_func in [basic_solution, efficient_solution]:
            print(f'File: {input_file}, Algorithm: {algo_func.__name__}')
            for iteration in range(repeat):
                resp = subprocess.run(f'python {algo_func.__module__}.py {input_file}')
                if resp.returncode != 0:
                    raise RuntimeError("Failed to execute algorithm!")
                op_file = gr.get_output_filename(input_file)
                with open(op_file, "r") as file:
                    lines = file.readlines()
                    records.append({
                        "inputFile": input_file,
                        "inputSize": len(string1) + len(string2),           # Piazza says size is m + n from TA
                        "iteration": iteration,
                        "algorithm": algo_func.__name__,
                        "score": float(lines[2].strip()),
                        "timeSec": float(lines[3].strip()),
                        "memoryKB": float(lines[4].strip())
                    })

    return pd.DataFrame(records)


def find_mismatch(records):
    records = records.groupby(["inputSize", "algorithm"], as_index=False).agg({"score": "min"})
    scores = records.pivot(index="inputSize", columns="algorithm", values="score")
    return scores[scores[basic_solution.__name__] != scores[efficient_solution.__name__]]


def plot_perf(records, output_dir):
    records = records.groupby(["inputSize", "algorithm"], as_index=False).agg({"timeSec": "mean", "memoryKB": "mean"})

    time = records.pivot(index="inputSize", columns="algorithm", values="timeSec")
    time.columns.name = None
    fig = time.plot()
    fig.set_ylabel("timeSec")
    plt.savefig(os.path.join(output_dir, "time_perf"))

    memory = records.pivot(index="inputSize", columns="algorithm", values="memoryKB")
    memory.columns.name = None
    fig = memory.plot()
    fig.set_ylabel("memoryKB")
    plt.savefig(os.path.join(output_dir, "memory_perf"))


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("input_dir", help="folder containing input files")
    parser.add_argument("--repeat", type=int, default=5, help="number of times to repeat each test")
    args = parser.parse_args()

    if not args.repeat >= 1:
        raise ValueError("Please enter a positive repeat count.")

    input_files = find_input_files(args.input_dir)

    records = collect_stats(input_files, args.repeat)
    score_diffs = find_mismatch(records)
    if not score_diffs.empty:
        print('Both solutions gave different scores!')
        print(score_diffs)
        exit(1)
    plot_perf(records, args.input_dir)
    records.to_csv("output.csv")
    print(f'Figures saved in: {args.input_dir}')
