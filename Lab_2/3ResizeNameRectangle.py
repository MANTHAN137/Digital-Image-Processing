import cv2

cap = cv2.VideoCapture('image.jpg')



while True:
    success, imgOutput = cap.read()

    start_point = (0,0)

    # Ending coordinate, here (220, 220)
    # represents the bottom right corner of rectangle
    end_point = (960, 1280)

    # Blue color in BGR
    color = (255, 0, 0)

    # Line thickness of 2 px
    thickness = 20

    # Using cv2.rectangle() method
    # Draw a rectangle with blue line borders of thickness of 2 px
    #image = cv2.rectangle(image, start_point, end_point, color, thickness)
    imgOutput = cv2.rectangle(imgOutput,  start_point, end_point, color, thickness)   #
    imgOutput = cv2.putText(imgOutput, "Manthan 201080020", (130, 35), 2, 0.8, (255,0,0), 2, cv2.LINE_AA)

    cv2.imshow("Image", imgOutput)
    cv2.waitKey(0)

    img_half = cv2.resize(imgOutput, (imgOutput.shape[0] // 2, imgOutput.shape[1] // 2))
    print(img_half.shape)

    cv2.imshow("HalfImage", img_half)
    cv2.waitKey(0)

    cv2.imwrite("HalfMyImage.jpg", img_half)
