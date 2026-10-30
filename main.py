from core.command_handler import process_command
from core.assistant import banner, ASSISTANT_NAME
from modules.voice import take_command, speak


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
            command = input("You: ").strip()
        else:
            command = take_command()

        if not command:
            continue

        result = process_command(command)
        print(f"\n{ASSISTANT_NAME}: {result['text']}\n")

        if result["speak"]:
            speak(result["text"])

        if result["should_exit"]:
            break


if __name__ == "__main__":
    main()
