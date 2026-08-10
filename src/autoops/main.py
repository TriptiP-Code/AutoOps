import sys


def start_application():
    print("===================================")
    print("🚀 Starting AutoOps...")
    print("===================================")

def hello_command():
    print("👋 Welcome to AutoOps!")


def version_command():
    print("AutoOps v0.1.0")


def help_command():
    print("Available commands:")
    print("  hello")
    print("  version")
    print("  help")

start_application()


if len(sys.argv) > 1: 
  command=sys.argv[1]
  
  if command == "hello":
    hello_command()

  elif command == "version":
    version_command()

  elif command == "help":
    help_command()

  else:
    print(f"❌ Unknown command: {command}")


else: 
  print(" No command provided")
  print("try: python main.py hello")