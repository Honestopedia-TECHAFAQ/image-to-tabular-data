import cv2
import pytesseract
import re
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image

def extract_text_from_image(image_path):
    preprocessed_image = preprocess_image(image_path)
    extracted_text = pytesseract.image_to_string(preprocessed_image)

    return extracted_text.strip()

def extract_numerical_values(text):
    numerical_values = re.findall(r'\d+', text)
    numerical_values = [int(value) for value in numerical_values]

    return numerical_values

def extract_data_structure(text):
    date_match = re.search(r'\d{2}/\w{3}/\d{4}', text)
    date = date_match.group() if date_match else None
    data_structure = {
        "date": date,
    }

    return data_structure

def main():
    image_path = 'path/to/your/image.jpg'
    extracted_text = extract_text_from_image(image_path)
    numerical_values = extract_numerical_values(extracted_text)
    data_structure = extract_data_structure(extracted_text)
    print("Extracted Text:")
    print(extracted_text)
    print("\nNumerical Values:")
    print(numerical_values)
    print("\nData Structure:")
    print(data_structure)

if __name__ == "__main__":
    main()
