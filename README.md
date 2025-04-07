# AutoQuizClicker 📸🤖

An automation script using Python, OCR, and image recognition to answer on-screen quiz questions and interact with UI buttons.

---

## 🧠 Description

This project automates answering multiple-choice questions on-screen using `pyautogui` and `pytesseract`. It captures the screen, recognizes the text using OCR, matches known answers, and simulates mouse clicks to select the correct answer. It then clicks "Check", "Continue", and "Practice Again" buttons using image recognition.

Useful for platforms where repetitive multiple-choice quizzes are involved (e.g., educational apps or web quizzes).

---

## 📦 Features

- 📸 Screenshot-based text detection via Tesseract OCR  
- 🧹 Text normalization for improved matching accuracy  
- 🖱️ Clicks correct answers automatically  
- 🔁 Handles "Check", "Continue", and "Practice Again" buttons via image recognition  
- ♾️ Runs in an infinite loop until manually stopped  

---

## 🛠️ Requirements

Install the required packages:

```bash
pip install pyautogui pytesseract
```

Also, make sure you have [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installed and properly configured in your system's PATH.

---

## 🧪 How It Works

1. **Detects** on-screen text using `pyautogui` screenshots + `pytesseract` OCR.
2. **Matches** predefined correct answers (`DISTINCT`, `?column?`, `5`) from the question text.
3. **Clicks** the correct answer using coordinates.
4. **Navigates** using image recognition for:
   - ✅ "Check"
   - 🔁 "Continue"
   - 🔄 "Practice Again"

---

## 🧩 File Assets

Make sure to include the following image assets in the same folder:

- `check_button.png`
- `continue_button.png`
- `again_button.png`

These are used for UI navigation with `pyautogui.locateCenterOnScreen()`.

---

## ▶️ Running the Script

```bash
python your_script_name.py
```

Once running, the script will:
- Attempt to solve 3 questions
- Click "Check", then "Continue"
- Repeat the process by clicking "Practice Again"

---

## 🚨 Disclaimer

This script is for educational and experimental use only. Make sure you're allowed to automate interactions on the platform you're using it with.

---

## 📸 Preview (Optional)

Add a GIF or screenshot of it in action here!

---

## 📄 License

MIT License
---

## 🔍 Code Walkthrough

### 1. `get_screen_text()`
- Takes a screenshot of the screen.
- Uses Tesseract OCR to extract text with better layout segmentation (`--psm 6`).

### 2. `normalize_text(text)`
- Removes extra spaces and converts text to lowercase for easier comparison.

### 3. `find_text_coordinates(text)`
- Searches for the given text in the screenshot using OCR data output.
- Returns coordinates of the center of the text for clicking.

### 4. `find_and_click_text(text)`
- Finds the coordinates of the given text and clicks it using PyAutoGUI.

### 5. `find_and_click_image(image, confidence=0.8)`
- Looks for an image (e.g., a button) on screen with given confidence.
- If found, clicks the center of the image.

### 6. `answer_three_questions()`
- Loops through and answers three questions using a list of known correct answers (`DISTINCT`, `?column?`, `5`).
- Uses text matching and button clicking to proceed through the quiz interface.

### 7. `main()`
- Main infinite loop to keep practicing questions.
- After answering 3, it clicks "Practice Again" to restart.

---
