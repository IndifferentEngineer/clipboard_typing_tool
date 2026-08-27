import pyautogui
import pyperclip
import keyboard
import time
import threading


# ============================================================
# SETTINGS
# ============================================================

# Shortcut to start typing clipboard
HOTKEY = "f8"

# Delay between characters
# 0.0 = maximum speed
# 0.02 = very fast
# 0.05 = normal
TYPE_INTERVAL = 0.02

# Stop key
STOP_KEY = "esc"


# ============================================================
# PROGRAM STATE
# ============================================================

typing_now = False
stop_requested = False

lock = threading.Lock()


# ============================================================
# TYPE CLIPBOARD
# ============================================================

def type_clipboard():

    global typing_now
    global stop_requested

    # Prevent starting twice
    with lock:

        if typing_now:
            print("Already typing...")
            return

        typing_now = True
        stop_requested = False

    try:

        # ----------------------------------------------------
        # Read current clipboard
        # ----------------------------------------------------

        text = pyperclip.paste()

        if not text:

            print("Clipboard is empty.")
            return

        # ----------------------------------------------------
        # Show clipboard content
        # ----------------------------------------------------

        print()
        print("=" * 60)
        print("CLIPBOARD")
        print("=" * 60)
        print(text)
        print("=" * 60)

        print("Typing started...")
        print("Press ESC to stop.")

        # ----------------------------------------------------
        # Give F8 time to release
        # ----------------------------------------------------

        time.sleep(0.15)

        # ----------------------------------------------------
        # Type text
        # ----------------------------------------------------

        # Split into lines so that ENTER works correctly.
        lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")

        for line_number, line in enumerate(lines):

            # Check STOP
            with lock:

                if stop_requested:

                    print()
                    print("Typing stopped.")

                    return

            # Type current line
            if line:

                pyautogui.write(
                    line,
                    interval=TYPE_INTERVAL
                )

            # Press ENTER between lines
            if line_number < len(lines) - 1:

                pyautogui.press("enter")

            # Small check between lines
            time.sleep(0.01)

        print()
        print("Typing completed.")

    except Exception as e:

        print()
        print("ERROR:")
        print(e)

    finally:

        with lock:

            typing_now = False
            stop_requested = False


# ============================================================
# START BUTTON / F8
# ============================================================

def start_typing():

    # Run typing in another thread so the hotkey listener
    # remains responsive.
    thread = threading.Thread(
        target=type_clipboard,
        daemon=True
    )

    thread.start()


# ============================================================
# STOP TYPING
# ============================================================

def stop_typing():

    global stop_requested

    with lock:

        if typing_now:

            stop_requested = True

            print()
            print("STOP requested...")


# ============================================================
# EXIT PROGRAM
# ============================================================

def exit_program():

    print()
    print("Closing program...")

    keyboard.unhook_all()

    raise SystemExit


# ============================================================
# MAIN
# ============================================================

def main():

    print()
    print("=" * 60)
    print("       CLIPBOARD → NAPS TYPING TOOL")
    print("=" * 60)
    print()

    print("HOW TO USE:")
    print()
    print("1. Copy text normally:")
    print("       Ctrl + C")
    print()
    print("2. Click inside the input field.")
    print()
    print("3. Press:")
    print("       F8")
    print()
    print("4. To stop typing:")
    print("       ESC")
    print()
    print("5. To exit the program:")
    print("       Ctrl + Shift + X")
    print()
    print("=" * 60)
    print()

    # F8 = start
    keyboard.add_hotkey(
        "f8",
        start_typing,
        suppress=False
    )

    # ESC = stop
    keyboard.add_hotkey(
        "esc",
        stop_typing,
        suppress=False
    )

    # Ctrl + Shift + X = exit
    keyboard.add_hotkey(
        "ctrl+shift+x",
        exit_program,
        suppress=False
    )

    print("PROGRAM READY")
    print()
    print("F8 = TYPE CLIPBOARD")
    print("ESC = STOP")
    print("CTRL + SHIFT + X = EXIT")
    print()

    # Keep program running
    keyboard.wait()


# ============================================================
# START
# ============================================================

if __name__ == "__main__":

    try:
        main()

    except KeyboardInterrupt:

        print()
        print("Program stopped.")

    except SystemExit:

        pass
