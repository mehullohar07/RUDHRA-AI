from modules.apps import open_app
from modules.llm import get_ai_response
from modules import utility
from core.assistant import ASSISTANT_NAME


COMMANDS = {
    "hello": utility.greet,
    "creator": utility.creator,
    "who are you?": utility.who_are_you,
    "current time": utility.current_time,
    "current date": utility.current_date,
    "help": utility.help_menu,
    "version": utility.version,
}

APP_COMMANDS = {
    "open chrome": "chrome",
    "open paint": "paint",
    "open calculator": "calculator",
    "open vscode": "vscode",
    "open notepad": "notepad",
    "open instagram": "instagram",
    "open youtube": "youtube",
}


def process_command(command):
    """Process a request and return data without printing or speaking it.

    The returned dictionary is shared by CLI, GUI, and future interfaces.
    """
    normalized_command = command.strip().lower()

    if not normalized_command:
        return {
            "text": "Please enter a command.",
            "should_exit": False,
            "source": "system",
            "speak": False,
        }

    if normalized_command in ("bye", "exit", "quit"):
        return {
            "text": utility.goodbye(),
            "should_exit": True,
            "source": "command",
            "speak": True,
        }

    if normalized_command in COMMANDS:
        return {
            "text": COMMANDS[normalized_command](),
            "should_exit": False,
            "source": "command",
            "speak": True,
        }

    if normalized_command in APP_COMMANDS:
        return {
            "text": open_app(APP_COMMANDS[normalized_command]),
            "should_exit": False,
            "source": "command",
            "speak": False,
        }

    response = get_ai_response(command.strip())
    return {
        "text": response or "No response received from the AI service.",
        "should_exit": False,
        "source": "ai",
        "speak": True,
    }


def execute_command(command):
    """Legacy CLI adapter; new interfaces should call process_command()."""
    result = process_command(command)
    print(f"\n{ASSISTANT_NAME}: {result['text']}\n")

    if result["speak"]:
        from modules.voice import speak

        speak(result["text"])

    return "exit" if result["should_exit"] else None
