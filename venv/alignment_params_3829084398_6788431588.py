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


def is_valid_alignment(string1, string2, alignment1, alignment2):
    return (
            string1 == alignment1.replace("_", "") and
            string2 == alignment2.replace("_", "")
    )


def matching_underscores(alignment1, alignment2):
    for i in range(len(max(alignment1, alignment2))):
        if alignment1[i] == '_' and alignment2[i] == '_':
            print("_ aligned with _")
            return True
    print("good alignment")
    return False


def compute_score(alignment1, alignment2):
    if len(alignment1) != len(alignment2):
        raise ValueError('Alignment lengths do not match!')

    score = 0
    for i in range(len(alignment1)):
        if (alignment1[i] == '_') ^ (alignment2[i] == '_'):
            score += GAP_PENALTY
        else:
            score += calculate_alpha(alignment1[i], alignment2[i])

    return score
