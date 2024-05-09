import json
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import networkx as nx
from Module_user_file import choose_file
import tkinter as tk
from tkinter import messagebox

file_path = choose_file()

if not file_path.endswith('.json'):
    tk.Tk().withdraw()  # скрываем основное окно
    messagebox.showerror("Ошибка", "Выбранный файл не является файлом JSON.")
    exit()

# Load the JSON data
if file_path is None:
    exit()

with open(file_path) as f:
    data = json.load(f)

# Find the maximum y-coordinate
max_y = max(block['y'] + block['height'] for block in data['blocks'])

# Create a new plot
fig, ax = plt.subplots()

# Create a directed graph for the arrows
G = nx.DiGraph()

# Add the blocks to the plot
for block in data['blocks']:
    # Subtract the y-coordinate from max_y to flip the diagram
    y = max_y - block['y'] - block['height']
    rect = patches.Rectangle((block['x'], y), block['width'], block['height'], linewidth=1, edgecolor='r', facecolor='none')
    ax.add_patch(rect)
    plt.text(block['x'] + block['width'] / 2, y + block['height'] / 2, block['text'], ha='center', va='center')

# Add the arrows to the graph
for arrow in data['arrows']:
    G.add_edge(arrow['startIndex'], arrow['endIndex'])

# Draw the arrows
pos = {i: (block['x'] + block['width'] / 2, max_y - block['y'] - block['height'] / 2) for i, block in enumerate(data['blocks'])}
nx.draw(G, pos, ax=ax, arrows=True)

plt.savefig('block_diagram.png', format='png', dpi=300)
# Show the plot
plt.show()
