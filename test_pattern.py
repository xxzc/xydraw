from commands import *

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
    n=5
    startx=0
    code['penwait'] = 0.3
    for mag in [0.4, 0.5, 0.6, 0.7]:
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

if __name__ == '__main__':
    fncode = 'D:\\Downloads\\tp.gcode'
    code = Commands()
    test_lines(code)
    code.save(fncode)