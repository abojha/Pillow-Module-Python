from PIL import Image

# Create New image by import
image = Image.open('image.jpg')
# # show the picture
# image.show()

# Alternate way to import an image
# with Image.open('PILLOW/image.jpg') as image:
#     image.show()

#Create a new image from scratch
# Image.new(format, size)
# image_blank = Image.new('RGBA', (1000, 600))
# image_blank.show()

#Saving the picture
# image.save('PILLOW/test_save.png')

#image information
print(image.size)
print(image.filename)
print(image.format)
print(image.format_description)