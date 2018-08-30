import math
from PIL import Image

class Editor:

    def __init__(self, picture):
        self.picture = picture

    def count_colors(self, range_length, max_colors):

        self.color_ranges = {}
        new, duplicate = 0, 0
        for pixel in self.picture.get_all_pixels():
            key = (pixel.r - pixel.r % range_length,
                   pixel.g - pixel.g % range_length,
                   pixel.b - pixel.b % range_length)
            if self.color_ranges.get(key) is None :
                new += 1
                self.color_ranges[key] = 0
            else:
                duplicate += 1
                self.color_ranges[key] += 1

        print(new, duplicate)

        self.top_colors = sorted(self.color_ranges.items(), key=lambda x: -x[1])[:max_colors]
        print(self.top_colors)

    def adjust_colors(self, range_length):
        self.top_ranges = [colors[0] for colors in self.top_colors]

        in_top = 0
        outside_top = 0

        for pixel in self.picture.get_all_pixels():
            pixel.adjust_down(range_length)
            if pixel.get_rgb() not in self.top_ranges:
                self.set_to_closest_color(pixel)
                outside_top += 1
            else:
                in_top += 1

    def set_to_closest_color(self, pixel):
        min_difference = 10000
        closest_color = (255, 255, 255)
        for color in self.top_ranges:
            difference = math.sqrt(
                math.pow(pixel.r - color[0], 2) +
                math.pow(pixel.g - color[1], 2) +
                math.pow(pixel.b - color[2], 2)
                )
            if difference < min_difference:
                min_difference = difference
                closest_color = color

        pixel.set_rgb(closest_color)



def split(picture):

    for row_index in range(picture.height):
        for column_index in range(picture.width - 1):
            current = picture.pixels[row_index][column_index]
            next = picture.pixels[row_index][column_index + 1]
            if (row_index % 20 == 0 or column_index % 20 == 0):
                r = picture.pixels[row_index][column_index][0] + 255#(0, 0, 0)
                g = picture.pixels[row_index][column_index][1] + 255#(0, 0, 0)
                b = picture.pixels[row_index][column_index][2] + 255#(0, 0, 0)
                # picture.pixels[row_index][column_index] = (int(r), int(g), int(b))
            if is_different(current, next, 10):
                picture.pixels[row_index][column_index] = (0, 0, 0)

def is_different(pixel_1, pixel_2, treshold):

    difference = 0

    for i in range(3):
        difference+= math.pow(pixel_1[i] - pixel_2[i], 2)

    return difference / 3 > math.pow(treshold, 2)
