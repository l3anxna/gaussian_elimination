import random

def matrix_generator(n):
    A = [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]
    x = [i + 1 for i in range(n)]
    B = [sum(A[i][j] * x[j] for j in range(n)) for i in range(n)]
    return A, B

def forward_elimination(A, B):
    n = len(A)
    for i in range(n):
        if A[i][i] == 0:
            for k in range(i + 1, n):
                if A[k][i] != 0:
                    A[i], A[k] = A[k], A[i]
                    B[i], B[k] = B[k], B[i]
                    break
            else:
                raise ValueError("Singular matrix")

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
    B_computed = [sum(A[i][j] * x[j] for j in range(len(x))) for i in range(len(A))]
    return all(abs(B_computed[i] - B[i]) < 1e-5 for i in range(len(B)))

n = int(input("Enter the size of the matrix: "))
A, B = matrix_generator(n)
print("Original Matrix A:")
for row in A:
    print([f'{val:.5f}' for val in row])
print("Original Vector B:", [f'{val:.5f}' for val in B])

A_eliminated, B_eliminated = forward_elimination(A, B)
x = backward_substitution(A_eliminated, B_eliminated)
result = test_solution(A, B, x)

print('Eliminated Matrix A:')
for row in A_eliminated:
    print([f'{val:.5f}' for val in row])
print('Eliminated Vector B:', [f'{val:.5f}' for val in B_eliminated])
print('Solution Vector x:', [f'{val:.5f}' for val in x])
print('Test Solution:', result)
