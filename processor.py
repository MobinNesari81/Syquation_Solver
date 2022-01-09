# All functions and formulas implemented here.
def transpose_matrix(m):
    return map(list, zip(*m))


def get_matrix_minor(m, i, j):
    return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]


def get_matrix_determinant(m):
    # base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1) ** c) * m[0][c] * get_matrix_determinant(get_matrix_minor(m, 0, c))
    return determinant


def get_matrix_inverse(m):
    determinant = get_matrix_determinant(m)
    # special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1] / determinant, -1 * m[0][1] / determinant],
                [-1 * m[1][0] / determinant, m[0][0] / determinant]]

    # find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactor_row = []
        for c in range(len(m)):
            minor = get_matrix_minor(m, r, c)
            cofactor_row.append(((-1) ** (r + c)) * get_matrix_determinant(minor))
        cofactors.append(cofactor_row)
    cofactors = list(transpose_matrix(cofactors))
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c] / determinant
    return cofactors


def matrix_multiplication(m1, m2):
    result = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]
    # iterating by row of A
    for i in range(len(m1)):

        # iterating by column by B
        for j in range(len(m2[0])):

            # iterating by rows of B
            for k in range(len(m2)):
                result[i][j] += m1[i][k] * m2[k][j]
    return result


def matrix_printer(m):
    for i in m:
        print(*i)


def equation_solver(coefficient_matrix, constants_matrix) -> list:
    if get_matrix_determinant(coefficient_matrix) == 0:
        return None
    result = matrix_multiplication(get_matrix_inverse(coefficient_matrix), constants_matrix)
    return result


def answer_printer(variable_matrix, results_matrix) -> None:
    for i in range(len(variable_matrix)):
        print(f"\t{variable_matrix[i]} = {results_matrix[i][0]}")
