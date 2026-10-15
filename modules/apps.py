import os
import subprocess
import webbrowser

apps = {
    "chrome": "chrome.exe",
    "notepad": "notepad.exe",
    "paint": "mspaint.exe",
    "vscode": "Code.exe",
    "calculator": "calc.exe",
    "instagram": "https://www.instagram.com",
    "youtube": "https://www.youtube.com",
}


def open_app(app_name):
    if app_name not in apps:
        print(f"Application '{app_name}' not found.")
        return

    app = apps[app_name]

    if app.startswith(("http://", "https://")):
        webbrowser.open(app)
        return

    if app_name == "chrome":
        chrome_paths = [
            os.path.expandvars(
                r"%ProgramFiles%\Google\Chrome\Application\chrome.exe"
            ),
            os.path.expandvars(
                r"%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe"
            ),
            os.path.expandvars(
                r"%LocalAppData%\Google\Chrome\Application\chrome.exe"
            ),
        ]

        for chrome_path in chrome_paths:
            if os.path.isfile(chrome_path):
                try:
                    subprocess.Popen([chrome_path])
                    return
                except OSError as error:
                    print(f"Could not open Chrome: {error}")
                    return

        print("Chrome installation not found. Opening default browser...")
        webbrowser.open("https://www.google.com")
        return

    try:
        subprocess.Popen(app)
    except OSError as error:
        print(f"Could not open {app_name}: {error}")