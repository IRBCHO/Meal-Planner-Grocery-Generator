# 🥗 Meal Planner & Grocery Generator  
by **Benchaphorn (Irene) Cho**

A Python desktop application built with **Tkinter** that helps users plan meals for a full week (3 meals per day), calculates total cost and calories, generates a grocery list, suggests healthy snacks, saves favorite meals, and optionally opens a recipe website for more ideas.

This project demonstrates GUI development, file handling, dictionaries, randomization, and user-driven workflow design — perfect for showcasing early software development skills.

---

## ✨ Features

### ✅ User Input Prompts
- Enter your name  
- Set a weekly grocery budget  
- Choose diet type: **Low-Carb**, **Low-Sugar**, or **None**

### ✅ Generates a Full 7-Day Meal Plan
- Breakfast, lunch, and dinner  
- Cost per meal  
- Calories per meal  
- Total weekly cost & calories  
- Budget validation

### ✅ Grocery List Generator
- Collects ingredients from all meals  
- Removes duplicates  
- Displays total item count  
- Generates full grocery list

### ✅ Healthy Snack Suggestions  
Randomly recommends a healthy snack for the day.

### ✅ Favorite Meals  
- Add favorite meals  
- Auto-saves to **favorite.txt**

### ✅ Meal Descriptions  
Reads details from **file1.txt** and displays them in a **scrollable Tkinter popup window**.

### ✅ External Recipe Link  
Optionally opens **mealime.com** for more recipes.

---

## 📸 Application Screenshots  

### 👤 User Name Input  
![User Name Input](screenshots/IMG_9202.jpeg)

### 💰 Budget Input  
![Budget Input](screenshots/IMG_9204.jpeg)

### 🥗 Diet Preference  
![Diet Preference](screenshots/IMG_9205.jpeg)

### 🍽 Generated Weekly Meal Plan  
![Meal Plan](screenshots/IMG_9208.jpeg)

### 🔢 Grocery Item Count  
![Item Count](screenshots/IMG_9209.jpeg)

### 🛒 Grocery List  
![Grocery List](screenshots/IMG_9210.jpeg)

### 🥕 Healthy Snack Suggestion  
![Snack Suggestion](screenshots/IMG_9211.jpeg)

### ⭐ Add Favorite Meal  
![Add Favorite](screenshots/IMG_9212.jpeg)

### ✅ Favorite Confirmation  
![Favorite Confirmation](screenshots/IMG_9213.jpeg)

### 📄 Open Meal Descriptions  
![Open File](screenshots/IMG_9214.jpeg)

### 📖 Meal Description Window  
![Meal Details](screenshots/IMG_9215.jpeg)

### 🌐 Open External Recipes  
![External Recipes](screenshots/IMG_9216.jpeg)

### 🧃 Additional Snack Suggestion  
![Another Snack](screenshots/IMG_9219.jpeg)

### 🙌 Final Thank You Message  
![Thank You](screenshots/IMG_9220.jpeg)

---

## 🛠 Technologies Used
- Python 3  
- Tkinter (GUI)  
- Random module  
- Datetime  
- File I/O  
- Webbrowser module  

---

## 📁 Project Structure  

Meal-Planner-Grocery-Generator/
│── meal_planner.py          # Main application file
│── file1.txt                # Meal descriptions database
│── favorite.txt             # Stores user favorite meals
│── README.md                # Project documentation
│── screenshot/              # Application screenshots
│     ├── IMG_9202.jpeg
│     ├── IMG_9204.jpeg
│     ├── IMG_9205.jpeg
│     ├── ...

---

## How to Run
1. Install Python 3  
2. Download or clone this repository  
3. Make sure meal_planner.py, file1.txt, and favorite.txt are in the same folder  
4. Run the program:
   python3 meal_planner.py

👩🏻‍💻 Author

Benchaphorn (Irene) Cho
GitHub: IRBCHO
