import sys
import os
from PIL import Image
from pytesseract import pytesseract

output = os.path.abspath(os.path.dirname(__file__)) + "\\output.txt"

sys.stdout = open(output, "w", encoding='utf-8')

# Define path to tesseract.exe
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Define path ot the image
path_to_image = os.path.abspath(
    os.path.dirname(__file__)) + "\\images\\hindiText.png"

# Point tesseract_cmd to tesseract.exe
pytesseract.tesseract_cmd = path_to_tesseract

# open the image with PIL
img = Image.open(path_to_image)

# Extract text from image
text = pytesseract.image_to_string(image=img, lang='hin')

print(text)
