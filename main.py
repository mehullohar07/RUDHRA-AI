from core.command_handler import execute_command
from core.assistant import banner
from modules.voice import take_command
from core.assistant import ASSISTANT_NAME

def main():
    banner()

    print("Choose your input mode:")
    print("1. Text Mode")
    print("2. Voice Mode")

    while True:
        mode = input("Enter 1 or 2: ").strip()
        if mode == "1":
            mode = "text"
            break
        elif mode == "2":
            mode = "voice"
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    print(f"\n{ASSISTANT_NAME} started in {mode.upper()} mode.")
    print("Type 'exit' to quit.\n")

    while True:
        if mode == "text":
            command = input("You: ").strip().lower()
        else:
            command = take_command()

        if not command:
            continue

        result = execute_command(command)

        if result == "exit":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()