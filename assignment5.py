import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Function to load data from a CSV file
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
        return None


# Function to analyze data and generate statistics and histograms
def analyze_data(data, column_name, color='blue'):
    if column_name not in data.columns:
        print("Invalid column name. Please select a valid column.")
        return

    column_data = data[column_name]

    statistics = {
        'Count': column_data.count(),
        'Mean': column_data.mean(),
        'Standard Deviation': column_data.std(),
        'Min': column_data.min(),
        'Max': column_data.max()
    }

    print(f"The statistics for column {column_name} are:")
    for stat, value in statistics.items():
        print(f"{stat} = {value}")

    plt.hist(column_data, bins=20, color=color, edgecolor='black')
    plt.xlabel(column_name)
    plt.ylabel('Frequency')
    plt.title(f'Histogram of {column_name}')
    plt.show()


def select_column(data, columns):
    while True:
        print("Select the Column you want to analyze:")
        for idx, column in enumerate(columns):
            print(f"{chr(ord('a') + idx)}. {column}")

        print(f"{chr(ord('a') + len(columns))}. Exit Column")

        column_choice = input().lower()

        if column_choice == chr(ord('a') + len(columns)):
            print("You selected to exit the column menu")
            break
        elif column_choice in [chr(ord('a') + i) for i in range(len(columns))]:
            selected_column = columns[ord(column_choice) - ord('a')]
            analyze_data(data, selected_column)
        else:
            print("Invalid choice. Please enter a valid option.")


def main():
    print("***************** Welcome to the Python Data Analysis App**********")

    while True:
        print("Select the file you want to analyze:")
        print("1. Population Data")
        print("2. Housing Data")
        print("3. Exit the Program")

        choice = input()

        if choice == '1':
            population_data_path = r"C:\Users\xXste\Downloads\PopChange.csv"  # Path to local file
            population_data = load_data(population_data_path)

            if population_data is not None:
                while True:
                    print("Select the Column you want to analyze:")
                    print("a. Pop Apr 1")
                    print("b. Pop Jul 1")
                    print("c. Change Pop")
                    print("d. Exit Column")

                    column_choice = input()
                    if column_choice == 'a':
                        analyze_data(population_data, 'Pop Apr 1')
                    elif column_choice == 'b':
                        analyze_data(population_data, 'Pop Jul 1')
                    elif column_choice == 'c':
                        analyze_data(population_data, 'Change Pop')
                    elif column_choice == 'd':
                        break
                    else:
                        print("Invalid choice. Please enter a valid option.")
        elif choice == '2':
            housing_data_path = r"C:\Users\xXste\Downloads\Housing.csv"  # Path to local file
            housing_data = load_data(housing_data_path)

            if housing_data is not None:
                while True:
                    print("Select the Column you want to analyze:")
                    print("a. AGE")
                    print("b. BEDRMS")
                    print("c. BUILT")
                    print("d. ROOMS")
                    print("e. UTILITY")
                    print("f. Exit Column")

                    column_choice = input()
                    if column_choice == 'a':
                        analyze_data(housing_data, 'AGE')
                    elif column_choice == 'b':
                        analyze_data(housing_data, 'BEDRMS')
                    elif column_choice == 'c':
                        analyze_data(housing_data, 'BUILT')
                    elif column_choice == 'd':
                        analyze_data(housing_data, 'ROOMS')
                    elif column_choice == 'e':
                        analyze_data(housing_data, 'UTILITY')
                    elif column_choice == 'f':
                        break
                    else:
                        print("Invalid choice. Please enter a valid option.")
        elif choice == '3':
            print("*************** Thanks for using the Data Analysis App**********")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
