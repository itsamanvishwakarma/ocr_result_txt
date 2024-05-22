import json
import os

def json_to_text(json_path, text_file_path):
    with open(json_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    with open(text_file_path, 'w', encoding='utf-8') as text_file:
        for file_name, pages in data.items():
            text_file.write(f"File: {file_name}\n")
            for page in pages:
                text_file.write(f"\nPage: {page['page']}\n")
                for line in page['text_lines']:
                    text_file.write(f"{line['text']}\n")
                text_file.write("\n" + "-"*50 + "\n")

# Define the path to your JSON file and the desired text output file
json_path = 'results/surya/samplefile/results.json'
text_file_path = 'ocr_output.txt'

# Convert JSON to text file
json_to_text(json_path, text_file_path)
