import os
from PIL import Image

image_arr = os.listdir("./girls")
for image in image_arr:
    image_location = "./60x60/" + image
    image_file = "./girls/" +  image
    print(image_file)
    im1 = Image.open(image_file)
    
    width = 60
    height = 60

    im2 = im1.resize((width, height), Image.NEAREST)      # use nearest neighbour
    im2.save(image_location)
