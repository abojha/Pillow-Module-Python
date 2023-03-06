from PIL import Image
from numpy import array

# import image
image = Image.open('image.jpg')

#################################
# ANALYSING PICTURE INFORMATION #
#################################

#numpy section
print(array(image))
print(array(image.getchannel('R')))

# colors only
# image.getpixel((x, y))
print(image.getpixel((0, 0)))
print(image.getcolors(maxcolors=image.size[0]*image.size[1])) # max color argument = 255 -> if image has more colors it returns none

# gettig picture information
print(image.mode)
print(image.getbands())
print(image.info)

# channels
red_channel = image.getchannel('R')
red_channel.show()

######################
# COLOR CONVERSTIONS #
######################

# 1 bit grayscale image
image_grayscale_1bit = image.convert('1')
print(array(image_grayscale_1bit))
print(image_grayscale_1bit.getbands())
image_grayscale_1bit.show()


# 8 bit grayscale image
image_grayscale_l = image.convert('L')
print(array(image_grayscale_l))
print(image_grayscale_l.getbands())
image_grayscale_l.show()


# Palette
palette = image.convert('P') # 256 colors only
print(array(palette)) # not colors! refrence to a color in a palette
print(palette.getpalette())
# palette.show()

# palette of 16 color
palette_16 = image.convert('P', palette = Image.Palette.ADAPTIVE, colors = 16)
# update the color palette
new_palette = [x // 2 for x in palette_16.getpalette()]
palette_16.putpalette(new_palette)
palette_16.show()


############################
# CHANGE INDIVIDUAL PIXELS #
############################

# image.putpixel(pos, color)
image.putpixel((100, 200), (255, 0, 0))

for x in range(image.size[0]):
    for y in range(image.size[1]):
        if image.getpixel((x,y))[0] > 200:
            image.putpixel((x,y), (0, 0, 0))


image.show()