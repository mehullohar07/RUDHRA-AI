from datetime import datetime

from core.assistant import ASSISTANT_NAME, VERSION
from modules.voice import speak

def greet():
    text = "Namaste! How can I assist you today?"
    print(text)
    speak(text)

def goodbye():
    text = "Goodbye! have a productive day ahead!"
    print(text)
    speak(text)

def current_time():
    text = "Current Time: " + datetime.now().strftime("%H:%M:%S")
    print(text)
    speak(text)

def current_date():
    text = "Current Date: " + datetime.now().strftime("%d/%m/%Y")
    print(text)
    speak(text)

def creator():
    text = "My creator is Mehul."
    print(text)
    speak(text)

def who_are_you():
    text = "I am RUDHRA, your AI assistant."
    print(text)
    speak(text)

def version():
    text = f"{ASSISTANT_NAME} Version: {VERSION}"
    print(text)
    speak(text)

def help_menu():
    help_text = """
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
    """
    print(help_text)
    speak(help_text)