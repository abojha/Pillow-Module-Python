from PIL import Image, ImageChops

# image import
image = Image.open('image.jpg')
owl = Image.open('owl.jpg')
python = Image.open('python.png')

# Merging Images with image.methods()
image_blend = Image.blend(image, owl, 0.5) # both images same size and mode
image_blend.show()

image_composite = Image.composite(image,owl,Image.new('L', image.size, 50))
image_composite.show()


# # Image Paste
image.paste(python, (100,300), mask = python)
image.show()

# Channel Operations
image_overlay = ImageChops.overlay(image, owl)
image_darker = ImageChops.darker(image, owl)
image_lighter = ImageChops.lighter(image, owl)
image_soft_light = ImageChops.soft_light(image, owl)
image_hard_light = ImageChops.hard_light(image, owl)
image_difference = ImageChops.difference(image, owl)
image_modulo = ImageChops.add_modulo(image, owl)
image_screen = ImageChops.screen(image, owl)

# display
image_overlay.show()
image_darker.show()
image_lighter.show()
image_soft_light.show()
image_hard_light.show()
image_difference.show()
image_modulo.show()
image_screen.show()

# More complex channel operations
image_add = ImageChops.add(image, owl, scale=2, offset=10)
image_subtract = ImageChops.subtract(image, owl, scale=2, offset=10)
image_logical_and = ImageChops.logical_and(image.convert('1'), owl.convert('1'))
image_logical_or = ImageChops.logical_or(image.convert('1'), owl.convert('1'))

#display
image_add.show()
image_subtract.show()
image_logical_and.show()
image_logical_or.show()

# Super Easy
image_invert = ImageChops.invert(image)
image_invert.show()

# Masking
# Mask must have a specific mode: RGBA, 1 or L.

mask = Image.open('mask.png')
# mask.show()
image_masked_alpha = Image.alpha_composite(image.convert('RGBA'), mask)
image_masked = Image.composite(owl, image, mask.convert('L'))
image_masked.show()