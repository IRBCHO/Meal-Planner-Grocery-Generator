# Name: Benchaphorn Cho (Irene)
# Project: Meal Planner and Grocery Generator - Phrase 3
# Description: This program helps users plan meals for a whole week (3 meals per day), calculates
# the total cost and calorie count, checks if the plan fits within the user's budget,
# recommends a healthy snack, saves favorite meals, and links to an external website
# for more recipes.


# I: User inputs their meal plans, diet preferences, and budget.
# P: The program calculates the total cost, calorie count, and generates a weekly meal plan.
# O: The user receives a formatted meal plan with cost, calorie count, a random healthy snack, save favorite meal, and a URL for additional information.

import tkinter as tk
from tkinter import messagebox, simpledialog, Label
import random
import webbrowser  # For opening a related URL
from datetime import datetime, date, time, timedelta # P3-6 import for system date/time usage


#P3-1: DICTIONARY for meal plans with ingredients, costs, and calories
mealPlans = {
    "Spaghetti": {"cost": 10, "calories": 600, "ingredients":['spaghetti',"ground beef","tomato sauce"]},
    "Salad": {"cost": 5, "calories": 350, "ingredients":["lettuce","tomato","cucumber"]},
    "Tacos": {"cost": 7, "calories": 450, "ingredients":["taco shells","ground beef","cheese"]},
    "Curry": {"cost": 12, "calories": 700, "ingredients":["chicken","curry paste","coconut milk","basil"]},
    "Fried Rice": {"cost": 8, "calories": 550, "ingredients":["rice","egg","soy sauce","oyster sauce"]},
    "Grilled Salmon": {"cost": 15, "calories": 400,"ingredients":["salmon","lemon","olive oil"]},
    "Vegetable Stir-fry": {"cost": 7, "calories": 300,"ingredients":["broccoli","carrot","garlic","soy sauce"]},
    "Lasagna": {"cost": 12, "calories": 800, "ingredients":["lasagna sheets","cheese","tomato sauce"]},
    "Eggs Benedict": {"cost": 10, "calories": 550, "ingredients": ["English muffin", "eggs", "hollandaise sauce", "ham"]},
    "Chia Pudding": {"cost": 4, "calories": 300, "ingredients": ["chia seeds", "milk", "honey", "fruit"]},
    "Hash Browns": {"cost": 4, "calories": 250, "ingredients": ["potatoes", "oil", "salt"]},
    "Fruit Parfait": {"cost": 5, "calories": 300, "ingredients": ["yogurt", "granola", "mixed fruit"]},
    "Tofu Scramble": {"cost": 5, "calories": 250, "ingredients": ["tofu", "vegetables", "spices"]},
    "Sandwich": {"cost": 7, "calories": 500, "ingredients": ["bread", "egg", "cheese", "bacon"]},
    "Scrambled Eggs": {"cost": 3, "calories": 250, "ingredients": ["eggs", "butter", "milk"]}
}

# P3-1: CREATE Dictionary for meal descriptions
mealDetails= {}

# List of healthy snacks
snackList = [
    "Almond","Greek Yogurt","Fruit Salad","Carrot Sticks","Hummus with Veggies","Apple with Peanut butter","Cucumber",
    "Mixed Nuts","Boiled eggs","Smoothie"
]

low_carb_meals = ["Salad", "Grilled Salmon", "Vegetable Stir-fry", "Tofu Scramble","Fruit Parfait","Scrambled Eggs"]
low_sugar_meals = ["Curry", "Grilled Salmon", "Tacos", "Salad","Hash Browns","Chia Pudding","Scrambled Eggs"]

#P3-2 and P3-3: Function to load the dictionary from file1.txt and use a function to load a dictionary
def loadMealDetails():
    try:
        with open("file1.txt", "r") as f1:
          while True:
               record = f1.readline()
               if (record == ""):
                    break
               record = record.strip()
               if ":" not in record:
                   continue
               try:
                  k, v = record.strip().split(":")
                  mealDetails[k] = v.capitalize() # P3-4: Use .capitalize() to format descriptions
               except ValueError:
                   messagebox.showerror("File Error",f"invalid format inline: {record}")
    except FileNotFoundError:
           messagebox.showerror("File Error","File1.txt not found. Please make sure the file exists.")

# P3-7: Ask for the user's name
def askName():
    name = simpledialog.askstring("Your name","Please enter your name:")
    if not name:
        name = "User"
    return name

# Function to create a weekly meal plan
def weekly_meal_plan(dietType):
    weeklyPlan = {"Breakfast": [], "Lunch": [], "Dinner": []}

    # Meal options for each time of day
    breakfastChoices = ["Fried Rice", "Salad","Eggs Benedict","Fruit Parfait","Chia Pudding","Scrambled Eggs"]
    lunchChoices = ["Spaghetti", "Grilled Salmon", "Lasagna","Salad","Sandwich","Scrambled Eggs"]
    dinnerChoices = ["Curry", "Vegetable Stir-fry", "Tacos","Tofu Scramble","Fried Rice","Grilled Salmon","Spaghetti","Lasagna"]

    # Adjust meals based on diet type (low-carb or low-sugar)
    if dietType == 1: #low-carb
        breakfastChoices = [meal for meal in breakfastChoices if meal in low_carb_meals]
        lunchChoices = [meal for meal in lunchChoices if meal in low_carb_meals]
        dinnerChoices = [meal for meal in dinnerChoices if meal in low_carb_meals]
    elif dietType == 2: #low-sugar
        breakfastChoices = [meal for meal in breakfastChoices if meal in low_sugar_meals]
        lunchChoices = [meal for meal in lunchChoices if meal in low_sugar_meals]
        dinnerChoices = [meal for meal in dinnerChoices if meal in low_sugar_meals]

    #Loop to generate the meal plan for 7 days (3 meals per day)
    for day in range(7):
        weeklyPlan["Breakfast"].append(random.choice(breakfastChoices))
        weeklyPlan["Lunch"].append(random.choice(lunchChoices))
        weeklyPlan["Dinner"].append(random.choice(dinnerChoices))

    return weeklyPlan


# Function to calculate total cost and calories
def costCalories(weeklyPlan):
    totalCost = 0
    totalCalories = 0
    dailyBreakdown = ""

    for day in range(7):
        breakfast = weeklyPlan["Breakfast"][day]
        lunch = weeklyPlan["Lunch"][day]
        dinner = weeklyPlan["Dinner"][day]

        # Calculate daily cost and calories
        dayCost = mealPlans[breakfast]["cost"] + mealPlans[lunch]["cost"] + mealPlans[dinner]["cost"]
        dayCalories = mealPlans[breakfast]["calories"] + mealPlans[lunch]["calories"] + mealPlans[dinner][
            "calories"]

        totalCost += dayCost
        totalCalories += dayCalories

        # Breakdown of the day
        dailyBreakdown += f"Day {day + 1}:\n"
        dailyBreakdown += f"  Breakfast: {breakfast} (${mealPlans[breakfast]['cost']}, {mealPlans[breakfast]['calories']} calories)\n"
        dailyBreakdown += f"  Lunch: {lunch} (${mealPlans[lunch]['cost']}, {mealPlans[lunch]['calories']} calories)\n"
        dailyBreakdown += f"  Dinner: {dinner} (${mealPlans[dinner]['cost']}, {mealPlans[dinner]['calories']} calories)\n"
        dailyBreakdown += f"  Daily Total: ${dayCost}, {dayCalories} calories\n\n"

    return totalCost, totalCalories, dailyBreakdown

# Function to generate a grocery list based on the weekly plan
def generateGrocery_list(weeklyPlan):
    groceryList = []
    itemCount = 0
    for day in range(7):
        breakfast = weeklyPlan["Breakfast"][day]
        lunch = weeklyPlan["Lunch"][day]
        dinner = weeklyPlan["Dinner"][day]

        # add ingredients for breakfast,lunch, and dinner to grocery list
        groceryList.extend(mealPlans[breakfast]["ingredients"])
        groceryList.extend(mealPlans[lunch]["ingredients"])
        groceryList.extend(mealPlans[dinner]["ingredients"])

    # Remove duplicates from the grocery list
    groceryList = list(set(groceryList))

    #Abbreviated incrementor to count the total number of items in grocery list
    for item in groceryList:
        itemCount += 1

    messagebox.showinfo("Item Count",f"You have {itemCount} grocery items to buy. ")

    return groceryList


# P3-7: Function to display meal plan and budget status
def displayMealplan(weeklyPlan, budget):
    totalCost, totalCalories, dailyBreakdown = costCalories(weeklyPlan)

    # Display total cost, calories, and daily breakdown
    planSummary = f"{dailyBreakdown}\nTotal Weekly Cost: ${totalCost}\nTotal Weekly Calories: {totalCalories} calories"

    #Compound condition to check if the total cost exceeds the budget
    if totalCost > budget:
        planSummary += f"\n\n⚠️ Your total weekly meal cost of ${totalCost:.2f} exceeds your budget of ${budget:.2f}.😱"
    else:
        planSummary += f"\n\n✅ Your total weekly meal cost of ${totalCost:.2f} is within your budget of ${budget:.2f}.😄"

    messagebox.showinfo("Weekly Meal Plan", planSummary)

    # Generate and display grocery list
    groceryList = generateGrocery_list(weeklyPlan)
    groceryList_str = "\n".join(groceryList)
    messagebox.showinfo("Grocery List",f"Here is your grocery list for the week:\n{groceryList_str}")

# P3-5: Error-Validation loop for budget input
def ask_budget():
    budget = None
    while budget is None or budget <= 0:  # Ensure valid budget entry
        try:
            budget = simpledialog.askfloat("Budget", "Enter your weekly grocery budget (USD):")
            if budget <= 0:
                messagebox.showerror("Input Error", "Please enter a valid budget greater than 0.")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid numeric value for your budget.")
    return budget

# View meal details from file1.txt
def viewMealDetails():
    try:
        with open("file1.txt", "r") as f:
            details = f.read()

        # Split into lines so we don't overflow the messagebox
        lines = details.splitlines()
        max_lines = 25  # adjust if you want more/less

        if len(lines) > max_lines:
            shown_text = "\n".join(lines[:max_lines])
            shown_text += "\n...\n(Full details are in file1.txt)"
        else:
            shown_text = details

        messagebox.showinfo("Meal Descriptions", shown_text)

    except FileNotFoundError:
        messagebox.showerror("Error", "file1.txt not found. Please ensure the file is in the correct location.")



# Function to suggest a random healthy snack
def healthySnackSuggestion():
    snack = random.choice(snackList)
    messagebox.showinfo("Healthy Snack Suggestion", f"How about try this snack: {snack}?")

#P3-9  Add another feature you want to include that is not on this requirement list.
def addFav(meal):
    with open ("favorite.txt", "a") as file:
        file.write(meal + "\n")
    messagebox.showinfo("Favorite",f"{meal} has been added to your favorite meal")

#P3-9  Add another feature you want to include that is not on this requirement list.
def viewFav():
    try:
        with open("favorite.txt", "r") as file:
            favorites = file.readlines()
        if favorites:
            favorites = [meal.strip() for meal in favorites]
            messagebox.showinfo("Favorite meal","Here is you favorite meals:\n" + "\n".join(favorites))
        else:
            messagebox.showinfo("Favorite Meal","You don't have any favorite meal yet!")
    except FileNotFoundError:
        messagebox.showinfo("Favorite Meal","No favorites found. Stat adding some!")

#p3-6: Add a time-based greeting
def timeGreeting():
    currentHour = datetime.now().hour
    if currentHour < 12:
        greeting = "Good morning"
    elif currentHour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"
    messagebox.showinfo("Greeting",f"{greeting}, 🍽Welcome to the Meal Planner and Grocery Generator!")

# Main function to run the program

def main():

    # Load meal descriptions from file
    loadMealDetails()

    # Display time-based greeting
    timeGreeting()

    name = askName()

    # Ask for the user's budget
    budget = ask_budget()

    # Ask for diet preferences
    dietType = simpledialog.askstring(
        "Diet Preference",
        "Enter your diet type:\n1. Low-carb\n2. Low-sugar\n3. None"
    )

    # Validate input
    if dietType not in ["1", "2", "3"]:
        messagebox.showerror("Error", "Invalid diet type. Please enter 1, 2, or 3")
        return

    # Convert from string to int so weekly_meal_plan works correctly
    dietType_int = int(dietType)

    # Create the weekly meal plan
    weeklyPlan = weekly_meal_plan(dietType_int)

    # Display the meal plan, cost, and calories with respect to the budget
    displayMealplan(weeklyPlan, budget)

    # Suggest a healthy snack
    healthySnackSuggestion()

    # Add favorite meal
    favoriteMeal = simpledialog.askstring(
        "Favorite",
        "Would you like to add a meal to favorites? Enter the meal name or type 'no': "
    )
    if favoriteMeal and favoriteMeal.lower() != "no":
        addFav(favoriteMeal.capitalize())

    # Ask if the user wants to view meal details from file1.txt
    open_details = messagebox.askyesno(
        "Meal Details",
        "Would you like to open file1.txt to see more meal descriptions?"
    )

    print("DEBUG: User clicked YES" if open_details else "DEBUG: User clicked NO")

    if open_details:
        print("DEBUG: Calling viewMealDetails")
        viewMealDetails()
    else:
        print("DEBUG: Skipping viewMealDetails")

    # Open an external URL
    if messagebox.askyesno("More Info", "Do you want to check out more recipes? "):
        webbrowser.open("http://www.mealime.com")
    else:
        messagebox.showinfo(
            "Goodbye",
            "Thank you so much for using the Meal Planner and Grocery Generator!"
        )


# Execute the main window
main()

