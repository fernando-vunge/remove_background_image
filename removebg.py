from rembg import remove
from PIL import Image

def removebg(name_of_file, path):
    image_with_background = Image.open(path)
    image_without_background = remove(image_with_background)
    image_without_background.save(str(path).replace(name_of_file, "out"))