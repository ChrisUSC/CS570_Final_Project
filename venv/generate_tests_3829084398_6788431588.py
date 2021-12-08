import random


def generate_tests(num=20):
    choices = ['A', 'C', 'G', 'T']
    num_tests = int(num/2)
    for i in range(0, num_tests):
        s = ""
        f = open("tests/generated/input" + str(i * 2) + ".txt", "w")
        for j in range(4):
            s += choices[random.randrange(4)]
        s += '\n'
        num_lines = i % 9           # max lines is 8, first line is 4 chars, 4 * 2^8 = 2^10 which is max input
        print("1 " + str(num_lines))
        for j in range(num_lines):
            max_num = 2 ** j
            s += str(random.randrange(max_num)) + '\n'

        for j in range(4):
            s += choices[random.randrange(4)]
        s += '\n'
        for j in range(num_lines):
            max_num = 2 ** j
            s += str(random.randrange(max_num)) + '\n'
        f.write(s)


        s = ""
        f = open("tests/generated/input" + str(i*2 + 1) + ".txt", "w")
        for j in range(4):
            s += choices[random.randrange(4)]
        s += '\n'
        for j in range(num_lines):
            max_num = 2 ** j
            s += str(random.randrange(max_num)) + '\n'
        num_lines = (i + 1) % 9           # max lines is 8, first line is 4 chars, 4 * 2^8 = 2^10 which is max input

        for j in range(4):
            s += choices[random.randrange(4)]
        s += '\n'
        for j in range(num_lines):
            max_num = 2 ** j
            s += str(random.randrange(max_num)) + '\n'
        f.write(s)



if __name__ == "__main__":
    # num_tests = int(input("How many tests do you want to create? "))
    generate_tests()
