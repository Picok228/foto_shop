from PIL import Image
from PIL import ImageDraw

img = Image.open("img_2.png")

I1 = ImageDraw.Draw(img)

I1.text((28, 36), "nice Car", fill=(255, 0, 0))

img.show()

img.save("img2_.png")