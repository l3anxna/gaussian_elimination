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

if __name__ == "__main__":
    n = int(input("Enter the size of the matrix: "))
    A, B = matrix_generator(n)
    print("Original Matrix A:")
    for row in A:
        print(row)
    print("Original Vector B:", B)

    A_eliminated, B_eliminated = forward_elimination(A, B)

    print("\nEliminated Matrix A:")
    for row in A_eliminated:
        print(row)
    print("Eliminated Vector B:", B_eliminated)
