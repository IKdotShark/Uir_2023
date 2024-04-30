import pytesseract
from PIL import Image

# Specify the path to the Tesseract executable

# Open the image file
img = Image.open('more_test.png')

extracted_text = pytesseract.image_to_string(img)

# Путь к файлу для сохранения текста
output_file_path = 'test.txt'

# Сохранение извлеченного текста в файл
with open(output_file_path, 'w', encoding='utf-8') as f:
    f.write(extracted_text)

print("Текст успешно извлечен и сохранен в файл test.txt")