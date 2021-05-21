from PIL import Image
from PIL import ImageFilter

img1 = Image.open("p1.jpg")
img2 = img1.filter(ImageFilter.BLUR)
img2.save("out1.jpg")
img3 = img1.filter(ImageFilter.CONTOUR)
img3.save("out2.jpg")
img4 = img1.filter(ImageFilter.DETAIL)
img4.save("out3.jpg")