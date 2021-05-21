from PIL import Image
from PIL import ImageFilter

img1 = Image.open("p1.jpg")
img2 = img1.filter(ImageFilter.BLUR) #模糊
img2.save("out1.jpg")
img3 = img1.filter(ImageFilter.CONTOUR) #描邊
img3.save("out2.jpg")
img4 = img1.filter(ImageFilter.DETAIL) #細節加強
img4.save("out3.jpg")
img5 = img1.filter(ImageFilter.EDGE_ENHANCE) #物件邊緣增強
img5.save("out4.jpg")
img6 = img1.filter(ImageFilter.EDGE_ENHANCE_MORE)
img6.save("out5.jpg")
img7 = img1.filter(ImageFilter.EMBOSS) #浮雕
img7.save("out6.jpg")