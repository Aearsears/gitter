import subprocess
import os
import sys
from PIL import Image

CHARACTERS = [" ", ".", ":", "-", "=", "+", "*", "#", "%", "@"]

is_windows = sys.platform == 'win32'

is_macos = sys.platform == 'darwin'


if is_windows:
    default_pager = 'more'
    eol = "\r\n"
else:
    default_pager = 'less -R'
    eol = "\n"

# update pager based on platform
process = subprocess.Popen(
    ['less', '-R'], stdin=subprocess.PIPE, text=True
)


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def img2ascii():
    im = Image.open("pic.jpg")
    width = 10
    height = 10
    grayscale = im.convert("L").resize((width, height))
    ascii = []
    line = ""
    for pixel in list(grayscale.getdata()):
        index = int((255-pixel)*10/256)
        line += CHARACTERS[index]
        if len(line) == width:
            line += eol
            ascii.append(line)
            line = ""

    process.communicate(input="".join(ascii))


if __name__ == "__main__":
    cls()
    img2ascii()
