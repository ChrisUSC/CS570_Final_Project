from alignment_params import calculate_alpha, GAP_PENALTY

'''
Pseudocode from text book
Alignment(X,Y):
    Array B[0...m, 0....n]
    Initialize A[i, 0]= i * gap_penalty for each i
    Initialize A[0, j]= j * gap_penalty for each j
    For j = 1, . . . , n
        For i = 1, . . . , m
            Use the recurrence (6.16) to compute A[i, j]
        Endfor
    Endfor
    Return A[m, n]

Space-Efficient-Alignment(X,Y)
    Array B[0...m, 0....1]
    Initialize B[i,0] = i * gap_penalty for each i (just as in column 0 of A)
    For j = 1, ... , n:
        B[0,1] = j * gap_penalty
        For i = 1, ..., m:
            B[i,1] = min(
                    B[i - 1][0] + calculate_alpha(string1[i], string2[j]),
                    B[i - 1][1] + gap_penalty,
                    arr[i][0] + gap_penalty
                )
        endfor
        move column 1 of B to column 0 to make room for next iteration:
            Update B[i,0] = B[i,1] for each i
    endfor
    
    
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


def efficient_solution(string1, string2):
    gap_penalty = GAP_PENALTY
    # TODO


if __name__ == "__main__":
    import generate_result as gr

    gr.parse_cli_and_run(efficient_solution)
