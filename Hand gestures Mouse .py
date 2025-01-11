import cv2
import mediapipe as mp
import pyautogui
import numpy as np

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands()

cap = cv2.VideoCapture(0)
sw, sh = pyautogui.size()

while True:
    success, img = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        break

    img = cv2.flip(img, 1)

    frame_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(img, hand_landmark, mp_hands.HAND_CONNECTIONS)
            h, w, _ = img.shape
            landmark_8 = hand_landmark.landmark[8]
            landmark_4 = hand_landmark.landmark[4]
            cx8, cy8 = int(landmark_8.x * w), int(landmark_8.y * h)
            cx4, cy4 = int(landmark_4.x * w), int(landmark_4.y * h)

            x_screen8 = np.clip(cx8 / w * sw, 0, sw)
            y_screen8 = np.clip(cy8 / h * sh, 0, sh)
            x_screen4 = np.clip(cx4 / w * sw, 0, sw)
            y_screen4 = np.clip(cy4 / h * sh, 0, sh)

            pyautogui.moveTo(x_screen8, y_screen8)

            if np.hypot(cx8 - cx4, cy8 - cy4) < 30: 
                pyautogui.click()
                
            # Draw circles at the fingertips
            cv2.circle(img, (cx8, cy8), 2, (0, 255, 0), 2)
            cv2.circle(img, (cx4, cy4), 2, (0, 255, 0), 2)

    # Display the image with landmarksq
    cv2.imshow("Hand Detection", img)

    # Check for 'q' key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()