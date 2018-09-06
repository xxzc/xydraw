from commands import *
from PIL import Image
import sys


def emit_dot(cmd, img):
    pinv = 0.5
    def topos(x,y):
        return (pinv*x, pinv*(img.size[1]-y-1))
    for y in range(img.size[1]):
        for x in range(img.size[0]) if y%2==0 else range(img.size[0]-1, -1, -1):
            if img.getpixel((x,y)) == 0:
                print(x,y, img.getpixel((x,y)))
                cmd.do(CMD_UPPEN)
                cmd.do(CMD_MOVETO, pos=topos(x,y))
                cmd.do(CMD_DOWNPEN)
    code.do(CMD_UPPEN)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        fnimg = sys.argv[1]
        fncode = sys.argv[2]
    else:
        fnimg = './data/data.png'
        fncode = './data/out.gcode'

    img = Image.open(fnimg)
    px = img.load()
    print(img.format, img.size, img.mode)

    code = Commands()
    emit_dot(code, img)
    code.do(CMD_MOVETO, pos=(0,0))
    code.save(fncode)