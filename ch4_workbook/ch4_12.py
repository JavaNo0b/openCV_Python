import numpy as np
import cv2


def onChange(value):
    global image, title

    add_value = value - int(image[0][0])
    print("추가 화소값:", add_value)
    image[:] = image + add_value
    cv2.imshow(title, image)


def keyEvent(value):
    print(cv2.getTrackbarPos('Brightness', title))
    while True:
        key = cv2.waitKeyEx(100)

        if key == 27:
            cv2.destroyAllWindows()
            break
        elif key == 2424832:
            cv2.setTrackbarPos('Brightness', title, max(value - 1, 0))
        elif key == 2555904:
            cv2.setTrackbarPos('Brightness', title, min(value + 1, 255))


image = np.zeros((300, 500), np.uint8)

title = 'Trackbar Event'
cv2.imshow(title, image)

cv2.createTrackbar('Brightness', title, image[0][0], 255, onChange)
keyEvent(cv2.getTrackbarPos('Brightness', title))