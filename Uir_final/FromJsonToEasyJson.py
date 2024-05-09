import json
from Module_user_file import choose_file
import tkinter as tk
from tkinter import messagebox

def simplification():
    file_path = choose_file()

    if not file_path.endswith('.json'):
        tk.Tk().withdraw()  # скрываем основное окно
        messagebox.showerror("Ошибка", "Выбранный файл не является файлом JSON.")
        exit()

    # Load the JSON data
    if file_path is None:
        exit()

    with open(file_path, 'r') as file:
        data = json.load(file)
    blocks_with_text = [block for block in data['blocks'] if 'text' in block and block['text']]
    sorted_blocks = sorted(blocks_with_text, key=lambda block: -block['y'])
    with open('sorted_blocks.json', 'w') as file:
        json.dump(sorted_blocks, file)