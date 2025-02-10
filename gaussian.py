import random

def matrix_generator(n):
    A = [[random.randint (1, 10) for _ in range(n)] for _ in range(n)]
    x = [i + 1 for i in range(n)]
    B = [sum(A[i][j] * x[j] for j in range(n)) for i in range(n)]

    return A, B

if __name__ == '__main__':
    n = int(input("Enter the size of the matrix: "))
    A, B = matrix_generator(n)
    print(A)
    print(B)
            
