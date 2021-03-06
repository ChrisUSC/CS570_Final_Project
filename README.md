## CS570 - Algorithms

### Naming conventions

- All test cases are present in `tests` folder
- The input files have naming convention `*input*.txt`
- The expected results are named `*expected*.txt`
- The output files have naming convention `*output*.txt`, and are configured to be ignored by git.

### Final Project

`basic.py` and `efficient.py` are the main programs. They can either be run in debug mode which prints console outputs, or in normal mode where the `output.txt` file is generated.  

For their exact command line usage, you can run:
```
python <script.py> --help
```

The script always generates the output.txt file as required by the project instructions. Further, we can enable the debug prints or output comparison by the following flags:
```
python <script.py> <input_file> [--verbose] [--diff]

options:
  --verbose, -v  enable prints in console
  --diff, -d     compare output with expected result
```
