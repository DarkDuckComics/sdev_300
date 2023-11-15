import matplotlib.pyplot as plt
from PIL import Image
import os

# Define all 50 states data in a dictionary
state_data = {
    "Alabama": {"Capital": "Montgomery", "Population": 196010, "Flower": "Camellia"},
    "Alaska": {"Capital": "Juneau", "Population": 31534, "Flower": "Forget-me-not"},
    "Arizona": {"Capital": "Phoenix", "Population": 1651344, "Flower": "Saguaro Cactus Blossom"},
    "Arkansas": {"Capital": "Little Rock", "Population": 201029, "Flower": "Apple Blossom"},
    "California": {"Capital": "Sacramento", "Population": 528306, "Flower": "California Poppy"},
    "Colorado": {"Capital": "Denver", "Population": 699288, "Flower": "Rocky Mountain Columbine"},
    "Connecticut": {"Capital": "Hartford", "Population": 119817, "Flower": "Mountain Laurel"},
    "Delaware": {"Capital": "Dover", "Population": 37892, "Flower": "Peach Blossom"},
    "Florida": {"Capital": "Tallahassee", "Population": 198631, "Flower": "Orange Blossom"},
    "Georgia": {"Capital": "Atlanta", "Population": 490270, "Flower": "Cherokee Rose"},
    "Hawaii": {"Capital": "Honolulu", "Population": 337088, "Flower": "Hibiscus"},
    "Idaho": {"Capital": "Boise", "Population": 240713, "Flower": "Syringa"},
    "Illinois": {"Capital": "Springfield", "Population": 111711, "Flower": "Violet"},
    "Indiana": {"Capital": "Indianapolis", "Population": 871449, "Flower": "Peony"},
    "Iowa": {"Capital": "Des Moines", "Population": 208734, "Flower": "Wild Rose"},
    "Kansas": {"Capital": "Topeka", "Population": 125353, "Flower": "Sunflower"},
    "Kentucky": {"Capital": "Frankfort", "Population": 28523, "Flower": "Goldenrod"},
    "Louisiana": {"Capital": "Baton Rouge", "Population": 217665, "Flower": "Magnolia"},
    "Maine": {"Capital": "Augusta", "Population": 19058, "Flower": "White Pine"},
    "Maryland": {"Capital": "Annapolis", "Population": 40397, "Flower": "Black-eyed Susan"},
    "Massachusetts": {"Capital": "Boston", "Population": 617459, "Flower": "Mayflower"},
    "Michigan": {"Capital": "Lansing", "Population": 112460, "Flower": "Apple Blossom"},
    "Minnesota": {"Capital": "St. Paul", "Population": 299830, "Flower": "Pink and White Lady's Slipper"},
    "Mississippi": {"Capital": "Jackson", "Population": 143776, "Flower": "Magnolia"},
    "Missouri": {"Capital": "Jefferson City", "Population": 42535, "Flower": "Hawthorn"},
    "Montana": {"Capital": "Helena", "Population": 34690, "Flower": "Bitterroot"},
    "Nebraska": {"Capital": "Lincoln", "Population": 295222, "Flower": "Goldenrod"},
    "Nevada": {"Capital": "Carson City", "Population": 59630, "Flower": "Sagebrush"},
    "New Hampshire": {"Capital": "Concord", "Population": 44606, "Flower": "Purple Lilac"},
    "New Jersey": {"Capital": "Trenton", "Population": 90048, "Flower": "Purple Violet"},
    "New Mexico": {"Capital": "Santa Fe", "Population": 89220, "Flower": "Yucca"},
    "New York": {"Capital": "Albany", "Population": 97593, "Flower": "Rose"},
    "North Carolina": {"Capital": "Raleigh", "Population": 472540, "Flower": "Dogwood"},
    "North Dakota": {"Capital": "Bismarck", "Population": 75073, "Flower": "Wild Prairie Rose"},
    "Ohio": {"Capital": "Columbus", "Population": 907865, "Flower": "Scarlet Carnation"},
    "Oklahoma": {"Capital": "Oklahoma City", "Population": 697763, "Flower": "Oklahoma Rose"},
    "Oregon": {"Capital": "Salem", "Population": 181620, "Flower": "Oregon Grape"},
    "Pennsylvania": {"Capital": "Harrisburg", "Population": 50267, "Flower": "Mountain Laurel"},
    "Rhode Island": {"Capital": "Providence", "Population": 188877, "Flower": "Violet"},
    "South Carolina": {"Capital": "Columbia", "Population": 137996, "Flower": "Yellow Jessamine"},
    "South Dakota": {"Capital": "Pierre", "Population": 13954, "Flower": "Pasque Flower"},
    "Tennessee": {"Capital": "Nashville", "Population": 658525, "Flower": "Iris"},
    "Texas": {"Capital": "Austin", "Population": 966292, "Flower": "Bluebonnet"},
    "Utah": {"Capital": "Salt Lake City", "Population": 202272, "Flower": "Sego Lily"},
    "Vermont": {"Capital": "Montpelier", "Population": 7988, "Flower": "Red Clover"},
    "Virginia": {"Capital": "Richmond", "Population": 226472, "Flower": "American Dogwood"},
    "Washington": {"Capital": "Olympia", "Population": 56510, "Flower": "Western Rhododendron"},
    "West Virginia": {"Capital": "Charleston", "Population": 46692, "Flower": "Rhododendron"},
    "Wisconsin": {"Capital": "Madison", "Population": 269897, "Flower": "Wood Violet"},
    "Wyoming": {"Capital": "Cheyenne", "Population": 64831, "Flower": "Indian Paintbrush"},
}


def display_states():
    """
    Function to display all U.S. States
    """
    print("List of U.S. States in Alphabetical Order:")
    for state in sorted(state_data.keys()):
        state_info = state_data[state]
        print(
            f"State: {state}, Capital: {state_info['Capital']},"
            f" Population: {state_info['Population']}, Flower: {state_info['Flower']}")


def search_state(state_name):
    """
    Function to search for a specific state
    :param state_name:
    :return:
    """
    state_name = state_name.capitalize()
    if state_name in state_data:
        state_info = state_data[state_name]
        capital = state_info["Capital"]
        population = state_info["Population"]
        flower = state_info["Flower"]
        print(f"{state_name} - Capital: {capital}, Population: {population}, Flower: {flower}")
        flower_image_path = f"images/{state_name}_flower.jpg"
        if os.path.exists(flower_image_path):
            img = Image.open(flower_image_path)
            img.show()
    else:
        print(f"{state_name} not found in the list of U.S. states.")


def create_population_bar_graph():
    """
    Function to create a bar graph of the top 5 populated states
    :return:
    """
    top_states = sorted(state_data.keys(), key=lambda x: state_data[x]["Population"], reverse=True)[:5]
    population_data = [state_data[state]["Population"] for state in top_states]
    plt.figure(figsize=(10, 6))
    plt.bar(top_states, population_data)
    plt.xlabel("State")
    plt.ylabel("Population")
    plt.title("Top 5 Populated States")
    plt.show()


def update_population(states_name, new_populations):
    """
    Function to update the population of a specific state
    :param states_name:
    :param new_populations:
    :return:
    """
    states_name = states_name.capitalize()
    if states_name in state_data:
        state_data[states_name]["Population"] = new_populations
        print(f"Updated population of {states_name} to {new_populations}.")
    else:
        print(f"{states_name} not found in the list of U.S. states.")


# Main menu
while True:
    print("\nMenu:")
    print("1. Display all U.S. States")
    print("2. Search for a specific state")
    print("3. Create a bar graph of the top 5 populated states")
    print("4. Update state population")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    try:
        choice = int(choice)
        if choice == 1:
            display_states()
        elif choice == 2:
            user_state_name = input("Enter the name of the state you want to search: ")
            search_state(user_state_name)
        elif choice == 3:
            create_population_bar_graph()
        elif choice == 4:
            user_state_name = input("Enter the name of the state you want to update: ")
            new_population = input("Enter the new population: ")
            if new_population.isnumeric():
                update_population(user_state_name, int(new_population))
            else:
                print("Invalid population. Please enter a numeric value.")
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1-5).")
    except ValueError:
        print("Invalid input. Please enter a valid numeric choice (1-5).")
