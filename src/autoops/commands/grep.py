import os


def grep_command(search_text, file_path):
    try:
        if os.path.getsize(file_path) == 0:
            print(f"⚠️ File is empty: {file_path}")
            return

        matches_found = False

        with open(file_path, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                if search_text.lower() in line.lower():
                    if not matches_found:
                        print("Found:")
                        matches_found = True

                    print(f"Line {line_number}: {line.strip()}")

        if not matches_found:
            print("No match found.")

    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
    except Exception as e:
        print(f"❌ An error occurred while reading the file: {e}")