import os

def read_values(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()
    blocks = content.split('__________________________')[-8:]
    return blocks

def write_values(output_file, values):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write('__________________________'.join(values))

def weekly():
    usr = os.getlogin()
    input_file = "report_" + usr + ".txt"
    output_file = "weekly_report_" + usr + ".txt"
    values = read_values(input_file)
    write_values(output_file, values)

weekly()



