import tkinter as tk
import webbrowser
import subprocess
import tkinter.messagebox as messagebox

def open_block_diagram_editor():
    webbrowser.open("https://programforyou.ru/block-diagram-redactor")

def convert_json_to_python():
    subprocess.run(["python", "FromJsonToEasyJson.py"])
    subprocess.run(["python", "Sorted_To_Simple_unworkable_code.py"])
    subprocess.run(["python", "FinalCodeCreator.py"])

def convert_python_to_block_diagram():
    subprocess.run(["python", "Converter.py"])

def convert_json_to_img():
    subprocess.run(["python", "FromJsonToImage.py"])

def convert_img_to_code():
    messagebox.showwarning("Предупреждение", "Конвертация из фото в код работает некорректно")

def exit_program():
    root.destroy()

root = tk.Tk()
root.title("Convert")

btn1 = tk.Button(root, text="Сделать блок схему", command=open_block_diagram_editor)
btn1.pack(pady=10)

btn2 = tk.Button(root, text="Блоксхема JSON -> Код python", command=convert_json_to_python)
btn2.pack(pady=10)

btn3 = tk.Button(root, text="Код python -> Блоксхема", command=convert_python_to_block_diagram)
btn3.pack(pady=10)

btn4 = tk.Button(root, text="Конвертировать JSON в изображение", command=convert_json_to_img)
btn4.pack(pady=10)

btn5 = tk.Button(root, text="Изображение в код", command=convert_img_to_code)
btn5.pack(pady=10)

btn6 = tk.Button(root, text="Выход", command=exit_program)
btn6.pack(pady=10)

root.mainloop()
