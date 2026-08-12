import sys

from commands.hello import hello_command
from commands.version import version_command
from commands.help import help_command
from commands.system import system_command
from commands.files import files_command
from commands.read import read_command
from commands.find import find_command
from commands.grep import grep_command
from commands.run import run_command
from commands.docker_cmd import docker_ps


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

  elif len(sys.argv) >= 4 and sys.argv[1] == "grep":
    query = sys.argv[2]
    path = sys.argv[3]
    grep_command(query, path)

  elif command == "docker":

    docker_ps()

  elif command == "run":

    if len(sys.argv) > 2:

        cmd = " ".join(sys.argv[2:])

        run_command(cmd)

    else:
        print("Usage: python main.py run <command>")

  elif command == "find":

    if len(sys.argv) > 2:
        find_command(sys.argv[2])

    else:
        print("Usage: python main.py find <text>")
  
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