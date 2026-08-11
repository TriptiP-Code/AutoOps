import os


def find_command(search):

    found = False

    for root, dirs, files in os.walk("."):

        for file in files:

            if search.lower() in file.lower():

                print(os.path.join(root, file))

                found = True

    if not found:
        print("No matching files found.")