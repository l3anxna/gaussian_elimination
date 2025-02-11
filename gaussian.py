import random
import numpy as np

def matrix_generator(n):
    A = [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]
    x = [i + 1 for i in range(n)]
    B = [sum(A[i][j] * x[j] for j in range(n)) for i in range(n)]
    return A, B

def hilbert_matrix(n):
    return np.array([[1 / (i + j + 1) for j in range(n)] for i in range(n)])

def forward_elimination(A, B):
    n = len(A)
    A = [row[:] for row in A]
    B = B[:]
    for i in range(n):
        if A[i][i] == 0:
            for k in range(i + 1, n):
                if A[k][i] != 0:
                    A[i], A[k] = A[k][:], A[i][:]
                    B[i], B[k] = B[k], B[i]
                    break

        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            B[j] -= factor * B[i]
    return A, B

def backward_substitution(A, B):
    n = len(A)
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = B[i]
        for j in range(i + 1, n):
            x[i] -= A[i][j] * x[j]
        x[i] /= A[i][i]
    return x

def test_solution(A, B, x):
    A = np.array(A)
    x = np.array(x)
    B = np.array(B)
    B_computed = A @ x
    residue = B_computed - B
    return np.linalg.norm(residue)

sizes = [5, 10, 20]
results_normal = {}
results_hilbert = {}

for n in sizes:
    A_normal, B_normal = matrix_generator(n)
    A_normal_eliminated, B_normal_eliminated = forward_elimination(A_normal, B_normal)
    x_normal = backward_substitution(A_normal_eliminated, B_normal_eliminated)
    residue_normal = test_solution(A_normal, B_normal, x_normal)
    results_normal[n] = residue_normal

    A_hilbert = hilbert_matrix(n)
    x_true = np.array([i + 1 for i in range(n)])
    B_hilbert = A_hilbert @ x_true
    A_hilbert_list = A_hilbert.tolist()
    B_hilbert_list = B_hilbert.tolist()
    try:
        A_hilbert_eliminated, B_hilbert_eliminated = forward_elimination(A_hilbert_list, B_hilbert_list)
        x_hilbert = backward_substitution(A_hilbert_eliminated, B_hilbert_eliminated)
        residue_hilbert = test_solution(A_hilbert_list, B_hilbert_list, x_hilbert)
        results_hilbert[n] = residue_hilbert
    except ValueError as e:
        results_hilbert[n] = str(e)

print("Normal Matrix:", results_normal)
print("Hilbert Matrix:", results_hilbert)
