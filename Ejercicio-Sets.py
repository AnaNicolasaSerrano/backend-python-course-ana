numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
letters = ["A", "B", "C", "D"]

unique_combinations = set()

for number in numbers:
    for letter in letters:
        unique_combinations.add(f"{number}{number}{number}{number}")
        unique_combinations.add(f"{number}{number}{number}{letter}")
        unique_combinations.add(f"{number}{number}{letter}{number}")
        unique_combinations.add(f"{number}{number}{letter}{letter}")
        unique_combinations.add(f"{number}{letter}{number}{number}")
        unique_combinations.add(f"{number}{letter}{number}{letter}")
        unique_combinations.add(f"{number}{letter}{letter}{number}")
        unique_combinations.add(f"{number}{letter}{letter}{letter}")
        unique_combinations.add(f"{letter}{number}{number}{number}")
        unique_combinations.add(f"{letter}{number}{number}{letter}")
        unique_combinations.add(f"{letter}{number}{letter}{number}")
        unique_combinations.add(f"{letter}{number}{letter}{letter}")
        unique_combinations.add(f"{letter}{letter}{number}{number}")
        unique_combinations.add(f"{letter}{letter}{number}{letter}")
        unique_combinations.add(f"{letter}{letter}{letter}{number}")
        unique_combinations.add(f"{letter}{letter}{letter}{letter}")

# print(unique_combinations)

for unique in unique_combinations:
    print(unique)
