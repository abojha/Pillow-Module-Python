# https://pillow.readthedocs.io/en/stable/reference/ImageFilter.html
from PIL import Image, ImageFilter

# image import
image = Image.open('image.jpg')

#basic filter
image_blur = image.filter(ImageFilter.BLUR)
image_contour = image.filter(ImageFilter.CONTOUR)
image_detail = image.filter(ImageFilter.DETAIL)
image_edge = image.filter(ImageFilter.EDGE_ENHANCE)
image_edge_more = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
image_emboss = image.filter(ImageFilter.EMBOSS)
image_sharp = image.filter(ImageFilter.SHARPEN)
image_smooth = image.filter(ImageFilter.SMOOTH)
image_smooth_more = image.filter(ImageFilter.SMOOTH_MORE)


# rank filter
image_filtered_min = image.filter(ImageFilter.MinFilter(size=7))
image_filtered_median = image.filter(ImageFilter.MedianFilter(size=7))
image_filtered_max = image.filter(ImageFilter.MaxFilter(size=7))


# multiband filter
image_boxblur = image.filter(ImageFilter.BoxBlur(radius = 4))
image_gaussblur = image.filter(ImageFilter.GaussianBlur(radius=4))
image_unsharp = image.filter(ImageFilter.UnsharpMask(radius=4))

# combine: blur + emboss
image_emboss = image.filter(ImageFilter.EMBOSS)
image_emboss_blur = image_emboss.filter(ImageFilter.GaussianBlur(radius=2))


#display
# image_blur.show()
# image_contour.show()
# image_detail.show()
# image_edge.show()
# image_edge_more.show()
# image_emboss.show()
# image_sharp.show()
# image_smooth.show()
# image_smooth_more.show()
# image_filtered_min.show()
# image_filtered_median.show()
# image_filtered_max.show()
# image_boxblur.show()
# image_gaussblur.show()
# image_unsharp.show()
image_emboss_blur.show()