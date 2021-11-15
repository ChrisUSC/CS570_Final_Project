from alignment_params import calculate_delta, GAP_PENALTY


def basic_solution(string1, string2):
    gap_penalty = GAP_PENALTY
    cols, rows = (len(string1), len(string2))
    arr = [[0 for i in range(cols)] for j in range(rows)]  # first index moves left/right, second moves up/down
    for i in range(cols):
        arr[i][0] = i * gap_penalty
    for j in range(rows):
        arr[0][j] = j * gap_penalty
    for j in range(1, cols):
        for i in range(1, rows):
            arr[i][j] = min(
                arr[i - 1][j - 1] + calculate_delta(string1[i], string2[j]),
                arr[i - 1][j] + gap_penalty,
                arr[i][j - 1] + gap_penalty
            )
    i = cols-1
    j = rows-1

    for row in arr:
        print(row)

    alignment1 = ""
    alignment2 = ""
    while i > 0 and j > 0:
        val = arr[i][j]
        print(val)
        if val == arr[i - 1][j - 1] + calculate_delta(string1[i], string2[j]):
            i -= 1
            j -= 1
            alignment1 += string1[i]
            alignment2 += string2[j]
        if val == arr[i - 1][j] + gap_penalty:
            i -= 1
            alignment1 += string1[i]
            alignment2 += "_"
        if val == arr[i][j - 1] + gap_penalty:
            j -= 1
            alignment1 += "_"
            alignment2 += string1[i]
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
