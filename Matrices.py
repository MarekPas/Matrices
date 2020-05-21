def print_menu():
    print("""
1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
0. Exit
""")


def check_matrix(matrix_sizeA, matrix_sizeB):
    if int(matrix_sizeA[1]) == int(matrix_sizeB[0]):
        return True
    else:
        print('Impossible to multiply this matrices!')
        return False


def enter_matrix(matrix_size):
    matrix = []
    #print(matrix)
    for x in range(int(matrix_size[0])):
        row = input().split()
        matrix.append([float(s) for s in row])
    return matrix


def enter_size_of_matrix(amount=2, is_same=False):
    matrix_sizeA = input("Enter size of first martix: ").split()
    if amount == 2:
        print("Enter first matrix: ")
    elif amount == 1:
        print("Enter matrix: ")
    matrixA = enter_matrix(matrix_sizeA)
    if amount == 1:
        return matrixA
    elif amount == 2:
        matrix_sizeB = input("Enter size of second martix: ").split()
        print("Enter second matrix: ")
        matrixB = enter_matrix(matrix_sizeB)
        if is_same == True:
            if check_matrix(matrix_sizeA, matrix_sizeB):
                return matrixA, matrixB
            else:
                print("Try again...")
                pass


def add_matrices(m1, m2):
    return [[m1[i][j] + m2[i][j] for j in range(len(m1[0]))] for i in range(len(m2))]


def multiply_matrices_by_constant(matrix, const):
    new_matrix = []
    for row in matrix:
        temp_matrix = [int(num * const) for num in row]
        new_matrix.append(temp_matrix)
    return new_matrix


def multiply_matrices(m1, m2):
    return [[sum(a * b for a, b in zip(x_row, y_col)) for y_col in zip(*m2)] for x_row in m1]


def print_matrix(result):
    print("The result is:")
    for row in result:
        print(*row)

while True:
    print_menu()
    try:
        choice = int(input("Your choice: "))
        if choice == 1:
            matrixA, matrixB = enter_size_of_matrix(is_same=True)
            print_matrix(add_matrices(matrixA, matrixB))

        elif choice == 2:
            matrixA = enter_size_of_matrix(amount=1)
            constant = int(input("Enter constant: "))
            print_matrix(multiply_matrices_by_constant(matrixA, constant))

        elif choice == 3:
            matrixA, matrixB = enter_size_of_matrix(is_same=True)
            print_matrix(multiply_matrices(matrixA, matrixB))

        elif choice == 0:
            break
        else:
            print("You must enter a number from 0 to 4!")
    except:
        print("ERROR")
