from PIL import Image
from models import Picture

def load_picture(filename):

    image = Image.open(filename)
    return image

def create_picture_object(filename):

    image = load_picture(filename)
    picture = Picture(image)

    return picture
