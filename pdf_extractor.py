import pdfplumber
import pytesseract
from PIL import Image

# Set the Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text.strip()

# Test the function
if __name__ == "__main__":
    pdf_path = "samplepdf.pdf"  # Replace with your PDF file
    text = extract_text_from_pdf(pdf_path)
    print(text)


import pytesseract

# Set the path to tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

print("Tesseract Path Set Successfully")
