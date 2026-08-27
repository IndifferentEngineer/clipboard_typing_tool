# 📋 Clipboard Typing Tool

A lightweight Windows utility built with Python that reads copied text and types it automatically into focused fields using simulated keyboard input. This is especially useful for repetitive data-entry tasks on websites, web portals, and desktop applications where standard clipboard pasting is disabled.

## 🚀 Features & Usage

*   **⚡ Auto-Typing:** Simulates real keystrokes to bypass restrictive forms.
*   **📝 Multiline Support:** Seamlessly types out block data (e.g., addresses or lists).
*   **⚙️ Customizable Speed:** Adjust `TYPE_INTERVAL` in the source code to fit application response times (e.g., `0.0` for max speed, `0.10` for slow).
*   **📦 Standalone Ready:** Easily packageable as a portable Windows executable.

**How to Use (Quick Start)**
1. Copy your text to the clipboard (e.g., *John Doe, 9123456780, john.doe@example.com, West Bengal*).
2. Click inside the specific input field where you want the text entered.
3. Press **F8** to begin the automated typing.
4. Press **Esc** to halt a typing operation instantly, or **Ctrl + Shift + X** to exit the background program entirely.

## 🛠️ Setup & Compilation

Ensure you have Python 3.x installed on your Windows machine. 

**Running from Source:**
```bash
# Install required packages
pip install pyautogui pyperclip keyboard

# Run the script
python clipboard_typing_tool.py
```

**Building a Standalone EXE:**
To share the tool or run it without Python installed, build it using PyInstaller. The output will be generated in the `dist/` folder as `NAPS_Typing_Tool.exe`.
```bash
python -m pip install pyinstaller
python -m PyInstaller --onefile --console --name NAPS_Typing_Tool clipboard_typing_tool.py
```

## ⚠️ Privacy & Important Notes

> **Privacy:** This tool processes clipboard content entirely locally on your machine. It does not require internet access or upload data. However, avoid copying sensitive information (like passwords) while the tool is running to prevent accidental automated entry.

*   Always ensure the correct input field is fully focused *before* pressing the start hotkey.
*   The application must remain running in the background for the global shortcuts to function.
*   The `pyautogui` library is primarily optimized for standard keyboard-compatible characters. 
*   **License:** MIT
