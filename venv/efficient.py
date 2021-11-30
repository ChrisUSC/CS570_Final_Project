from alignment_params import *
from basic import basic_solution

def find_alignment_scores(string1, string2):
    '''
    :param string1:
    :param string2:
    :return:
    '''
    # Return the last column with scores
    # That is nothing but the scores for all of string1, against each substring of string2
    # The returned array should have size (len(string2) + 1)
    gap_penalty = GAP_PENALTY
    rows, cols = (len(string1) + 1, len(string2) + 1)
    prev_col = [0 for _ in range(cols)]
    cur_col = [0 for _ in range(cols)]

    for j in range(cols):
        prev_col[j] = j * gap_penalty

    for i in range(1, len(string1) + 1):
        cur_col[0] = i * gap_penalty
        for j in range(1, len(string2) + 1):
            cur_col[j] = min(
                prev_col[j - 1] + calculate_alpha(string1[i - 1], string2[j - 1]),
                prev_col[j] + gap_penalty,
                cur_col[j - 1] + gap_penalty
            )
        prev_col, cur_col = cur_col, prev_col

    return prev_col


def _align_recurse(string1, string2):
    m = len(string1)
    n = len(string2)
    print(f'Recursing with: "{string1}", "{string2}"')

    # Base case
    if n == 0:
        # NOTE: m cannot never be 0, since we always split by 2 and stop splitting m <= 2
        return string1, "_" * m
    if m <= 2 or n <= 2:
        return basic_solution(string1, string2)

    # Find the scores for left half and right half
    mid = m // 2
    scores_left = find_alignment_scores(string1[:mid], string2)
    scores_right = find_alignment_scores(string1[-1:mid-1:-1], string2[-1::-1])
    scores_right = scores_right[::-1]

    # Find the divide point in string2
    split = 0
    min_score = scores_left[0] + scores_right[0]
    for i in range(1, len(string2) + 1):
        score = scores_left[i] + scores_right[i]
        if score < min_score:
            min_score = score
            split = i

    # Solve sub-problems and combine the solution
    align1_left, align2_left = _align_recurse(string1[:mid], string2[:split])
    align1_right, align2_right = _align_recurse(string1[mid:], string2[split:])
    return align1_left + align1_right, align2_left + align2_right


def efficient_solution(string1, string2):
    alignment1, alignment2 = _align_recurse(string1, string2)
    if not is_valid_alignment(string1, string2, alignment1, alignment2):
        raise RuntimeError('Alignment does not match with input letters!')
    return alignment1, alignment2


if __name__ == "__main__":
    import generate_result as gr
    gr.parse_cli_and_run(efficient_solution)
