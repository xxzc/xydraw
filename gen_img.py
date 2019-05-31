from commands import *
from PIL import Image
import sys

def rgb_to_cmyk(rgb):
    r,g,b = rgb #int 1,0
    c,m,y,k = (0,0,0,0)
    if 1 in (r,g,b):
        return (1-r,1-g,1-b,0)
    else:
        return (0,0,0,1)


def isblack(pix):
    return pix == 0 or pix[0] == 0

def load_img(fname, target = isblack):
    img = Image.open(fname)
    print(img.format, img.size, img.mode)
    w, h = img.size
    data = [[int(target(img.getpixel((x, h-y-1)))) for y in range(h)] for x in range(w)]
    if 1==0:
        for l in data:
            for p in l:
                if p ==1:
                    print('*',end='')
                else:
                    print('_',end='')
            print()
    return data

def emit_dot(cmd, img):
    pinv = 0.5
    cmd['mag'] = (pinv, pinv)
    for y in range(len(img[0])):
        for x in range(len(img)) if y%2==0 else range(len(img)-1, -1, -1):

            if img[x][y]:
                #print(x,y, img[x][y])
                cmd.do(CMD_UPPEN)
                cmd.do(CMD_MOVETO, pos=(x,y))
                cmd.do(CMD_DOWNPEN)
    cmd.do(CMD_UPPEN)

def emit_line(cmd, img):
    pinv = 0.45
    cmd['mag'] = (pinv, pinv)
    for y in range(len(img[0])):
        out_line(cmd, y, [row[y] for row in img], y%2)
    # for x in range(len(img)):
    #     out_line(cmd, x, img[x], x%2+2)

def out_color():
    fnimg = 'D:\\xydraw\\doc.bmp'
    is_k = lambda p: p[0] == 0 and p[1] == 0 and p[2] == 0
    is_c = lambda p: not is_k(p) and p[0] == 0
    is_m = lambda p: not is_k(p) and p[1] == 0 and not is_c(p) #color hack
    is_y = lambda p: not is_k(p) and p[2] == 0

    #judges = [pis_c, pis_m, pis_y, pis_k]
    judges = [is_c, is_m, is_y, is_k]
    fncodes = ['D:\\xydraw\\c.gcode', 'D:\\xydraw\\m.gcode',
               'D:\\xydraw\\y.gcode', 'D:\\xydraw\\k.gcode']
    for i in (0,1,2,3):
        img = load_img(fnimg,target=judges[i])
        code = Commands(speed=3000, penwait=0.10, penPWM=150)
        emit_dot(code, img)
        code.do(CMD_MOVETO, pos=(0,0))
        code.save(fncodes[i])

if __name__ == '__main__':
    out_color()

    # fnimg = 'D:\\xydraw\\r.bmp'
    # fncode = 'D:\\xydraw\\r.gcode'

    # img = load_img(fnimg)

    # code = Commands(speed=9000, penwait=0.1, penPWM=150)
    # emit_line(code, img)
    # code.do(CMD_MOVETO, pos=(0,0))
    # code.save(fncode)

