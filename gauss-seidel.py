import random

def generate_matrix(n):
    A = [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        A[i][i] = sum(A[i][j] for j in range(n)) + random.randint(1, 10)
    x = [random.randint(1, 10) for _ in range(n)]
    B = [sum(A[i][j] * x[j] for j in range(n)) for i in range(n)]
    return A, B, x

def gauss_seidel(A, b, x0=None, tol=1e-6, max_iterations=100):
    n = len(b)
    x = [0.0] * n if x0 is None else x0
    approximations = []

    for iteration in range(max_iterations):
        x_new = x[:]
        for i in range(n):
            s = sum(A[i][j] * x_new[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]

        approximations.append(x_new[:])

        distance = sum((x_new[i] - x[i]) ** 2 for i in range(n)) ** 0.5
        print(f"Iteration {iteration + 1}: {x_new}, Distance: {distance}")

        if distance < tol:
            print("Convergence achieved.")
            break

        x = x_new[:]

    return x_new, approximations

def hilbert_matrix(n):
    return [[1 / (i + j + 1) for j in range(n)] for i in range(n)]

n = int(input("Enter the size of the matrix: "))
A, B, x_true = generate_matrix(n)
print("Coefficient matrix (A):")
for row in A:
    print(row)
print("Right-hand side vector (b):")
print(B)
print("Known solution (x_true):")
print(x_true)

x0 = [x_true[i] + random.uniform(-0.5, 0.5) for i in range(n)]
print("Initial approximation (x0):")
print(x0)

x_approx, approximations = gauss_seidel(
    A, B, x0, tol=1e-6, max_iterations=10
)

print("Final approximation (x_approx):")
print(x_approx)
print("Exact solution (x_true):")
print(x_true)

n = int(input("Enter the size of the hilbert matrix: "))
A = hilbert_matrix(n)

x_true = [1 for _ in range(n)]
B = [sum(A[i][j] * x_true[j] for j in range(n)) for i in range(n)]

print("Hilbert matrix (A):")
for row in A:
    print(row)
print("Right-hand side vector (b):")
print(B)
print("Known solution (x_true):")
print(x_true)

x0 = [0.0] * n
x_approx, approximations = gauss_seidel(
    A, B, x0, tol=1e-6, max_iterations=100
)

print("Final approximation (x_approx):")
print(x_approx)
print("Exact solution (x_true):")
print(x_true)
