import subprocess


def run_command(command):

    try:

        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print(result.stdout)

        else:
            print("❌ Command Failed")
            print(result.stderr)

    except Exception as e:
        print(f"Error : {e}")