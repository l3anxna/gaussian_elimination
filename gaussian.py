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

        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            B[j] -= factor * B[i]
        print(f"\nMatrix after eliminating {i + 1}:")
        for row in A:
            print([f'{val:.5f}' for val in row])
        print(f"Vector after eliminating {i + 1}: {[f'{val:.5f}' for val in B]}")
    return A, B

n = 3
A, B = matrix_generator(n)
print("Original Matrix:")
for row in A:
    print([f'{val:.5f}' for val in row])
print("Original Vector:", [f'{val:.5f}' for val in B])

A_eliminated, B_eliminated = forward_elimination(A, B)

print("\nFinal Matrix:")
for row in A_eliminated:
    print([f'{val:.5f}' for val in row])
print("Final Vector:", [f'{val:.5f}' for val in B_eliminated])
