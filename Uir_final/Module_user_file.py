import tkinter as tk
from tkinter import filedialog

def choose_file():
    root = tk.Tk()
    root.withdraw()  # скрыть основное окно

    file_path = filedialog.askopenfilename()  # открываем диалог выбора файла
    return file_path
