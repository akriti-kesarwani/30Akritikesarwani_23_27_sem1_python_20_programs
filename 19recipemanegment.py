class Ingredient:
    def __init__(self, name):
        self.name = name

class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    def display_recipe(self):
        print(f"\nRecipe: {self.name}")
        print("Ingredients:")
        for ingredient in self.ingredients:
            print(f"- {ingredient.name}")
        print("Instructions:")
        for step, instruction in enumerate(self.instructions, start=1):
            print(f"{step}. {instruction}")

class User:
    def __init__(self, username):
        self.username = username
        self.saved_recipes = []

    def add_recipe(self, recipe):
        self.saved_recipes.append(recipe)

    def display_recipe_options(self):
        print("Choose a dish:")
        for index, recipe in enumerate(self.saved_recipes, start=1):
            print(f"{index}. {recipe.name}")

    def get_recipe_by_index(self, index):
        if 1 <= index <= len(self.saved_recipes):
            return self.saved_recipes[index - 1]
        return None

# Example usage:

# Create ingredients
ingredient1 = Ingredient("Chicken")
ingredient2 = Ingredient("Onion")
ingredient3 = Ingredient("Garlic")
ingredient4 = Ingredient("Salt")

# Create recipes
recipe1 = Recipe("Chicken Stir Fry", [ingredient1, ingredient2, ingredient3, ingredient4], ["1. Chop the chicken", "2. Saute the vegetables", "3. Add chicken and stir-fry"])
recipe2 = Recipe("Spaghetti Bolognese", [ingredient1, ingredient2, ingredient3], ["1. Cook pasta", "2. Brown the meat", "3. Add sauce"])
recipe3 = Recipe("Vegetable Curry", [ingredient2, ingredient3, ingredient4], ["1. Chop vegetables", "2. Cook in curry sauce"])

# Create a user
user_name = input("Enter your name: ")
user1 = User(user_name)

# Add recipes to the user's collection
user1.add_recipe(recipe1)
user1.add_recipe(recipe2)
user1.add_recipe(recipe3)

# Display dish options to the user
user1.display_recipe_options()

# Ask the user to select a dish
try:
    dish_choice = int(input("Enter the number of the dish you want to view (1, 2, or 3): "))
    selected_recipe = user1.get_recipe_by_index(dish_choice)

    if selected_recipe:
        selected_recipe.display_recipe()
    else:
        print("Invalid option. Please enter a valid number.")
except ValueError:
    print("Invalid input. Please enter a number.")
