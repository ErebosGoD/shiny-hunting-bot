# Shiny Hunting Automation Script

This script automates the process of Shiny Hunting in Pokémon games played on the melonDS emulator. It performs soft resets automatically and checks if the encountered Pokémon is shiny by comparing the colors of specific pixels.

## Prerequisites

Make sure you have the following Python libraries installed:

- `pyautogui`
- `opencv-python`
- `numpy`

You can install these libraries using the following command:

```sh
pip install pyautogui opencv-python numpy
```

## Preparation

### 1. Set the coordinates of the pixel to check:
Create a file named `coordinates.txt` and specify the x and y coordinates of the pixel to check. You can create a take a dummy screenshot the script took on its first run and examine it using Paint to search for the ideal pixel to check (especially important for moving sprites).

### 2. Record the button sequence:
Use the `record_sequence.py` script to record the sequence of button presses needed to start the Pokémon encounter. The recorded sequence should be saved in a file named `sequence.json`.

### 3. Emulator Window:
Ensure that the title of your emulator window is correctly specified in the `main` function.

Example:
```python
while pyautogui.getActiveWindowTitle() != "[60/60] melonDS 0.9.5":
```

## Usage
### 1. Start your emulator and load your game
### 2. Run the script
```sh
python shiny_hunting.py
```
### 3. Follow the instructions in the terminal
- Press Enter when you're ready
- The script will now automatically perform soft resets and execute the previously recorded button sequence.
- On the 1st run, a reference screenshot will be taken and on consecutive runs another one to compare. You may need to adjust the sleep timer between the screenshots depending on the game and emulator.

## Features
- **Soft Reset**: The script performs soft resets by pressing L + R + Start + Select (the keyboard keys associated with those. You may need to modify the soft reset button sequence in `soft_reset.py` depending on your game).
- **Pixel Check**: A specific pixel on the game screen is checked to determine if the Pokémon is shiny.
- **Save State**: If a shiny is found, the game is automatically saved(Again, you may need to edit the button sequence in `save_state.py` depending on your emulators keybinds).

## Important files
- **`coordinates.txt`**: Contains the pixel coordinates to check
- **`sequence.json`**: Contains the recorded button sequence.
- **`screenshots\reference_screenshot.png`**: Reference screenshot for comparison.
- **`screenshots\current_screenshot.png`**: Current screenshot for comparison.

## Troubleshooting
- **Coordinate Error**: Ensure that `coordinates.txt` contains the correct coordinates in the format `x,y`.
- **Emulator Focus**: The script waits for the emulator window to be active. Ensure the window title is correct. The script only works, if the emulator is constantly active. If not, the button sequence gets executed in the currently active window.

## License
This project is licensed under the MIT License. See the LICENSE file for details.