# 🥗 Meal Planner & Grocery Generator  
by **Benchaphorn (Irene) Cho**

A Python **desktop application** built with **Tkinter** that helps users plan meals for a full week (3 meals per day), calculate total cost and calories, generate a grocery list, suggest healthy snacks, save favorite meals, and optionally open a recipe website for more ideas.

This project demonstrates:
- GUI development  
- File handling  
- Python dictionaries & data structures  
- Randomization  
- Event-driven workflow design  

Perfect for showcasing early software development skills.

---

## ✨ Features

### ✅ User Input Prompts
- Enter your name  
- Set a weekly grocery budget  
- Choose diet type: **Low-Carb**, **Low-Sugar**, or **None**

### ✅ 7-Day Meal Plan Generator
- Breakfast, lunch, and dinner for all 7 days  
- Cost per meal  
- Calories per meal  
- Total weekly cost & calorie calculation  
- Alerts if the total cost exceeds your budget

### ✅ Grocery List Generator
- Pulls ingredients from all meals  
- Removes duplicate items  
- Displays total ingredient count  
- Shows full grocery list in a scrollable window  

### ✅ Healthy Snack Suggestions  
A random healthy snack appears whenever requested.

### ✅ Favorite Meals
- Add favorite meals with one click  
- Automatically saved to **favorite.txt**  

### ✅ Meal Descriptions
- Reads detailed meal descriptions from **file1.txt**  
- Displays descriptions in a scrollable Tkinter popup window  

### ✅ External Recipe Website  
- Opens **mealime.com** (or any recipe website) using Python’s `webbrowser` module  

---

## 🖼 Screenshots

*(Place your screenshots in the root folder or inside a /screenshots folder and update the paths)*

![Name Input](./IMG_9202.jpeg)
![Budget Input](./IMG_9204.jpeg)
![Diet Choice](./IMG_9205.jpeg)
![Weekly Plan](./IMG_9208.jpeg)
![Ingredient Count](./IMG_9209.jpeg)
![Grocery List](./IMG_9210.jpeg)
![Snack Suggestion](./IMG_9211.jpeg)
![Add Favorite](./IMG_9212.jpeg)
![Favorite Saved](./IMG_9213.jpeg)
![Meal Description](./IMG_9214.jpeg)
![Recipe Website](./IMG_9215.jpeg)
![Another Snack](./IMG_9216.jpeg)
![Thank You Screen](./IMG_9219.jpeg)

---

## 🧰 Technologies Used

- **Python 3**
- **Tkinter** for GUI  
- `random`  
- `datetime`  
- `webbrowser`  
- File I/O operations  

---

## 📁 Project Structure

```text
Meal-Planner-Grocery-Generator/
│── projectPhrase3nene.py       # Main application file
│── file1.txt                   # Meal descriptions database
│── favorite.txt                # Stores user favorite meals
│── README.md                   # Project documentation
│── IMG_9202.jpeg               # Screenshots
│── IMG_9204.jpeg
│── IMG_9205.jpeg
│── ... (other images)
