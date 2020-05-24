def print_menu():
    print("""
1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
0. Exit
""")


def print_menu2():
    print("""
1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line
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
        row = tuple(input().split())
        matrix.append([float(s) if "." in s else int(s) for s in row])
        #print(matrix)
    return matrix


def enter_size_of_matrix(amount=2, is_same=False):
    if amount == 1:
        matrix_sizeA = input("Enter size of the martix: ").split()
        print("Enter matrix: ")
        return enter_matrix(matrix_sizeA)
    elif amount == 2:
        matrix_sizeA = input("Enter size of first martix: ").split()
        print("Enter first matrix: ")
        matrixA = enter_matrix(matrix_sizeA)
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
    return [[m1[i][j] + m2[i][j]  for j in range(len(m1[0]))] for i in range(len(m2))]


def multiply_matrices_by_constant(matrix, const):
    new_matrix = []
    for row in matrix:
        temp_matrix = [int(num * const) for num in row]
        new_matrix.append(temp_matrix)
    return new_matrix


def multiply_matrices(m1, m2):
    return [[sum(a * b for a, b in zip(x_row, y_col)) for y_col in zip(*m2)] for x_row in m1]


def transpose_matrix(matrix, method):
    length = len(matrix[0]) - 1
    if method == 1:
        return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    elif method == 2:
        return [[matrix[length-j][length-i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    elif method == 3:   # vertical
        return [[matrix[i][length-j] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    elif method == 4:   # horizontal
        return [[matrix[length-i][j] for j in range(len(matrix))] for i in range(len(matrix[0]))]


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

        elif choice == 4:
            print_menu2()
            choice2 = int(input("Your choice: "))
            matrixA = enter_size_of_matrix(amount=1)
            if choice2 == 1:
                print_matrix(transpose_matrix(matrixA, choice2))
            elif choice2 == 2:
                print_matrix(transpose_matrix(matrixA, choice2))
            elif choice2 == 3:
                print_matrix(transpose_matrix(matrixA, choice2))
            elif choice2 == 4:
                print_matrix(transpose_matrix(matrixA, choice2))

        elif choice == 0:
            break
        else:
            print("You must enter a number for 0 to 4!")
    except:
        print("ERROR")
