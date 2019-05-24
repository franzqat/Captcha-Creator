import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

# font = ImageFont.truetype("Arial-Bold.ttf",14)
font = ImageFont.truetype("arial.ttf", 45)
img=Image.new("1", (100,100),color=1)
draw = ImageDraw.Draw(img)
draw.text((50, 50),"A",fill=0,font=font,align="center")
draw = ImageDraw.Draw(img)
img.save("a_test.png")