from alignment_params import calculate_alpha, GAP_PENALTY


def basic_solution(string1, string2):
    """
    :param string1:
    :param string2:
    :return:
    """
    gap_penalty = GAP_PENALTY
    cols, rows = (len(string1) + 1, len(string2) + 1)
    arr = [[0 for _ in range(cols)] for _ in range(rows)]  # first index moves left/right, second moves up/down
    for i in range(rows):
        arr[i][0] = i * gap_penalty
    for i in range(cols):
        arr[0][i] = i * gap_penalty

    for i in range(1, len(string1) + 1):
        for j in range(1, len(string2) + 1):
            arr[i][j] = min(
                arr[i - 1][j - 1] + calculate_alpha(string1[i - 1], string2[j - 1]),
                arr[i - 1][j] + gap_penalty,
                arr[i][j - 1] + gap_penalty
            )
    i = rows - 1
    j = cols - 1
    '''
    for row in arr:
        print(row)
    '''
    alignment1 = ""
    alignment2 = ""
    while i > 0 or j > 0:
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

    alignment1 = alignment1[::-1]
    alignment2 = alignment2[::-1]
    print(string1)
    print(alignment1)
    print(string2)
    print(alignment2)

    return alignment1, alignment2


if __name__ == "__main__":
    import generate_result as gr
    gr.parse_cli_and_run(basic_solution)
