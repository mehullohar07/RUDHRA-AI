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
    """Open a supported application or website and return a status message."""
    if app_name not in apps:
        return f"Application '{app_name}' not found."

    app = apps[app_name]

    if app.startswith(("http://", "https://")):
        try:
            opened = webbrowser.open(app)
            return (
                f"Opening {app_name.title()} in your browser."
                if opened
                else f"Could not open {app_name.title()} in your browser."
            )
        except OSError as error:
            return f"Could not open {app_name}: {error}"

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
                    return "Opening Chrome."
                except OSError as error:
                    return f"Could not open Chrome: {error}"

        try:
            opened = webbrowser.open("https://www.google.com")
            return (
                "Chrome installation not found. Opening your default browser."
                if opened
                else "Chrome was not found and the default browser could not be opened."
            )
        except OSError as error:
            return f"Chrome was not found. Could not open the default browser: {error}"

    try:
        subprocess.Popen(app)
        return f"Opening {app_name.title()}."
    except OSError as error:
        return f"Could not open {app_name}: {error}"
