# Hand Gesture Game Control

This project uses computer vision and hand gesture recognition to control a game (e.g., Hill Climb Racing) using your webcam. It detects hand gestures to simulate key presses for accelerating and braking.

## Features

- Real-time hand gesture detection using MediaPipe.
- Controls game by simulating 'right' (accelerate) and 'left' (brake) key presses based on thumb and index finger distance.
- Smooth gesture recognition with configurable thresholds.

## Requirements

- Python 3.x
- Webcam
- Dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/adityajaiswal25/Hand_Gesture_Game_Control.git
   cd Hand_Gesture_Game_Control
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Ensure your webcam is connected and not in use by other applications.
2. Run the script:
   ```
   python hand_control.py
   ```
3. A window will open showing your webcam feed with hand landmarks.
4. Use hand gestures to control the game:
   - **Open hand** (thumb and index finger apart): Accelerate (simulates 'right' key)
   - **Closed hand** (thumb and index finger close): Brake (simulates 'left' key)
5. Press 'q' in the window to quit.

## Configuration

- Adjust `THRESHOLD` in `hand_control.py` to change gesture sensitivity.
- Modify `SMOOTH_FRAMES` for gesture smoothing.

## Dependencies

- opencv-python
- mediapipe
- pyautogui

## License

This project is open-source. Feel free to modify and distribute.
