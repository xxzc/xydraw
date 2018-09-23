from commands import *
from PIL import Image
import sys


def load_img(fname):
    def isblack(pix):
        if pix == (0, 0, 0, 255) or pix == (0, 0, 0) or pix == 0:
            return 1
        return 0
    img = Image.open(fname)
    print(img.format, img.size, img.mode)
    w, h = img.size
    data = [[isblack(img.getpixel((x, h-y-1))) for y in range(h)] for x in range(w)]
    return data

def emit_dot(cmd, img):
    pinv = 0.45
    code['mag'] = (pinv, pinv)
    for y in range(len(img[0])):
        for x in range(len(img)) if y%2==0 else range(len(img)-1, -1, -1):
            #print(x,y, img.getpixel((x,y)))
            if img[x][y]:
                cmd.do(CMD_UPPEN)
                cmd.do(CMD_MOVETO, pos=(x,y))
                cmd.do(CMD_DOWNPEN)
    code.do(CMD_UPPEN)

def emit_line(cmd, img):
    pinv = 0.3
    code['mag'] = (pinv, pinv)
    for x in range(len(img)):
        out_line(code, x, img[x], x%2+2)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        fnimg = sys.argv[1]
        fncode = sys.argv[2]
    else:
        fnimg = 'D:\\Downloads\\out.png'
        fncode = 'D:\\Downloads\\out.gcode'

    img = load_img(fnimg)

    code = Commands(speed=9000, penwait=0.15, penPWM=100)
    emit_line(code, img)
    code.do(CMD_MOVETO, pos=(0,0))
    code.save(fncode)