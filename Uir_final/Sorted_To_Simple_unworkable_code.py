import json

# Open and read the sorted_blocks.json file
with open('sorted_blocks.json', 'r') as file:
    blocks = json.load(file)

# Extract the text from each block
texts = [block['text'] for block in blocks]

# Reverse the order of the texts
texts.reverse()

# Join the texts with a newline in between to form the Python code
code = '\n'.join(texts)

# Write the Python code into a new Python file
with open('output.py', 'w') as file:
    file.write(code)