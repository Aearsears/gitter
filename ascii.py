from PIL import Image

CHARACTERS = [" ", ".", ":", "-", "=", "+", "*", "#", "%", "@"]


def img2ascii():
    im = Image.open("pic.jpg")
    width = 150
    height = 50
    grayscale = im.convert("L").resize((width, height))
    ascii = []
    line = ""
    for pixel in list(grayscale.getdata()):
        index = int((255-pixel)*10/256)
        line += CHARACTERS[index]
        if len(line) == width:
            ascii.append(line)
            line = ""
    for l in ascii:
        print(l)


if __name__ == "__main__":
    img2ascii()
