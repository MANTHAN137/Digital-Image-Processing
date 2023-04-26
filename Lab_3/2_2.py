# import required libraries
from PIL import Image, ImageDraw

# set the size of the rectangle and its border
width = 700
height = 500
border_thickness = height // 10

# set the size of the inner rectangle and its border
inner_width = width // 3.5
inner_height = height // 3.5
inner_border_thickness = border_thickness

# calculate the position of the inner rectangle
inner_x1 = (width - inner_width) // 2
inner_y1 = (height - inner_height) // 2
inner_x2 = inner_x1 + inner_width
inner_y2 = inner_y1 + inner_height

# create a new image
image = Image.new(mode='RGB', size=(width, height), color='white')

# create a drawing object
draw = ImageDraw.Draw(image)

# draw the outer rectangle and its border
outer_x1 = border_thickness // 2
outer_y1 = border_thickness // 2
outer_x2 = width - border_thickness // 2
outer_y2 = height - border_thickness // 2
draw.rectangle(xy=[(outer_x1, outer_y1), (outer_x2, outer_y2)], outline='black', width=border_thickness)

# draw the inner rectangle and its border
draw.rectangle(xy=[(inner_x1, inner_y1), (inner_x2, inner_y2)], outline='black', width=inner_border_thickness)

# save the image
image.save('bordered_rectangle.png')
