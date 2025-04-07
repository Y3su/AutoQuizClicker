import pyautogui  # Library for controlling mouse and keyboard
import pytesseract  # OCR engine for text extraction from images
import time  # Provides sleep/delay functionality
import re  # For regular expression operations

def get_screen_text():
    # Take a screenshot of the screen
    screenshot = pyautogui.screenshot()
    # Extract text from the screenshot using Tesseract OCR (with layout config)
    text = pytesseract.image_to_string(screenshot, config="--psm 6")
    return text

def normalize_text(text):
    # Remove all whitespace and convert text to lowercase for comparison
    return re.sub(r"\s+", "", text).lower()

def find_text_coordinates(text):
    # Take a screenshot of the screen
    screenshot = pyautogui.screenshot()
    # Get detailed OCR data from the screenshot
    data = pytesseract.image_to_data(screenshot, output_type=pytesseract.Output.DICT)

    # Normalize the target text to match OCR output
    normalized_target = normalize_text(text)

    # Loop through all detected words on the screen
    for i in range(len(data["text"])):
        detected_text = normalize_text(data["text"][i])
        # Check if the target text is in the detected word
        if normalized_target in detected_text:
            x, y, w, h = data["left"][i], data["top"][i], data["width"][i], data["height"][i]
            # Return the center coordinates of the detected word
            return x + w // 2, y + h // 2

    # Return None if the text is not found
    return None

def find_and_click_text(text):
    # Find the coordinates of the specified text
    location = find_text_coordinates(text)
    if location:
        # Click on the found coordinates
        pyautogui.click(location)
        time.sleep(1)  # Short delay after clicking
        return True
    return False

def find_and_click_image(image, confidence=0.8):
    # Locate the center of the image on the screen with specified confidence
    location = pyautogui.locateCenterOnScreen(image, confidence=confidence)
    if location:
        # Click on the found image
        pyautogui.click(location)
        time.sleep(1)  # Short delay after clicking
        return True
    return False

def answer_three_questions():
    # List of correct answers to look for
    required_answers = ["DISTINCT", "?column?", "5"]
    answered_count = 0

    # Loop until all three correct answers are clicked
    while answered_count < 3:
        time.sleep(2)  # Wait before capturing screen
        question_text = get_screen_text()  # Capture and extract screen text
        print("Detected question:", question_text)

        # Loop through known answers and check if one appears in the question
        for answer in required_answers:
            if normalize_text(answer) in normalize_text(question_text):
                print(f"Clicking correct answer: {answer}")
                # Click the correct answer and update counters
                if find_and_click_text(answer):
                    answered_count += 1
                    required_answers.remove(answer)
                    break

        print("Clicking Check button...")
        find_and_click_image("check_button.png")  # Click the "Check" button

        time.sleep(2)
        print("Clicking Continue button...")
        find_and_click_image("continue_button.png")  # Click the "Continue" button

    print("All three questions answered!")

def main():
    # Infinite loop to continuously practice questions
    while True:
        answer_three_questions()  # Answer a batch of three questions

        time.sleep(2)
        print("Clicking Practice Again...")
        # Click the "Practice Again" button to restart the quiz
        if find_and_click_image("again_button.png"):
            print("Clicked Practice Again button. Restarting...")
        else:
            print("Practice Again button not found. Retrying...")
            time.sleep(2)

# Entry point of the script
if __name__ == "__main__":
    main()
