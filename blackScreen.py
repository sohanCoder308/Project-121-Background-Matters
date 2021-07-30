import cv2
import numpy as np

video = cv2.VideoCapture(0)

print("Enter 1 for 1st background, Enter 2 for 2nd background")
print("Enter only 1 or 2, if you write anything else it will give errors.")

background_select = input("Enter 1 or 2: ")

if background_select == "1":
    image = cv2.imread("download.jpg")
else:
    image = cv2.imread("background_image.png")    

while True:
    ret, frame = video.read()
    print(frame)

    frame = cv2.resize(frame, (640, 480))
    image = cv2.resize(image, (640, 480))

    u_black = np.array([253, 223, 73])
    l_black = np.array([30, 30, 0])

    mask = cv2.inRange(frame, l_black, u_black)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    f = frame - res
    f = np.where(f == 0, image, f)

    cv2.imshow("video", frame)
    cv2.imshow("mask", f)

    if cv2.waitKey(2) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()