def read_command(path):

    try:
        with open(path, "r") as file:

            content = file.read()

            print(content)

    except FileNotFoundError:
        print(f"❌ File not found: {path}")