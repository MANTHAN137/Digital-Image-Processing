from PIL import Image, ImageDraw

# Define the size of the main rectangle
width = 400
height = 300



# Create a new image with the specified size and white background
image = Image.new("RGB", (width, height), "white")

# Define the size and position of the smaller rectangles
small_width = width // 2
small_height = height // 2
rect1_pos = (0, 0)
rect2_pos = (width - small_width, 0)
rect3_pos = (0, height - small_height)
rect4_pos = (width - small_width, height - small_height)
center_rect_pos = (width // 2 - small_width // 2, height // 2 - small_height // 2)

# Create a new drawing object for the image
draw = ImageDraw.Draw(image)

# Draw the smaller rectangles
draw.rectangle((rect1_pos, (rect1_pos[0] + small_width, rect1_pos[1] + small_height)), fill="green")
draw.rectangle((rect2_pos, (rect2_pos[0] + small_width, rect2_pos[1] + small_height)), fill="red")
draw.rectangle((rect3_pos, (rect3_pos[0] + small_width, rect3_pos[1] + small_height)), fill="blue")
draw.rectangle((rect4_pos, (rect4_pos[0] + small_width, rect4_pos[1] + small_height)), fill="yellow")



image.show()
# Save the image as a file
#image.save("rectangle_image.png")
