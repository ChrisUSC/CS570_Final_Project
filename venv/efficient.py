from alignment_params import calculate_alpha, GAP_PENALTY
from basic import basic_solution

'''
Pseudocode from text book
Alignment(X,Y):
    Array A[0...m, 0....n]
    Initialize A[i, 0] = i * gap_penalty for each i
    Initialize A[0, j] = j * gap_penalty for each j
    For j = 1, . . . , n
        For i = 1, . . . , m
            Use the recurrence (6.16) to compute A[i, j]
        EndFor
    EndFor
    Return A[m, n]

Python
def Alignment(x,y):
    cols, rows = (len(x), len(y))
    arr = [[0 for _ in range(cols)] for _ in range(rows)]  # first index moves left/right, second moves up/down
    for i in range(cols):
        arr[i][0] = i * gap_penalty
    for j in range(rows):
        arr[0][j] = j * gap_penalty
    for j in range(1, cols):
        for i in range(1, rows):
            arr[i][j] = min(
                arr[i - 1][j - 1] + calculate_alpha(string1[i], string2[j]),
                arr[i - 1][j] + gap_penalty,
                arr[i][j - 1] + gap_penalty
            )
    return arr[cols, rows]


Space-Efficient-Alignment(x,y)
    Array B[0...m, 0....1]
    Initialize B[i,0] = i * gap_penalty for each i (just as in column 0 of A):
    For j = 1, ... , n:
        B[0,1] = j * gap_penalty
        For i = 1, ..., m:
            B[i,1] = min(
                    B[i - 1][0] + calculate_alpha(x[i], y[j]),
                    B[i - 1][1] + gap_penalty,
                    arr[i][0] + gap_penalty
                )
        EndFor
        move column 1 of B to column 0 to make room for next iteration:
            Update B[i,0] = B[i,1] for each i
    EndFor

def Space_Efficient_Alignment(x,y):
    gap_penalty = GAP_PENALTY
    cols = 2
    rows = len(x)
    arr = [[0 for _ in range(cols)] for _ in range(rows)]  # two columns of size m
    for i in range(0, rows):
        arr[i][0] = i * gap_penalty
    for j in range(1,cols):
        arr[0][1] = j * gap_penalty
        for i in range (1,rows):
            arr[i][1] =  min(
                    arr[i - 1][0] + calculate_alpha(x[i], y[j]),
                    arr[i - 1][1] + gap_penalty,
                    arr[i][0] + gap_penalty
                )
        for i in range (0, rows):
            arr[i][0] = arr[i][1]

    
Divide-and-conquer-alignment(X,Y):
    Let m be the number of symbols in X
    Let n be the number of symbols in Y
    If m <= 2 or n <= 2:
        compute optimal alignment using Alignment(X,Y)
    Call Space-Efficient-Alignment(X, Y[1:n/2])
    Call Backward-Space-Efficient-Alignment(X, Y[n/2 + 1: n]            # This is not given in the textbook
    let q be the index minimizing f(q, n/2) + g(q, n/2)
    Add (q, n/2) to global list p
    Divide-and-conquer-alignment(X[1:q],Y[1:n/2])
    Divide-and-conquer-alignment(X[q+1:n],Y[n/2 + 1: n])
    Return P
'''


def find_alignment_scores(string1, string2):
    # Return the last column with scores
    # That is nothing but the scores for all of string1, against each substring of string2
    # The returned array should have size len(string2) x 1
    gap_penalty = GAP_PENALTY
    pass


def efficient_solution(string1, string2):
    m = len(string1)
    n = len(string2)

    # Base case
    if m <= 2 or n <= 2:
        # TODO: Is it possible that either m or n become 0?
        return basic_solution(string1, string2)

    # Find the scores for left half and right half
    mid = m // 2
    scores_left = find_alignment_scores(string1[:mid], string2)
    scores_right = find_alignment_scores(string1[-1:mid-1:-1], string2[-1::-1])

    # Find the divide point in string2
    split = 0
    min_score = scores_left[0] + scores_right[0]
    for i in range(1, len(string2)):
        score = scores_left[i] + scores_right[i]
        if score < min_score:
            min_score = score
            split = i

    # Solve sub-problems and combine the solution
    align1_left, align2_left = efficient_solution(string1[:mid], string2[:split])
    align1_right, align2_right = efficient_solution(string1[mid:], string2[split:])
    return align1_left + align1_right, align2_left + align2_right


if __name__ == "__main__":
    import generate_result as gr
    gr.parse_cli_and_run(efficient_solution)
