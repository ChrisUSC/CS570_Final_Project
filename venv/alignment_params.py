GAP_PENALTY = 30


def calculate_alpha(first_letter, second_letter):
    if first_letter > second_letter:  # reduce number of combinations by 2
        temp = first_letter
        first_letter = second_letter
        second_letter = temp
    if first_letter == second_letter:
        return 0
    if first_letter == "A":
        if second_letter == "C":
            return 110
        if second_letter == "G":
            return 48
        if second_letter == "T":
            return 94
    if first_letter == "C":
        if second_letter == "G":
            return 118
        if second_letter == "T":
            return 48
    if first_letter == "G":
        if second_letter == "T":
            return 110
