"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import cv2
from gaze_tracking.gaze_tracking import GazeTracking
import pyautogui 
gaze = GazeTracking()
webcam = cv2.VideoCapture(0)
left_blink_counter = 0
right_blink_counter = 0
blink_threshold = 5  # Número de frames que o olho precisa estar fechado para contar como piscada
blink_detected = False
while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    screen_width, screen_height = pyautogui.size()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    text = ""


    if gaze.is_blinking():
     #   pyautogui.click(button='left')
        text = ''
    if gaze.is_blinking_right():
        text = ''
    elif gaze.is_right():
        text = "Looking right"
    elif gaze.is_left():
        text = "Looking left"
    elif gaze.is_center():
        text = "Looking center"

    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    if left_pupil is not None and right_pupil is not None:
        left_pupil_x = left_pupil[0]
        left_pupil_y = left_pupil[1]
        right_pupil_x = right_pupil[0]
        right_pupil_y = right_pupil[1]
        coordenateX = (left_pupil_x + right_pupil_x) / 2
        coordenateY = (left_pupil_y + right_pupil_y) / 2
        left_eye_coords = gaze.eye_left.square_coordinates 
        cv2.rectangle(frame, (left_eye_coords[0], left_eye_coords[1]), 
                             (left_eye_coords[2], left_eye_coords[3]), 
                             (0, 255, 0), 2)
        right_eye_coords = gaze.eye_right.square_coordinates 
        cv2.rectangle(frame, (right_eye_coords[0], right_eye_coords[1]), 
                             (right_eye_coords[2], right_eye_coords[3]), 
                             (0, 255, 0), 2)
        wR = right_eye_coords[2] - right_eye_coords[0] 
        hR = right_eye_coords[3] - right_eye_coords[1] 
        #xS = (screen_width * right_pupil_x) / wR
        #yS = (screen_height * right_pupil_y) / hR
        xS = screen_width - (screen_width * coordenateX) / (wR )
        yS = (screen_height * coordenateY ) / (hR )
    
        
    else:
        left_pupil_x = left_pupil
        right_pupil_x = right_pupil
        left_pupil_y = left_pupil
        right_pupil_y = right_pupil
       # coordenateX = left_pupil
        #coordenateY= right_pupil

    if coordenateX is not None and coordenateY is not None:
        pyautogui.moveTo(xS, yS)


        
    cv2.putText(frame, "Largura Quadrado:  " + str(right_eye_coords[2] - right_eye_coords[0]), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Altura Quadrado: " + str(right_eye_coords[3] - right_eye_coords[1]), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "X do Olho:  " + str(coordenateX), (90, 200), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Y do Olho:  " + str(coordenateY), (90, 235), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "xS:  " + str(xS), (90, 270), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "yS:  " + str(yS), (90, 305), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)


    cv2.imshow("Demo", frame)

    if cv2.waitKey(1) == 27:                                                                                                                                                                                      
        break
   
webcam.release()
cv2.destroyAllWindows()
