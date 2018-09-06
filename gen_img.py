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

def emit_line(cmd, img):
    pinv = 0.5
    def topos(x,y):
        return (pinv*x, pinv*(img.size[1]-y-1))
    xmax = img.size[0]

    def line_beg():
        cmd.do(CMD_MOVETO, pos=pos)
        cmd.do(CMD_DOWNPEN)
    def line_end():
        cmd.do(CMD_MOVETO, pos=pos)
        cmd.do(CMD_UPPEN)

    for y in range(img.size[1]):
        pqueue = range(xmax) if y%2==0 else range(xmax-1, -1, -1)
        for i,x in enumerate(pqueue):
            if img.getpixel((x,y)) == 0:
                pos = topos(x,y)
                if i==0:
                    line_beg()
                    break
                if(i == xmax -1):
                    line_end()
                    break
                if(img.getpixel((pqueue[i-1],y)) > 0):
                    line_beg()
                    break
                if(img.getpixel((pqueue[i+1],y)) > 0):
                    line_end()
                    break

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