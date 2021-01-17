import cv2
import time

cam = cv2.VideoCapture(0)

cv2.namedWindow("Input Data Collection")

img_counter = 1
i = 0
while i < 5:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("Input Data Collection", frame)

    k = cv2.waitKey(1)
 
    img_name = "C:/Users/Frede/OneDrive - Robert Gordon University/Uni/Python Workspace/Writing/Input_Pictures/V_Ring_{}.jpg".format(img_counter)
    cv2.imwrite(img_name, frame)
    print("{} written!".format(img_name))
    img_counter += 1
    i += 1
    time.sleep(5)
    


cam.release()

cv2.destroyAllWindows()