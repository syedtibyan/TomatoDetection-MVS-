# Importing all modules
import cv2
import numpy as np

# Capturing webcam footage
cap = cv2.VideoCapture(0)

while True:
    
    _, frame = cap.read()  # Reading webcam footage

    blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)    # Blurring the image
    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)  # Converting BGR image to HSV format
	
    # Specifying upper and lower ranges of color to detect in hsv format
    lower_white = np.array([0, 100, 100])
    upper_white = np.array([10, 255, 255]) # (These ranges will detect RED)

    # Masking the image to find our color
    mask = cv2.inRange(hsv, lower_white, upper_white)
	
    # Finding contours in mask image
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        cv2.drawContours(frame, contour, -1, (0, 255, 0), 3) # Finding position of all contours
		
    cv2.imshow("Frame", frame) # Displaying webcam image
    cv2.imshow("Mask", mask)   # Displaying mask image
    print ('tomato')
    key = cv2.waitKey(1)
    if key == 27:
        break
        
cap.release()
cv2.destroyAllWindows()