import csv
import os

# Open the CSV file and read its contents into a dictionary
with open('rename2.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    csv_dict = {}
    for row in reader:
        csv_dict[row[1].split(',')[0].strip().lower()] = row[2]

# Loop through the files in the directory and rename them
for filename in os.listdir('.'):
    if filename.endswith('.jpg'):
        print(f"Processing file: {filename}")
        file_prefix = filename[:10].lower()
        match_found = False
        for key in csv_dict.keys():
            if file_prefix in key[:10]:
                new_filename = csv_dict[key] + '.jpg'
                if new_filename == filename:
                    match_found = True
                    break
                if os.path.isfile(new_filename):
                    print(f"Error: file '{new_filename}' already exists")
                    break
                print(f"Renaming file '{filename}' to '{new_filename}'")
                try:
                    os.rename(filename, new_filename)
                except FileNotFoundError:
                    print(f"File '{filename}' not found.")
                match_found = True
                break
        if not match_found:
            print(f"No matching entry in CSV for file '{filename}'")