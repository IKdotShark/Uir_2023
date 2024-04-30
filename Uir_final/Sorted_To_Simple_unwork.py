import json
import numpy as np

# Open and read the sorted_blocks.json file
with open('sorted_blocks.json', 'r') as file:
    blocks = json.load(file)

# Calculate the average 'x' coordinate of all blocks
average_x = np.mean([block['x'] for block in blocks])

# Threshold for the 'x' coordinate to decide whether to add a tab or not
x_threshold = average_x + 50  # Update this value based on your requirements

# Extract the text from each block and add a tab if 'x' coordinate is significantly different from the average
texts = ['\t' + block['text'] if block['x'] > x_threshold else block['text'] for block in blocks]

# Reverse the order of the texts
texts.reverse()

# Join the texts with a newline in between to form the Python code
code = '\n'.join(texts)

# Write the Python code into a new Python file
with open('output.py', 'w') as file:
    file.write(code)