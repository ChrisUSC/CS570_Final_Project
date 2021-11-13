def calculate_delta(first_letter, second_letter):
    first_letter = first_letter.lower()
    second_letter = second_letter.lower()
    if first_letter > second_letter:  # reduce number of combinations by 2
        temp = first_letter
        first_letter = second_letter
        second_letter = temp
    if first_letter == second_letter:
        return 0
    if first_letter == "a":
        if second_letter == "c":
            return 110
        if second_letter == "g":
            return 48
        if second_letter == "t":
            return 94
    if first_letter == "c":
        if second_letter == "g":
            return 118
        if second_letter == "t":
            return 48
    if first_letter == "g":
        if second_letter == "t":
            return 110


def efficient_solution():
    gap_penalty = 30
    # TODO
