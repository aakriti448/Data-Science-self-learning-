# Dictionary of fruits and their calorie counts
fruits = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80
}
# to print calorie in dict: print("calorie of plum is:",fruits["plums"])

# Prompt user for input
item = input("Item: ").lower()

# Output calorie count if fruit is in the dictionary
if item in fruits:
    # print(f"Calories: {fruits[item]}")
    print("calories:", fruits[item])
