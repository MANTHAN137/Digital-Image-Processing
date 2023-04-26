import cv2

# Load the image
img = cv2.imread('image.jpg')

# Get the resolution of the image
height, width, channels = img.shape

# Print the resolution
print('Image Resolution:', width, 'x', height)