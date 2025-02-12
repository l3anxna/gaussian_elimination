import random
import matplotlib.pyplot as plt

def generate_diagonally_dominant_matrix(n):
    A = [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        A[i][i] = sum(abs(A[i][j]) for j in range(n)) + random.randint(1, 10)
    x = [random.randint(1, 10) for _ in range(n)]
    B = [sum(A[i][j] * x[j] for j in range(n)) for i in range(n)]
    return A, B, x

def jacobi(A, b, x0=None, tol=1e-6, max_iterations=100):
    n = len(b)
    x = [0.0] * n if x0 is None else x0
    x_new = [0.0] * n
    errors = []

    for _ in range(max_iterations):
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]

        error = sum((x_new[i] - x[i]) ** 2 for i in range(n)) ** 0.5
        errors.append(error)

        if error < tol:
            break

        x = x_new[:]

    return x_new, errors

def gauss_seidel(A, b, x0=None, tol=1e-6, max_iterations=100):
    n = len(b)
    x = [0.0] * n if x0 is None else x0
    errors = []

    for _ in range(max_iterations):
        x_new = x[:]
        for i in range(n):
            s = sum(A[i][j] * x_new[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]

        error = sum((x_new[i] - x[i]) ** 2 for i in range(n)) ** 0.5
        errors.append(error)

        if error < tol:
            break

        x = x_new[:]

    return x_new, errors

n = int(input("Enter the size of the matrix: "))
A, B, x_true = generate_diagonally_dominant_matrix(n)

x0 = [0.0] * n

jacobi_result, jacobi_errors = jacobi(A, B, x0, tol=1e-6, max_iterations=100)
gauss_seidel_result, gauss_seidel_errors = gauss_seidel(A, B, x0, tol=1e-6, max_iterations=100)

plt.figure(figsize=(10, 6))
plt.plot(range(1, len(jacobi_errors) + 1), jacobi_errors, label="Jacobi", color="blue")
plt.plot(range(1, len(gauss_seidel_errors) + 1), gauss_seidel_errors, label="Gauss-Seidel", color="red")

plt.yscale("log")
plt.xlabel("Iteration Number")
plt.ylabel("Error (Log Scale)")
plt.title("Convergence of Jacobi and Gauss-Seidel Methods")
plt.legend()
plt.grid(True)
plt.show()
