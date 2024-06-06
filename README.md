# Shiny Hunting Automation Script

This script automates the process of Shiny Hunting in Pokémon games played on the melonDS emulator. It performs soft resets automatically and checks if the encountered Pokémon is shiny by comparing the colors of specific pixels.

## Prerequisites

Make sure you have the following Python libraries installed:

- `pyautogui`
- `opencv-python`
- `numpy`
- `keyboard`

You can install these libraries using the following command:

```sh
pip install pyautogui opencv-python numpy keyboard
```

## Preparation

### 1. Edit the `config.json` file for your hunt:
The `config.json` file contains information about your current hunt like soft reset count, pixel coordinates, the time it takes for your chosen emulator to start after a soft reset and the time you want to take the screenshots at. To find the pixel coordinates simply input some dummy values first and let the script take an initial screenshot (after you have fine tuned the timings). From there you can open it in any image editing software to find a suitable pixel for comparison and then put these coordinates in the `config.json` file as well. 
Lastly edit the `emulator` section of the `config.json` file to match your emulator. NOTE: The window title of the emulator should go there.

### 2. Record the button sequence:
Use the `record_sequence.py` script to record the sequence of button presses needed to start the Pokémon encounter. The recorded sequence should be saved in a file named `sequence.json`.

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
- **`config.json`**: Contains information about current setup like emulator title, soft reset count etc.
- **`sequence.json`**: Contains the recorded button sequence.
- **`screenshots\reference_screenshot.png`**: Reference screenshot for comparison.
- **`screenshots\current_screenshot.png`**: Current screenshot for comparison.

## Troubleshooting
- **Coordinate Error**: Ensure that `pixelCoordinates` from the `config.json` file contains the correct coordinates in the format `x,y`.
- **Emulator Focus**: The script waits for the emulator window to be active. Ensure the window title is correct. The script only works, if the emulator is active. If not, the button sequence execution is paused until the emulator window is active again.

## License
This project is licensed under the MIT License. See the LICENSE file for details.