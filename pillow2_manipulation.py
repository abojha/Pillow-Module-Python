from PIL import Image, ImageColor

# image import
image = Image.open('image.jpg')

# rotating the image
# image_rotate = image.rotate(angle, expand, fillcolor)
image_rotate = image.rotate(60, expand=True, fillcolor = ImageColor.getcolor('red', 'RGB'))
# print(ImageColor.getcolor('red', 'RGB'))

# crop 
# image_crop = image.crop((left_x, top_y, right_x, bottom_y))
image_crop = image.crop((0, 0, 500, 400))

# flipping the image / transpose the image
image_flip_horizontal = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
image_flip_vertical = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
image_transpose = image.transpose(Image.Transpose.TRANSPOSE)
#options: FLIP_LEFT_RIGHT, FLIP_TOP_BOTTOM, ROTATE_90, ROTATE_180, ROTATE_270, TRANSPOSE, TRANSVERSE

# resize
# image.resize((width, height))
image_resize = image.resize((600, 1000)) #bad example

#better example
scale_factor = 2
new_image_size = (image.size[0]*scale_factor, image.size[1] *scale_factor)
image_resize_better = image.resize(new_image_size)

#display
# image_rotate.show()
# image_crop.show()
# image_flip_horizontal.show()
# image_flip_vertical.show()
# image_transpose.show()
# image_resize.show()
image_resize_better.show()

