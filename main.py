import tkinter as tk
from tkinter import ttk, messagebox
import keyboard
import pyautogui
from threading import Thread
import time

class MousePositionManager:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("MouseMan")
        self.root.geometry("400x400")
        self.root.resizable(False, False)
        
        # Settings
        self.save_position_shortcut = 'ctrl+alt+s'
        self.move_to_position_shortcut = 'ctrl+alt+d'
        self.saved_position = {'x': 0, 'y': 0}
        self.is_recording = False
        self.setup_ui()
        self.register_hotkeys()

    def setup_ui(self):
        # Style configuration
        style = ttk.Style()
        style.configure('TButton', padding=5)
        style.configure('TLabel', padding=5)
        
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Shortcuts section
        ttk.Label(main_frame, text="Keyboard Shortcuts", font=('Helvetica', 12, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)
        
        # Save Position Shortcut
        ttk.Label(main_frame, text="Save Position:").grid(row=1, column=0, sticky=tk.W)
        self.save_shortcut_label = ttk.Label(main_frame, text=self.save_position_shortcut)
        self.save_shortcut_label.grid(row=1, column=1, sticky=tk.W)
        ttk.Button(main_frame, text="Change", command=lambda: self.change_shortcut('save')).grid(row=1, column=2, padx=5)
        
        # Move to Position Shortcut
        ttk.Label(main_frame, text="Move to Position:").grid(row=2, column=0, sticky=tk.W)
        self.move_shortcut_label = ttk.Label(main_frame, text=self.move_to_position_shortcut)
        self.move_shortcut_label.grid(row=2, column=1, sticky=tk.W)
        ttk.Button(main_frame, text="Change", command=lambda: self.change_shortcut('move')).grid(row=2, column=2, padx=5)
        
        # Saved Position Display
        ttk.Label(main_frame, text="Saved Position", font=('Helvetica', 12, 'bold')).grid(row=3, column=0, columnspan=2, pady=(20,10))
        
        self.position_label = ttk.Label(main_frame, text=f"X: {self.saved_position['x']}, Y: {self.saved_position['y']}")
        self.position_label.grid(row=4, column=0, columnspan=2)
        
        # Status section
        ttk.Label(main_frame, text="Status", font=('Helvetica', 12, 'bold')).grid(row=5, column=0, columnspan=2, pady=(20,10))
        self.status_label = ttk.Label(main_frame, text="Ready")
        self.status_label.grid(row=6, column=0, columnspan=2)
        
        # Instructions
        instructions = "Press the shortcuts to save and restore mouse position.\nThe application will run in the background."
        ttk.Label(main_frame, text=instructions, wraplength=350).grid(row=7, column=0, columnspan=3, pady=20)


    def change_shortcut(self, shortcut_type):
        if self.is_recording:
            return
            
        self.is_recording = True
        self.status_label.config(text="Press new shortcut combination...")
        
        def record_key():
            time.sleep(0.1)  # Small delay to avoid capturing the click event
            keys = keyboard.read_event(suppress=True).name
            time.sleep(0.1)  # Wait for potential modifier keys
            
            # Get all currently pressed keys
            pressed_keys = keyboard.get_hotkey_name()
            if pressed_keys:
                if shortcut_type == 'save':
                    self.save_position_shortcut = pressed_keys
                else:
                    self.move_to_position_shortcut = pressed_keys
                self.root.after(0, self.update_shortcut_labels)
                self.register_hotkeys()
            
            self.is_recording = False
            self.root.after(0, lambda: self.status_label.config(text="Ready"))

        Thread(target=record_key, daemon=True).start()

    def update_shortcut_labels(self):
        self.save_shortcut_label.config(text=self.save_position_shortcut)
        self.move_shortcut_label.config(text=self.move_to_position_shortcut)

    def save_mouse_position(self):
        x, y = pyautogui.position()
        self.saved_position = {'x': x, 'y': y}
        self.position_label.config(text=f"X: {x}, Y: {y}")
        self.status_label.config(text="Position saved!")
        self.root.after(2000, lambda: self.status_label.config(text="Ready"))

    def move_to_saved_position(self):
        x = self.saved_position['x']
        y = self.saved_position['y']
        pyautogui.moveTo(x, y)
        self.status_label.config(text="Moved to saved position!")
        self.root.after(2000, lambda: self.status_label.config(text="Ready"))

    def register_hotkeys(self):
        # Unregister existing hotkeys
        keyboard.unhook_all()
        
        # Register new hotkeys
        keyboard.add_hotkey(self.save_position_shortcut, self.save_mouse_position)
        keyboard.add_hotkey(self.move_to_position_shortcut, self.move_to_saved_position)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = MousePositionManager()
    app.run()
