from commands import *
from PIL import Image
import sys



if __name__ == '__main__':
    fnimg = sys.argv[1]
    fncode = sys.argv[2]

    img = Image.open(fnimg)
    px = img.load()
    print(img.format, img.size, img.mode)

    code = Commands()

    pinv = 0.5
    def topos(x,y):
        return (pinv*x, pinv*(img.size[1]-y-1))
    for y in range(img.size[1]):
        for x in range(img.size[0]) if y%2==0 else range(img.size[0]-1, -1, -1):
            if px[x,y] == 0:
                #print(x,y, px[x,y])
                code.do(CMD_UPPEN)
                code.do(CMD_MOVETO, pos=topos(x,y))
                code.do(CMD_DOWNPEN)

    code.do(CMD_UPPEN)
    code.do(CMD_MOVETO, pos=(0,0))
    code.save(fncode)