from datetime import datetime

from core.assistant import ASSISTANT_NAME, VERSION


def greet():
    return "Namaste! How can I assist you today?"


def goodbye():
    return "Goodbye! Have a productive day ahead!"


def current_time():
    return "Current Time: " + datetime.now().strftime("%H:%M:%S")


def current_date():
    return "Current Date: " + datetime.now().strftime("%d/%m/%Y")


def creator():
    return "My creator is Mehul."


def who_are_you():
    return "I am RUDHRA, your AI assistant."


def version():
    return f"{ASSISTANT_NAME} Version: {VERSION}"


def help_menu():
    return """
    =========================
            HELP MENU
    =========================

    APPLICATIONS
    ------------
    1. Open Chrome
    2. Open Paint
    3. Open VS Code
    4. Open Notepad
    5. Open Calculator
    6. Open Instagram
    7. Open YouTube

    UTILITY COMMANDS
    ----------------
    8. Current Time
    9. Current Date

    SYSTEM COMMANDS
    ---------------
    10. Hello
    11. creator
    12. Who are you?
    13. Help
    14. Version
    15. Exit
    """.strip()
