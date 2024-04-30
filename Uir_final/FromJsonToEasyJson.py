import json

# Open and read the data.json file
with open('data.json', 'r') as file:
    data = json.load(file)

# Extract the blocks with text from the parsed data
blocks_with_text = [block for block in data['blocks'] if 'text' in block and block['text']]

# Sort the blocks by the 'y' coordinate in descending order
sorted_blocks = sorted(blocks_with_text, key=lambda block: -block['y'])

# Write the sorted blocks into a new JSON file
with open('sorted_blocks.json', 'w') as file:
    json.dump(sorted_blocks, file)