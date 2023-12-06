# This code is for tracking hands movement

# Importing the libraries 
import cv2
import mediapipe as mp 

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mphands = mp.solutions.hands

cap = cv2.VideoCapture(0)

hands = mphands.Hands()

while True:
    # Show image
    data, image = cap.read()

    # Coverting the img to rgb and fliping
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

    results = hands.process(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image,
                hand_landmarks, mphands.HAND_CONNECTIONS)
            # Inside the loop after drawing landmarks
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:

                    # Extract the x-coordinate of the middle finger tip (Landmark 8)
                    x_middle_finger = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.MIDDLE_FINGER_TIP].x
                    y_middle_finger = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.MIDDLE_FINGER_TIP].y

                    # Get the width of the image
                    image_width = image.shape[1]

                    percentagex = int(x_middle_finger*100)

                    # Check if the middle finger is on the left half of the image
                    if (x_middle_finger < 0.5) & (y_middle_finger < 0.5):
                        print("Esquerda: ", percentagex, "%")
                    else:
                        print("Direita: ", percentagex, "%")

                cv2.imshow('HandTracker', image)
    # Stop button
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
