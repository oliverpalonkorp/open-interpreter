import threading
from pynput import keyboard


class HotkeyHandler:
    def __init__(self, key_combination):
        self.key_combination = key_combination
        self.current_keys = set()

        self.listener_thread = threading.Thread(target=self.start_key_listener)
        self.listener_thread.daemon = True  # This makes the thread terminate when the main program exits

    def on_press(self, key):
        if key in self.key_combination:
            self.current_keys.add(key)
            if all(k in self.current_keys for k in self.key_combination):
                print('Hotkey activated!')

    def on_release(self, key):
        try:
            self.current_keys.remove(key)
        except KeyError:
            pass

    def start_key_listener(self):
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

    def start(self):
        # Start the listener thread in the background
        self.listener_thread.start()