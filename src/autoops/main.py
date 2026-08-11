import sys

from commands.hello import hello_command
from commands.version import version_command
from commands.help import help_command
from commands.system import system_command
from commands.files import files_command
from commands.read import read_command


def start_application():
    print("===================================")
    print("🚀 Starting AutoOps...")
    print("===================================")


start_application()


if len(sys.argv) > 1: 
  command=sys.argv[1]
  
  if command == "hello":
    hello_command()

  elif command == "version":
    version_command()

  elif command == "help":
    help_command()
  
  elif command == "system":
    system_command()
  
  elif command == "read":

    if len(sys.argv) > 2:
        read_command(sys.argv[2])

    else:
        print("Usage: python main.py read <filename>")

  elif command == "files":

    if len(sys.argv) > 2:
        path = sys.argv[2]
        files_command(path)

    else:
        files_command(".")

  else:
    print(f"❌ Unknown command: {command}")


else: 
  print(" No command provided")
  print("try: python main.py hello")