# Main file which solve equation
import processor
coefficient_rows = int(input("Please enter coefficient matrix row numbers: "))
coefficient_columns = int(input("Please enter coefficient matrix column numbers: "))
coefficient_matrix = [[] for _ in range(coefficient_rows)]
print("Please enter coefficients in one row then another one: ")
for i in range(coefficient_rows):
    coefficient_matrix[i] = [int(k) for k in input().split()]
variables_numbers = int(input("Please enter variables numbers: "))
variables_matrix = []
for i in range(variables_numbers):
    variables_matrix.append(input(f"Please enter {i+1} variable's symbol: "))
constants_matrix = [[0] for _ in range(coefficient_rows)]
for i in range(coefficient_rows):
    constants_matrix[i][0] = int(input(f"Please enter {i+1} constant: "))
print('-' * 10)
print("Answer: ")
answer = processor.equation_solver(coefficient_matrix, constants_matrix)
processor.answer_printer(variables_matrix, answer)
