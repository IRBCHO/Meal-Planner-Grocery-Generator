# 🥗 Meal Planner & Grocery Generator  
by **Benchaphorn (Irene) Cho**

A Python desktop application built with **Tkinter** that helps users:

- Plan meals for a full week (3 meals per day)
- Calculate cost and calories for each meal
- Generate a full grocery list
- Suggest healthy snacks
- Save favorite meals
- Open a recipe website for more ideas

This project demonstrates GUI development, file handling, data structures (lists/dictionaries), randomization, and user-driven workflow design — great for showcasing early software development skills.

---

## ✨ Features

### ✅ User Input Prompts
- Enter your name  
- Set a weekly grocery budget  
- Choose diet type: **Low-carb**, **Low-sugar**, or **None**

### ✅ 7-Day Meal Plan Generator
- Breakfast, lunch, and dinner for 7 days  
- Cost per meal  
- Calories per meal  
- Total weekly cost & calories  
- Budget validation (tells you if you are over budget)

### ✅ Grocery List Generator
- Collects ingredients from all meals  
- Removes duplicates  
- Shows total item count  
- Displays the full grocery list in a scrollable window

### ✅ Healthy Snack Suggestions
- Randomly recommends a healthy snack when requested

### ✅ Favorite Meals
- Add a favorite meal  
- Saves to `favorite.txt` for future reference

### ✅ Meal Descriptions
- Reads detailed descriptions from `file1.txt`  
- Displays them in a **scrollable Tkinter popup window**

### ✅ External Recipe Website
- Optionally opens **mealime.com** (or another recipe site) for more ideas using the `webbrowser` module

---

## 🖼 Screenshots

Below are real screenshots from the app running on macOS:

> 💡 Tip: Replace each image name with the correct one if needed.

![User Name Input](./IMG_9202.jpeg)
![Budget Input](./IMG_9204.jpeg)
![Diet Preference](./IMG_9205.jpeg)
![Generated Weekly Meal Plan](./IMG_9208.jpeg)
![Grocery Item Count](./IMG_9209.jpeg)
![Grocery List](./IMG_9210.jpeg)
![Healthy Snack Suggestion](./IMG_9211.jpeg)
![Add Favorite Meal](./IMG_9212.jpeg)
![Favorite Confirmation](./IMG_9213.jpeg)
![Meal Description Window](./IMG_9214.jpeg)
![External Recipes Website](./IMG_9215.jpeg)
![Another Snack Suggestion](./IMG_9216.jpeg)
![Final Thank You Message](./IMG_9219.jpeg)

---

## 🧰 Technologies Used

- Python 3  
- Tkinter (GUI)  
- `random`  
- `datetime`  
- File I/O (reading/writing `.txt` files)  
- `webbrowser` module  

---

## 📁 Project Structure

```text
Meal-Planner-Grocery-Generator/
│── projectPhrase3nene.py   # Main Python script
│── file1.txt               # Meal descriptions
│── favorite.txt            # Saved favorite meals
│── README.md               # Documentation
│── IMG_9202.jpeg           # Screenshots (used in README)
│── IMG_9204.jpeg
│── IMG_9205.jpeg
│── ...


That alone will fix the messy paragraphs and actually show your screenshots inside the README.

---

## 3️⃣ Step 2 – Tidy how the repo itself looks

Right now all your JPEGs sit in the root. That’s fine functionally, but visually it looks messy for recruiters.

**Goal:** keep code clean at the top; tuck screenshots away.

### Steps

1. On the main repo page, click **“Add file → Create new file”**.
2. Name it `screenshots/.gitkeep` (this will create a folder called `screenshots`).
3. Go back to the file list.
4. For each `IMG_92xx.jpeg`:
   - Click the file → click **“…” → “Move”** (or “Edit” then change path depending on UI).
   - Change the path from `IMG_9202.jpeg` to `screenshots/IMG_9202.jpeg`.
   - Commit the move.
5. After moving them, update the image paths in README from  
   `![User Name Input](./IMG_9202.jpeg)`  
   to  
   `![User Name Input](./screenshots/IMG_9202.jpeg)`  
   then commit again.

Now your root will show just:

- `projectPhrase3nene.py`
- `file1.txt`
- `favorite.txt`
- `README.md`
- `screenshots/` folder

Much cleaner.

---

## 4️⃣ Step 3 – Improve repo “metadata”

On the right side of your repo page you have: **0 stars, 0 forks, Languages: Python 100%** etc. :contentReference[oaicite:4]{index=4}  

Do this:

1. At the top, under the repo name, click the **gear icon** (Settings) for description.
2. In “Description” put something more polished, e.g.:

   > “Tkinter-based weekly meal planner that calculates cost & calories and generates a grocery list (Python).”

3. In “Topics” add:
   - `python`
   - `tkinter`
   - `meal-planner`
   - `gui-application`
   - `beginner-project`
4. Optional: add a **LICENSE** (MIT). GitHub can auto-generate it under **Add file → Create new file → “LICENSE” → “Choose a license template”**.

This helps recruiters and search.

---

## 5️⃣ Step 4 – (Optional later) Rename / refactor main file

Not urgent, but nicer:

- Rename `projectPhrase3nene.py` → `meal_planner.py`.
- Update README “How to Run” to use:

  ```bash
  python3 meal_planner.py
