# Voice Assistant with GUI

This project is a voice-activated assistant with a graphical user interface (GUI) built using Python. The assistant can handle information retrieval and video playing requests using speech recognition and text-to-speech capabilities.

## Features

- **Voice Interaction**: The assistant listens to user commands and responds with voice output.
- **Information Retrieval**: The assistant can search for information online and provide results.
- **Video Playback**: The assistant can search for and play videos on YouTube.
- **Graphical User Interface (GUI)**: A simple GUI allows the user to interact with the assistant using buttons.

## Technologies Used

- **Python**: Core programming language.
- **Django**: Web framework used for creating a robust back-end.
- **pyttsx3**: Text-to-Speech conversion library in Python.
- **SpeechRecognition**: Library for performing speech recognition, with support for several engines and APIs.
- **tkinter**: Standard GUI library for Python.
- **Selenium**: WebDriver for automating web applications for testing purposes.
- **WebDriver Manager**: For managing browser drivers (ChromeDriver in this case).

## Installation

### Prerequisites

Ensure you have Python and pip installed. You can download Python from [python.org](https://www.python.org/).

### Clone the Repository

```bash
git clone https://github.com/Riya-2603/voice-assistant-gui.git
cd voice-assistant-gui
```

### Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Requirement.txt list 

```bash
pyttsx3==2.90
SpeechRecognition==3.8.1
tk==0.1.0
selenium==4.4.0
webdriver-manager==3.5.2
```

### Running the Voice Assistant

Run the main script directly:

```bash
python main.py
```

## Project Structure

- **main.py**: Entry point for the voice assistant functionality.
- **selenium_web.py**: Contains the `InfoScraper` class for web scraping.
- **YT_auto.py**: Contains the `YouTubePlayer` class for playing YouTube videos.
- **index.py**: Contains the `VoiceAssistant` class for the GUI.
- **requirements.txt**: Lists the dependencies required for the project.

## Usage

1. **Run the Assistant**: Execute `main.py` to start the voice assistant.
2. **Interact via GUI**: Use the GUI to press the button and speak your command.

## Example Commands

- **Information Requests**: "I need information about Python programming."
- **Video Requests**: "Play a video of cute cats."

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests for any features, improvements, or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements

- The developers and contributors of `pyttsx3`, `SpeechRecognition`, `tkinter` and `Selenium`.
