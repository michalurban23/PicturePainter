from PIL import Image

def save_array_to_picture(picture, filename):

    image = Image.new("RGB", (picture.width, picture.height))
    save_pixels_to_image(picture, image)
    image.save(filename)

    return image

def save_pixels_to_image(picture, image):

    image_pixels = image.load()

    for row_index in range(picture.height):
        for column_index in range(picture.width):
            image_pixels[column_index, row_index] = picture.pixels[row_index][column_index].get_rgb()
