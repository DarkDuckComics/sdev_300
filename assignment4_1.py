import numpy as np
import pandas as pd
import re


def get_phone_number():
    """Prompt the user to enter a valid phone number."""
    while True:
        try:
            phone_number = input("Enter your phone number (XXX-XXX-XXXX): ")
            if re.match(r'\d{3}-\d{3}-\d{4}', phone_number):
                return phone_number
            else:
                raise ValueError("Invalid phone number format. Please use the format XXX-XXX-XXXX.")
        except ValueError as e:
            print(e)


def get_zip_code():
    """Prompt the user to enter a valid zip code."""
    while True:
        try:
            zip_code = input("Enter your zip code+4 (XXXXX-XXXX): ")
            if re.match(r'\d{5}-\d{4}', zip_code):
                return zip_code
            else:
                raise ValueError("Invalid zip code format. Please use the format XXXXX-XXXX.")
        except ValueError as e:
            print(e)


def get_matrix(prompt):
    """Prompt the user to enter a 3x3 matrix."""
    try:
        matrix_values = []

        # Provide instructions to the user
        print(f"{prompt} (Enter each element separated by a space)")

        # Loop through each row
        for row_num in range(3):
            # Prompt the user to enter elements for each row
            row = input(f"Row {row_num + 1}: Enter elements separated by spaces: ")

            # Convert the entered values to float and append to the matrix
            matrix_values.append(list(map(float, row.split())))

        # Convert the list of lists to a NumPy array
        matrix = np.array(matrix_values)

        # Check if the matrix is 3x3
        if matrix.shape == (3, 3):
            return pd.DataFrame(matrix)
        else:
            raise ValueError("Invalid matrix size. Please enter a valid 3x3 matrix.")
    except ValueError as e:
        # Handle exceptions and print error
        print(e)


def matrix_operations(matrix_a, matrix_b, operation):
    """Perform matrix operations based on the user's choice."""
    try:
        if operation == 'a':
            # Matrix Addition
            result = np.add(matrix_a, matrix_b)
        elif operation == 'b':
            # Matrix Subtraction
            result = np.subtract(matrix_a, matrix_b)
        elif operation == 'c':
            # Matrix Multiplication
            result = np.matmul(matrix_a, matrix_b)
        elif operation == 'd':
            # Element-wise Matrix Multiplication
            result = np.multiply(matrix_a, matrix_b)
        else:
            raise ValueError("Invalid operation selected. Please choose a valid operation (a, b, c, or d).")

        # Return the result, transpose, row mean, and column mean
        return result, result.T, np.mean(result, axis=1), np.mean(result, axis=0)
    except ValueError as e:
        print(e)


def display_results(phone_number, zip_code, results, transpose, row_mean, col_mean):
    """Display user information and matrix operation results."""
    print("User Information:")
    print(f"Phone Number: {phone_number}")
    print(f"Zip Code: {zip_code}")

    print("\nThe results are:")
    print(results)
    print("\nThe Transpose is:")
    print(transpose)
    print("\nThe row mean values of the results are:")
    print(row_mean)
    print("\nThe column mean values of the results are:")
    print(col_mean)


def main():
    """Main function to run the Python Matrix Application."""
    print("***************** Welcome to the Python Matrix Application ***********")

    while True:
        play_game = input("Do you want to play the Matrix Game? Enter Y for Yes or N for No: ")
        if play_game.lower() != 'y':
            print("*********** Thanks for playing Python Numpy ***************")
            break

        try:
            phone_number = get_phone_number()
            zip_code = get_zip_code()

            matrix_a = get_matrix("Enter your first 3x3 matrix element by element")
            print("Your first 3x3 matrix is:")
            print(matrix_a)

            matrix_b = get_matrix("Enter your second 3x3 matrix element by element")
            print("Your second 3x3 matrix is:")
            print(matrix_b)

            operation = input("Select a Matrix Operation from the list below:\n"
                              "a. Addition\nb. Subtraction\nc. Matrix Multiplication\n"
                              "d. Element by element multiplication\n")

            results, transpose, row_mean, col_mean = matrix_operations(matrix_a, matrix_b, operation)
            display_results(phone_number, zip_code, results, transpose, row_mean, col_mean)

        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
