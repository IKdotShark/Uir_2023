import re

# Open the output.py file and read the lines
with open('output.py', 'r') as file:
    lines = file.readlines()

# Initialize a list to hold the processed lines
processed_lines = []

# Process each line
for line in lines:
    line = line.strip()
    if line == 'start':
        continue
    elif line == 'end':
        continue
    elif line.startswith('input'):
        _, variables = line.split(' ', 1)
        variables = variables.split(',')
        for variable in variables:
            variable = variable.strip()
            line = f'{variable} = input()'
            processed_lines.append(line + '\n')
        continue
    elif line == 'flag = false':
        line = 'flag = False'
        processed_lines.append(line + '\n')
        continue
    elif line == 'flag = true':
        line = '    flag = True'
        processed_lines.append(line + '\n')
        continue
    elif line.startswith('for'):
        match = re.match(r'for (\w+) = (\d+) to (\w+)', line)
        if match:
            index, start, end = match.groups()
            line = f'for {index} in range(int({start}), int({end})):'
            processed_lines.append(line + '\n')
        continue
    elif line.endswith('++'):
        variable = line[:-2]
        line = f'    {variable} += 1'
        processed_lines.append(line + '\n')
        continue
    elif line.startswith('if'):
        line = line + ':'
        processed_lines.append(line + '\n')
        continue
    elif '=' in line:
        # Handle assignment statements
        if 'int(' in line and ')' in line:
            # Handle assignment statements with int conversion
            variable, value = map(str.strip, line.split('='))
            line = f'{variable} = {value}'
            processed_lines.append(line + '\n')
        else:
            variable, value = map(str.strip, line.split('='))
            line = f'{variable} = {value}'
            processed_lines.append(line + '\n')
        continue
    elif re.match(r'^\w+$', line):  # If the line is a single word
        line = f'print({line})'
        processed_lines.append(line + '\n')
        continue
    else:
        line = '    ' + line
        processed_lines.append(line + '\n')

# Write the processed lines to a new file named final.py
with open('final.py', 'w') as file:
    file.writelines(processed_lines)