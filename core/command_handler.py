from modules.apps import *
from modules.utility import *
from modules.llm import get_ai_response
from modules.voice import speak
from core.assistant import ASSISTANT_NAME

def execute_command(command):
    command = command.strip().lower()

    if command == "hello":
        greet()

    elif command == "creator":
        creator()

    elif command == "who are you?":
        who_are_you()

    elif command == "current time":
        current_time()

    elif command == "current date":
        current_date()

    elif command == "open chrome":
        open_app("chrome")

    elif command == "help":
        help_menu()

    elif command == "open paint":
        open_app("paint")

    elif command == "open calculator":
        open_app("calculator")

    elif command == "open vscode":
        open_app("vscode")

    elif command == "open notepad":
        open_app("notepad")

    elif command == "open instagram":
        open_app("instagram")

    elif command == "open youtube":
        open_app("youtube")

    elif command == "version":
        version()

    elif command in ("bye", "exit", "quit"):
        goodbye()
        return "exit"

    else:
        print(f"\n{ASSISTANT_NAME} is thinking...")
        response = get_ai_response(command)
        print(f"\n{ASSISTANT_NAME}: {response}\n")
        speak(response)

    return None