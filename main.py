from commands import *
from PIL import Image
import sys

xres = 0.8

if __name__ == '__main__':
    fnimg = sys.argv[1]
    fncode = sys.argv[2]

    img = Image.open(fnimg)
    print(img.format, img.size, img.mode)

    code = Commands()

    for x in range(img.size[0]):
        for y in range(img.size[1]):
            if img[x,y] >0:
                code.do(CMD_MOVETO, x=x*xres, y=y*xres)
                code.do(CMD_DOWNPEN)
                code.do(CMD_UPPEN)

    code.save(fncode)