class Pixel:

    def __init__(self, rgb):
        self.r = rgb[0]
        self.g = rgb[1]
        self.b = rgb[2]
        self.primary = False

    def get_rgb(self):
        return (self.r, self.g, self.b)

    def set_rgb(self, rgb):
        self.r = rgb[0]
        self.g = rgb[1]
        self.b = rgb[2]

    def set_primary(self):
        self.primary = True

    def adjust_down(self, range):
        self.r = self.r // range * range
        self.g = self.g // range * range
        self.b = self.b // range * range

    def __str__(self):
        return '({}, {}, {})'.format(self.r, self.g, self.b)

    def __repr__(self):
        return self.__str__()

class Picture:

    def __init__(self, picture):
        self.picture = picture.load()
        self.width = picture.size[0]
        self.height = picture.size[1]
        self.pixels = self.create_array()

    def create_array(self):
        pixels = []
        for row in range(self.height):
            row_pixels = []
            for column in range(self.width):
                row_pixels.append(Pixel(self.picture[column, row]))
            pixels.append(row_pixels)

        return pixels

    def get_all_pixels(self):

        return [pixel for row in self.pixels for pixel in row]
