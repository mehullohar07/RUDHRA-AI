# RUDHRA AI

A Python-based personal desktop assistant and the next evolution of Ashwatthama AI. This milestone updates the project identity while preserving the existing command-line assistant, Tkinter chat GUI, Groq responses, and voice/utility modules.

**Current version:** `v0.5` (identity migration milestone)

## Existing features

- AI-powered conversational responses using the Groq API
- Command-line text and voice interaction
- Tkinter desktop chat interface
- Speech recognition and text-to-speech for supported commands
- Launch supported Windows applications and open supported websites
- Date, time, help, creator, and version commands
- Modular Python project structure

> The multi-agent planner, specialist agents, and execution verification are planned work, not implemented features yet.

## Tech stack

- Python 3
- Groq API (`openai/gpt-oss-20b`)
- Tkinter GUI (included with most standard Python installations)
- `python-dotenv`, `SpeechRecognition`, `PyAudio`, and `pyttsx3`

## Project structure

```text
RUDHRA-AI/
├── core/
│   ├── assistant.py
│   └── command_handler.py
├── gui/
│   ├── __init__.py
│   └── app.py
├── modules/
│   ├── apps.py
│   ├── llm.py
│   ├── system.py
│   ├── utility.py
│   └── voice.py
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Setup

Use Python 3.10 or newer. Some desktop and microphone commands are designed for Windows.

1. Open the project folder in VS Code and open its terminal.
2. Create and activate a virtual environment if desired.
3. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Copy `.env.example` to `.env` and set `GROQ_API_KEY` in your local `.env` file. Never paste your key into chat or commit `.env` to GitHub.

## Run the assistant

### Desktop GUI

```bash
python -m gui.app
```

### Command-line interface

```bash
python main.py
```

The CLI asks you to select text or voice mode. Voice mode requires a working microphone and the relevant audio dependencies. AI responses require internet access and a valid Groq API key.

## Quick checks

Compile the Python files without launching the GUI or microphone:

```bash
python -m compileall -q core gui modules main.py
```

Then run the GUI and CLI separately and test basic commands such as `help`, `version`, `current time`, and a simple AI question. Application launching depends on the local computer and installed applications.

## Version history

### v0.5 - RUDHRA AI foundation

- Updated the assistant identity and version in the CLI, GUI, LLM system prompt, and version command.
- Documented both GUI and CLI startup paths.
- Preserved existing features while preparing for a future modular agent architecture.

### Earlier Ashwatthama AI milestones

- v0.4: Groq API responses and text/voice CLI interaction.
- v0.3.1: Speech recognition and runtime dependency updates.
- v0.3: Text-to-speech and consolidated command handling.
- v0.2: Modular `core/` and `modules/` structure.
- v0.1: Initial command-line assistant.

## Roadmap

1. RUDHRA main agent and structured task routing.
2. VAJRA: controlled PC automation.
3. GARUDA: web research; MANI: file operations with confirmation for destructive actions.
4. MEDHA: knowledge tasks; NETRA: verification of important outcomes.
5. NAAD: voice integration with the assistant workflow.
6. Logging, tests, UI polish, and documentation.

Roadmap items are planned and should not be treated as existing features.

## Author

**Mehul Lohar** · [GitHub](https://github.com/mehullohar07)
