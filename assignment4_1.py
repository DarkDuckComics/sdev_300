import numpy as np
import re


def validate_phone_number(phone_number):
    # Use regular expression to validate phone number format
    pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
    while not pattern.match(phone_number):
        phone_number = input("Your phone number is not in correct format. Please reenter: ")
    return phone_number


def validate_zip_code(zip_code):
    # Use regular expression to validate zip code format
    pattern = re.compile(r'\d{5}-\d{4}')
    while not pattern.match(zip_code):
        zip_code = input("Your zip code is not in correct format. Please reenter: ")
    return zip_code


def get_matrix_input():
    # Get input for a 3x3 matrix
    matrix = []
    print("Enter your 3x3 matrix:")
    for _ in range(3):
        row = [float(x) for x in input().split()]
        matrix.append(row)
    return np.array(matrix)


def perform_matrix_operation(matrix_a, matrix_b, operation):
    if operation == 'a':
        result = np.add(matrix_a, matrix_b)
    elif operation == 'b':
        result = np.subtract(matrix_a, matrix_b)
    elif operation == 'c':
        result = np.matmul(matrix_a, matrix_b)
    elif operation == 'd':
        result = np.multiply(matrix_a, matrix_b)
    else:
        print("Invalid operation.")
        return None

    transpose = np.transpose(result)
    row_means = np.mean(result, axis=1)
    column_means = np.mean(result, axis=0)

    return result, transpose, row_means, column_means


def main():
    print("*********** Welcome to the Python Matrix Application ***********")

    while True:
        play_game = input("Do you want to play the Matrix Game? Enter Y for Yes or N for No: ")
        if play_game.lower() != 'y':
            break

        validate_phone_number(input("Enter your phone number (XXX-XXX-XXXX): "))
        validate_zip_code(input("Enter your zip code+4 (XXXXX-XXXX): "))

        matrix_a = get_matrix_input()
        print("Your first 3x3 matrix is:")
        print(matrix_a)

        matrix_b = get_matrix_input()
        print("Your second 3x3 matrix is:")
        print(matrix_b)

        operation = input("Select a Matrix Operation from the list below:\n"
                          "a. Addition\nb. Subtraction\nc. Matrix Multiplication"
                          "\nd. Element by element multiplication\n")

        result, transpose, row_means, column_means = perform_matrix_operation(matrix_a, matrix_b, operation)

        if result is not None:
            print(f"The results are:\n{result}")
            print(f"The Transpose is:\n{transpose}")
            print("The row mean values of the results are:", ', '.join(map(str, row_means)))
            print("The column mean values of the results are:", ', '.join(map(str, column_means)))

    print("*********** Thanks for playing Python Numpy ***************")


if __name__ == "__main__":
    main()
