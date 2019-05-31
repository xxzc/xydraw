from commands import *
from PIL import Image

def test_pattern(code):
    startx=0
    for mag in [0.4, 0.45, 0.5]:
        for y in range(0,10):
            for x in range(0,10,2):
                code.ddot(startx+(x+y%2)*mag, y*mag)
        for y in range(5,15):
            for x in range(0,10,2):
                code.ddot(startx+(x+y%2-1)*mag, y*mag)
        startx += mag*10 + 2.0
    code.do(CMD_UPPEN)
    code.do(CMD_MOVETO, pos=(0,0))


def test_lines(code):
    n=10
    startx=0
    code['penwait'] = 0.3
    for mag in [0.4, 0.45, 0.5]:
        code['orig'] = (startx, 0)
        code['mag'] = (mag, mag)
        for i in range(n):
            code.do(CMD_MOVETO, pos=(n+i,0))
            code.do(CMD_DOWNPEN)
            code.do(CMD_MOVETO, pos=(n+i,n))
            code.do(CMD_WAIT)
            code.do(CMD_MOVETO, pos=(n,n+i))
            code.do(CMD_WAIT)
            code.do(CMD_MOVETO, pos=(0,n+i))
            code.do(CMD_UPPEN)
        startx += 2*n*mag

def test_net(code):
    n=5
    startx=0
    pattern = [1,1,1,0]*(n-1) + [1,1,1]

    print(pattern)
    for mag in [0.2, 0.3, 0.4]:
        code['orig'] = (startx, 0)
        code['mag'] = (mag, mag)
        for y in range(0, n):
            out_line(code, (y)*4+1, pattern, 1 if y%2 else 0)
        for x in range(0, n):
            out_line(code, (x)*4+1, pattern, 3 if x%2 else 2)
        startx += len(pattern)*mag + 2.0



if __name__ == '__main__':
    #data = load_img('data/data.png')
    fncode = 'D:\\xydraw\\tp.gcode'
    code = Commands()

    #test_net(code)
    test_pattern(code)
    code.save(fncode)