import pytesseract
import cv2
from Module_user_file import choose_file
import tkinter as tk
from tkinter import messagebox

file_path = choose_file()

if not file_path.endswith('.png'):
    tk.Tk().withdraw()  # скрываем основное окно
    messagebox.showerror("Ошибка", "Выбранный файл не является файлом PNG.")
    exit()

# Load the JSON data
if file_path is None:
    exit()

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

img = cv2.imread(file_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# config = r'--oem 3 --psm 6'
with open("output.txt", 'w') as file:
    file.write(pytesseract.image_to_string(img))
