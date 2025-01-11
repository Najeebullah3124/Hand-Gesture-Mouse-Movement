# 🖐️ Hand Gesture Mouse Control 🖱️

This project uses **computer vision** to control the mouse pointer and perform clicks through **hand gestures**. It leverages the `mediapipe` library for hand detection, `pyautogui` for mouse control, and `opencv` for video capture and processing. 🖥️💻👆

## 🚀 Requirements

To run this project, you need to have the following Python libraries installed:

- `opencv-python` 📷
- `mediapipe` 🤖
- `pyautogui` 🖱️
- `numpy` ➗

You can install the required libraries using `pip`:

```bash
pip install opencv-python mediapipe pyautogui numpy

⚙️ How It Works
Hand Tracking: The program uses mediapipe to detect hand landmarks ✋. Specifically, it tracks the index finger (landmark 8) and thumb (landmark 4).
Mouse Movement: The position of the index finger (landmark 8) is mapped to the screen coordinates to move the mouse pointer 🖱️.
Mouse Click: When the index finger and thumb come close (within a defined distance), a mouse click is simulated using pyautogui 👆🖱️.
Real-time Feedback: The camera feed is displayed in a window with detected hand landmarks and fingertip positions marked with green circles 🔵.
🏃‍♂️ Usage
Run the Python script 🐍.
The camera feed will open, and the program will start detecting hand gestures 👋.
Move your index finger to control the mouse pointer 🖱️.
Bring your thumb and index finger together to perform a click 👆👌.
