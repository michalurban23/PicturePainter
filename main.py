from picture_loader import create_picture_object as load
from picture_saver import save_array_to_picture as save
from services import Editor
from sys import argv

RANGES = 32
MAX_COLORS = 25
INPUT_NAME = "test.jpeg"
OUTPUT_NAME = "test_output.jpg"

def save_and_show(picture) :

    new_picture = save(picture, "./assets/{}".format(OUTPUT_NAME))
    new_picture.show()

def main():

    picture = load("./assets/{}".format(INPUT_NAME))
    editor = Editor(picture)

    editor.count_colors(RANGES, MAX_COLORS)
    editor.adjust_colors(RANGES)

    save_and_show(picture)

    picture2 = load('./assets/test_output.jpg')
    editor2 = Editor(picture2)

    editor2.count_colors(32, 25)


if __name__ == "__main__":
    main()
