def add_matrix(A, B):
    size = len(A)
    return [[A[i][j] + B[i][j] for j in range(size)] for i in range(size)]


def subtract_matrix(A, B):
    size = len(A)
    return [[A[i][j] - B[i][j] for j in range(size)] for i in range(size)]


def strassen(A, B):

    n = len(A)

    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2

    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    P1 = strassen(add_matrix(A11, A22), add_matrix(B11, B22))
    P2 = strassen(add_matrix(A21, A22), B11)
    P3 = strassen(A11, subtract_matrix(B12, B22))
    P4 = strassen(A22, subtract_matrix(B21, B11))
    P5 = strassen(add_matrix(A11, A12), B22)
    P6 = strassen(subtract_matrix(A21, A11), add_matrix(B11, B12))
    P7 = strassen(subtract_matrix(A12, A22), add_matrix(B21, B22))

    C11 = add_matrix(subtract_matrix(add_matrix(P1, P4), P5), P7)
    C12 = add_matrix(P3, P5)
    C21 = add_matrix(P2, P4)
    C22 = add_matrix(subtract_matrix(add_matrix(P1, P3), P2), P6)

    result = []

    for i in range(mid):
        result.append(C11[i] + C12[i])

    for i in range(mid):
        result.append(C21[i] + C22[i])

    return result


# ---------------- Main Program ---------------- #

matrix_A = [
    [1, 2],
    [3, 4]
]

matrix_B = [
    [5, 6],
    [7, 8]
]

answer = strassen(matrix_A, matrix_B)

print("Matrix A")
for row in matrix_A:
    print(row)

print("\nMatrix B")
for row in matrix_B:
    print(row)

print("\nProduct Matrix")
for row in answer:
    print(row)