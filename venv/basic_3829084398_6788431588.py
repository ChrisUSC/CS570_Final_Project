from alignment_params_3829084398_6788431588 import *


def basic_solution(string1, string2):
    """
    :param string1:
    :param string2:
    :return:
    """
    gap_penalty = GAP_PENALTY
    rows, cols = (len(string1) + 1, len(string2) + 1)
    arr = [[0 for _ in range(cols)] for _ in range(rows)]  # first index moves left/right, second moves up/down
    for i in range(len(arr)):
        arr[i][0] = i * gap_penalty
    for i in range(len(arr[0])):
        arr[0][i] = i * gap_penalty

    for i in range(1, len(string1) + 1):
        for j in range(1, len(string2) + 1):
            arr[i][j] = min(
                arr[i - 1][j - 1] + calculate_alpha(string1[i - 1], string2[j - 1]),
                arr[i - 1][j] + gap_penalty,
                arr[i][j - 1] + gap_penalty
            )

    '''
    for row in arr:
        print(row)
    '''

    i = rows - 1
    j = cols - 1
    alignment1 = ""
    alignment2 = ""
    while i > 0 and j > 0:
        # Traceback until we reach a base case
        val = arr[i][j]
        if val == arr[i - 1][j - 1] + calculate_alpha(string1[i-1], string2[j-1]):
            alignment1 += string1[i - 1]
            alignment2 += string2[j - 1]
            i -= 1
            j -= 1
        elif val == arr[i - 1][j] + gap_penalty:
            alignment1 += string1[i - 1]
            alignment2 += "_"
            i -= 1
        elif val == arr[i][j - 1] + gap_penalty:
            alignment1 += "_"
            alignment2 += string2[j - 1]
            j -= 1

    if i == 0 and j != 0:
        # Rest of string2 is matched to gap
        alignment1 += '_' * j
        alignment2 += string2[j-1::-1]
    if i != 0 and j == 0:
        # Rest of string1 is matched to gap
        alignment1 += string1[i-1::-1]
        alignment2 += '_' * i

    alignment1 = alignment1[::-1]
    alignment2 = alignment2[::-1]

    if matching_underscores(alignment1, alignment2):
        raise RuntimeError('Alignment matches _ with another _')

    if not is_valid_alignment(string1, string2, alignment1, alignment2):
        raise RuntimeError('Alignment does not match with input letters!')
    return alignment1, alignment2


if __name__ == "__main__":
    import generate_result_3829084398_6788431588 as gr
    gr.parse_cli_and_run(basic_solution)
