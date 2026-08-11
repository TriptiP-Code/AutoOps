import os


def files_command(path):

    print(f"===== Files in {path} =====")

    # files = os.listdir() this will also work , if nothing is inside listdir then it will print the current working directory , i.e from where u ran the command

    files = os.listdir(path) # this will take the path mentioned by user

    for file in files:
        print(file)