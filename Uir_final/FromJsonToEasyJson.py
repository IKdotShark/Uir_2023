import json

def extract_blocks(input_file, output_file):
    with open(input_file, "r") as f:
        data = json.load(f)

    blocks = data["blocks"]

    cleaned_blocks = []
    for block in blocks:
        cleaned_blocks.append(block["text"])

    cleaned_data = {"blocks": cleaned_blocks}

    with open(output_file, "w") as f:
        json.dump(cleaned_data, f, indent=4)


input_file = "data_copy.json"
output_file = "data_remake.json"
extract_blocks(input_file, output_file)
