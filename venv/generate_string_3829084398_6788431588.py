import sys


def generate_string(string_list):
    s = string_list[0]
    for i in range(1, len(string_list)):  # len(string_list)
        index = int(string_list[i]) + 1
        first_part_string = s[:index]
        second_part_string = s[index:]
        s = first_part_string + s + second_part_string
    return s


def validate(list_1, list_2, string_1, string_2):
    j = len(list_1) - 1
    k = len(list_2) - 1
    if (2 ** j * len(list_1[0])) == len(string_1) and (2 ** k * len(list_2[0])) == len(string_2):
        return True
    return False


def read_input(filename):
    file = open(filename, "r")
    lines = file.readlines()
    index_second_string = 0
    for idx, line in enumerate(lines):
        lines[idx] = line.rstrip()
        try:
            int(lines[idx])  # If line is not a number, raise an exception
        except ValueError:
            # Exception caught, so this line is the next string
            index_second_string = idx

    first_string_list = lines[:index_second_string]
    second_string_list = lines[index_second_string:]

    generated_string1 = generate_string(first_string_list)
    generated_string2 = generate_string(second_string_list)
    if validate(first_string_list, second_string_list, generated_string1, generated_string2):
        return generated_string1, generated_string2
    else:
        # Prevent the program from running further
        raise RuntimeError('Failed to parse the inputs correctly.')


if __name__ == "__main__":
    f_name = sys.argv[1]
    string1, string2 = read_input(f_name)
    print(string1)
    print(string2)
