def generate_string(string_list):
    s = string_list[0]
    for i in range(1, len(string_list)):                     #len(string_list)
        index = int(string_list[i]) + 1
        first_part_string = s[:index]
        second_part_string = s[index:]
        s = first_part_string + s + second_part_string
    return s


if __name__ == "__main__":
    file = open("input.txt", "r")
    lines = file.readlines()
    index_second_string = 0
    count = 0
    for line in lines:
        lines[count] = line.rstrip()
        if len(line) > 2:  # the number and newline char
            index_second_string = count
        count += 1

    first_string_list = lines[:index_second_string]
    second_string_list = lines[index_second_string:]

    generated_string1 = generate_string(first_string_list)
    generated_string2 = generate_string(second_string_list)
    print(generated_string1)
    print(generated_string2)
