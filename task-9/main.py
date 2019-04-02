matrix = [
    [0, 1, 2, 3, 2, 3],
    [3, 4, 5, 6, 5, 1],
    [8, 4, 2, 1, 6, 8],
    [9, 2, 3, 2, 9, 10],
    [10, 11, 3, 2, 9, 33],
    [5, 11, 3, 4, 3, 3],
]

def get_minor_matrix(M, column_index):
    work_matrix = M[1:]
    minor_matrix = []
    work_matrix_len = len(work_matrix)
    M_len = len(M)
    for i in range(0, work_matrix_len):
        minor_matrix.append([])
        work_row = minor_matrix[-1]

        for j in range(0, M_len):
            if j == column_index:
                continue
            work_row.append(work_matrix[i][j])

    return minor_matrix

def get_det(M):
    M_len = len(M)
    result = 0

    if M_len == 1:
        return M[0][0]

    for k in range(0, M_len):
        sign = (-1)**(k + 2)
        minor_matrix = get_minor_matrix(M, k)

        result += sign * M[0][k] * get_det(minor_matrix)

    return result

print(get_det(matrix))
