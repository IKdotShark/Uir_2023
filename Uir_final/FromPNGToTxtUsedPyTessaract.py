import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

img = cv2.imread("block_diagram.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#config = r'--oem 3 --psm 6'
with open("output.txt",'w') as file:
    file.write(pytesseract.image_to_string(img))
