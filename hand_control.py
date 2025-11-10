import cv2
import mediapipe as mp
import pyautogui
import time

# pyautogui setup
pyautogui.PAUSE = 0

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1,
                       min_detection_confidence=0.7,
                       min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
time.sleep(1)

# Track pressed keys
is_right_pressed = False
is_left_pressed = False

# Threshold tuning
THRESHOLD = 0.15  # distance between thumb tip & index tip
SMOOTH_FRAMES = 6

gesture = None
gesture_count = 0

def release_keys():
    global is_right_pressed, is_left_pressed
    if is_right_pressed:
        pyautogui.keyUp('right')
        is_right_pressed = False
    if is_left_pressed:
        pyautogui.keyUp('left')
        is_left_pressed = False

try:
    while True:
        success, frame = cap.read()
        if not success:
            break

        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        current = None

        if results.multi_hand_landmarks:
            hand = results.multi_hand_landmarks[0]
            lm = hand.landmark

            # Thumb tip & index tip
            x4, y4 = lm[4].x, lm[4].y
            x8, y8 = lm[8].x, lm[8].y
            dist = ((x4 - x8)**2 + (y4 - y8)**2)**0.5

            if dist > THRESHOLD:
                current = 'open'  # accelerate
            else:
                current = 'closed'  # brake

            if current == gesture:
                gesture_count += 1
            else:
                gesture = current
                gesture_count = 1

            if gesture_count >= SMOOTH_FRAMES:
                if gesture == 'open':
                    if not is_right_pressed:
                        if is_left_pressed:
                            pyautogui.keyUp('left')
                            is_left_pressed = False
                        pyautogui.keyDown('right')
                        is_right_pressed = True
                elif gesture == 'closed':
                    if not is_left_pressed:
                        if is_right_pressed:
                            pyautogui.keyUp('right')
                            is_right_pressed = False
                        pyautogui.keyDown('left')
                        is_left_pressed = True

            mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)
            cv2.putText(frame, f'{gesture}  dist:{dist:.2f}', (10, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        else:
            release_keys()
            gesture = None
            gesture_count = 0

        cv2.imshow("Hill Climb Control (q to quit)", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except Exception as e:
    print("Error:", e)

finally:
    release_keys()
    cap.release()
    cv2.destroyAllWindows()
