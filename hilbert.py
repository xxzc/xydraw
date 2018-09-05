from commands import *

#https://github.com/dentearl/simpleHilbertCurve/blob/master/src/simpleHilbertCurve.py

def rot(n, x, y, rx, ry):
    """
    rotate/flip a quadrant appropriately
    """
    if ry == 0:
        if rx == 1:
            x = n - 1 - x
            y = n - 1 - y
        return y, x
    return x, y

def d2xy(n, d):
    n = int(n)
    d = int(d)
    """
    take a d value in [0, n**2 - 1] and map it to
    an x, y value (e.g. c, r).
    """
    #assert(d <= n**2 - 1)
    t = d
    x = y = 0
    s = 1
    while (s < n):
        rx = 1 & (t // 2)
        ry = 1 & (t ^ rx)
        x, y = rot(s, x, y, rx, ry)
        x += s * rx
        y += s * ry
        t //= 4
        s *= 2
    return x, y

if __name__ == '__main__':
    pinv = 1.0
    def topos(x,y):
        return (pinv*x, pinv*y)
    
    code = Commands()
    code.do(CMD_DOWNPEN)
    m=4
    n=2**m
    for d in range(n*n):
        x,y = d2xy(n,d)
        print(x,y)
        #code.do(CMD_DOWNPEN)
        code.do(CMD_MOVETO, pos=topos(x,y))
        #code.do(CMD_UPPEN)
        code.do(CMD_WAIT)
    
    code.do(CMD_UPPEN)
    code.do(CMD_MOVETO, pos=(0,0))
    code.save('data/hilbert2.gcode')