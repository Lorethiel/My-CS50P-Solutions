import sys
from PIL import Image, ImageOps


def main():
    a = get_input(sys.argv)
    b = create_image(a)
    return b



def get_input(x):

    if len(x) < 3:
        print('Too few command-line arguments')
        sys.exit(1)
    elif len(x) > 3:
        print('Too many command-line arguments')
        sys.exit(1)

    try:
        if not (x[1].endswith('.png') or x[1].endswith('.jpg') or x[1].endswith('.jpeg')):
            print('Not an image file')
            sys.exit(1)
        else:
            a = x[1]
            b = x[2]
            if not a[-3:] == b[-3:]:
                sys.exit(1)
            return x
    except FileNotFoundError:
        print('File does not exist')
        sys.exit(1)
    except IndexError:
        print('Too few command-line arguments')
        sys.exit(1)



def create_image(y):
    shirt = Image.open('shirt.png')
    photo = Image.open(y[1])
    size = shirt.size
    photo = ImageOps.fit(photo, size)
    photo.paste(shirt, shirt)
    photo.save(y[2])






if __name__ == '__main__':
    main()
