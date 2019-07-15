from PIL import Image
import os
def crop(image_path, coords):
    """
    @param image_path: The path to the image to edit
    @param coords: A tuple of x/y coordinates (x1, y1, x2, y2)
    @param saved_location: Path to save the cropped image
    """
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(image_path)
    #cropped_image.show()
if __name__ == '__main__':
    image_arr = os.listdir("./girls")
    for image in image_arr:
        image_location = "./girls/" + image
        crop(image_location, (0, 0, 160, 160))
