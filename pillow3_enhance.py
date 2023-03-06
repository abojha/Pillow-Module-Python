# https://pillow.readthedocs.io/en/stable/reference/ImageEnhance.html
from PIL import Image, ImageEnhance

# image import
image = Image.open('image.jpg')

# Create an Enhancer
color_enhancer = ImageEnhance.Color(image) #vibrant
contrast_enhancer = ImageEnhance.Contrast(image) # contrast
brightness_enhancer = ImageEnhance.Brightness(image) # brightness
sharpness_enhancer = ImageEnhance.Sharpness(image) # sharpness

# applying the enhaner
# enhanced_image = color_enhancer.enhance(0)
# enhanced_image = contrast_enhancer.enhance(10)
# enhanced_image = brightness_enhancer.enhance(2)
enhanced_image = sharpness_enhancer.enhance(500)

#display
enhanced_image.show()
