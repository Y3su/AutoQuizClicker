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