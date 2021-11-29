import random


def generate_tests(num):
    choices = ['A', 'C', 'G', 'T']
    for i in range(num):
        s = ""
        f = open("tests/generated/input" + str(i) + ".txt", "w")
        for j in range(4):
            s += choices[random.randrange(4)]
        s += '\n'
        num_lines = random.randint(3, 9)
        for j in range(num_lines):
            max_num = 2**j
            s += str(random.randrange(max_num)) + '\n'
        for j in range(4):
            s += choices[random.randrange(4)]
        s += '\n'
        num_lines = random.randint(3, 9)
        for j in range(num_lines):
            max_num = 2**j
            s += str(random.randrange(max_num)) + '\n'
        f.write(s)


if __name__ == "__main__":
    num_tests = int(input("How many tests do you want to create? "))
    generate_tests(num_tests)