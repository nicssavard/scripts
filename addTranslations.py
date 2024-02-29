import sys

path = "/home/kali/jmap/jmapcloud-portal/src/resources/json/translations/"


def insert_text(line_num, string_name, text_en, text_fr, text_es):
    # files = ["./en.json", "./fr.json", "./scripts/es.json"]
    files = [f"{path}en.json", f"{path}fr.json", f"{path}es.json"]
    text = [f'  "{string_name}": "{text_en}",',
            f'  "{string_name}": "{text_fr}",',
            f'  "{string_name}": "{text_es}",']

    for index, file in enumerate(files):
        try:
            print(f"Inserting text in {file}...")
            with open(file, 'r') as f:
                lines = f.readlines()

            if line_num > len(lines):
                print(f"Error: The file only has {len(lines)} lines.")
                return

            # Insert a new line and the text
            lines.insert(line_num - 1, '\n')
            lines.insert(line_num - 1, text[index])

            with open(file, 'w') as f:
                f.writelines(lines)
            print(f"Text inserted successfully in {file}.")

        except FileNotFoundError:
            print(f"Error: {file} not found.")
        except Exception as e:
            print(f"An error occurred: {e}")


if len(sys.argv) != 6:
    print("Usage: python insert_text.py lineNumber 'stringToInsert' fileName")
else:
    _, line_num, string_name, text_en, text_fr, text_es = sys.argv
    insert_text(int(line_num), string_name, text_en, text_fr, text_es)
