# https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html
from PIL import Image, ImageDraw, ImageFont

# image import
image = Image.open('image.jpg')
draw = ImageDraw.Draw(image) # creates a draw object


# Draw shapes
draw.rectangle((200, 400, 700, 600), fill=(255, 0, 0), outline='yellow', width=5)
draw.ellipse((200, 400, 700, 600), fill=(255, 0, 255), outline='purple', width=5)
draw.polygon(((0, 0), (100, 0), (100, 100), (50, 200)), fill='blue', outline='yellow', width=5)
draw.line(((800, 1000), (1000, 1100), (1200, 1000)), fill='black', width=10, joint = 'curve')
image.show()

# draw circle thingies
draw.arc((800, 100, 1000, 300), start=0, end=360, width=10, fill='red')
draw.chord((800, 100, 1000, 300), start=40, end=150, width=10, fill='red')
draw.pieslice((800, 100, 1000, 300), start = 10, end = 180, width = 10, fill='red')

# drawing text
font = ImageFont.truetype('PILLOW/halogen.Otf', size=500)
draw.text((1300, 640), 'Mayank', font=font, fill = (0, 255, 255), align='center', anchor='mm')


image.show()