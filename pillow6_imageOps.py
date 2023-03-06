# https://pillow.readthedocs.io/en/stable/reference/ImageOps.html
from PIL import Image, ImageOps

# image import
image = Image.open('image.jpg')

# Color Changes
image_contrast = ImageOps.autocontrast(image = image, cutoff = 5)
image_inverted = ImageOps.invert(image)
image_solarize = ImageOps.solarize(image=image, threshold = 100)
image_posterize = ImageOps.posterize(image=image, bits=2)
image_grayscale = ImageOps.grayscale(image=image)
image_equalized = ImageOps.equalize(image=image)
image_colorize = ImageOps.colorize(image=image.convert('L'), black = 'green', white = 'red')


# Dimension Changes
image_mirror = ImageOps.mirror(image)
image_flip = ImageOps.flip(image)
image_scale = ImageOps.scale(image=image, factor=0.4)
image_contain = ImageOps.contain(image=image, size=(500, 200))


# Adding and Removing
image_border = ImageOps.expand(image=image, border=100, fill=(255, 255, 0))
image_padded = ImageOps.pad(image = image, size = (2500, 1600))
image_fit = ImageOps.fit(image = image, size = (500, 300))
image_crop = ImageOps.crop(image=image, border=400)

# deformer

# display
# image_contrast.show()
# image_inverted.show()
# image_solarize.show()
# image_posterize.show()
# image_grayscale.show()
# image_equalized.show()
# image_colorize.show()
# image_mirror.show()
# image_flip.show()
# image_scale.show()
# image_contain.show()
# image_padded.show()
# image_crop.show()