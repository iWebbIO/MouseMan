# MouseMan

A desktop application that allows you to save and restore mouse cursor positions using customizable keyboard shortcuts. Built with Python and Tkinter.

## Features

- Save current mouse position with a customizable keyboard shortcut (default: Ctrl+Alt+S)
- Restore mouse position with a customizable keyboard shortcut (default: Ctrl+Alt+D)
- User-friendly GUI interface
- Persistent settings storage
- Customizable keyboard shortcuts
- Real-time status updates

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/mouse_position_manager.git
cd mouse_position_manager
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:
```bash
python main.py
```

2. The application window will appear showing the current shortcuts and saved position.

3. To change shortcuts:
   - Click the "Change" button next to the shortcut you want to modify
   - Press the new key combination you want to use
   - The new shortcut will be saved automatically

4. Using the application:
   - Press the "Save Position" shortcut (default: Ctrl+Alt+S) to save the current mouse position
   - Press the "Move to Position" shortcut (default: Ctrl+Alt+D) to move the mouse to the saved position
   - The application will run in the background while the window is open

## Requirements

- Python 3.6 or higher
- keyboard==0.13.5
- PyAutoGUI==0.9.54

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
