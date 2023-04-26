import cv2

# read the images
img1 = cv2.imread('1.jpg')
img2 = cv2.imread('2.jpg')
img3=  cv2.resize(cv2.imread('3.jpg'),(2448,3264))


# perform pixel-wise addition

def imageAddition():
    addition = cv2.add(img1, img2)

    # resize the output image to a specific size (e.g., 640x480)
    output_size = (640, 480)
    resized = cv2.resize(addition, output_size)

    # display the result
    cv2.imwrite('addition.jpg', resized)

    cv2.imshow('Resized Addition', resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
################

def imageSubtraction():
    subtraction=cv2.subtract(img1,img2)
    output_size = (640, 480)

    resized = cv2.resize(subtraction, output_size)

    # display the result
    cv2.imwrite('subtraction.jpg', resized)

    cv2.imshow('Resized Subtraction', resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#################

def imageMultiplication():
    multiplication=cv2.multiply(img1,img2)
    output_size = (640, 480)

    resized = cv2.resize(multiplication, output_size)
    # display the result
    cv2.imwrite('multiplication.jpg', resized)

    cv2.imshow('Resized multiplication', resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#################
def imageDivision():
    division=cv2.divide(img1,img2)
    output_size = (640, 480)


    resized=cv2.resize(division,output_size)
    cv2.imwrite('division.jpg',resized)
    cv2.imshow('Resized Division',resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


imageAddition()
imageSubtraction()
imageMultiplication()
imageDivision()



