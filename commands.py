

CMD_MOVETO = 'G1 X{pos[0]:.5f} Y{pos[1]:.5f} F{speed}'
CMD_UPPEN = 'M5 G4 P{penwait}'
CMD_DOWNPEN = 'M3 S{penPWM} G4 P{penwait}'
CMD_WAIT = 'G4 P{waittime}'
CMD_INIT = 'M5 G4 P{penwait} G90 G21 G1 F{speed}\n'
class Commands:
    def __init__(self, **para):
        self.para = {'penwait': 0.2,
                     'penPWM': 100,
                    'waittime': 0.2,
                    'xres': 1.0,
                    'yres': 1.0,
                    'speed': 3000,
                    'orig': (0.0,0.0),
                    'mag': (1.0, 1.0)}
        self.para.update(para)
        self.gcode = ''
        self.do(CMD_INIT)

    def setto(self, **para):
        self.para.update(para)

    def __getitem__(self, attr):
        return self.para[attr]

    def __setitem__(self, attr, value):
        self.para[attr] = value

    def do(self, cmd, **para):
        npara = self.para
        npara.update(para)
        if 'pos' in npara:
            npara['pos'] = (npara['orig'][0]+npara['pos'][0]*npara['mag'][0],
                            npara['orig'][1]+npara['pos'][1]*npara['mag'][1])
        self.gcode += cmd.format(**npara) + '\n'

    def ddot(self, x,y):
            self.do(CMD_UPPEN)
            self.do(CMD_MOVETO, pos=(x,y))
            self.do(CMD_DOWNPEN)

    def save(self, fname):
        with open(fname, 'w') as f:
            f.write(self.gcode)



'''dir: 01 x, 23 y'''
def out_line(code, pos, pattern, dir):
    data = pattern.copy()
    data.insert(0,0)
    data.append(0)
    size = len(data)
    if dir == 0:
        coords = [(i-1, pos) for i in range(size)]
    elif dir == 1:
        coords = [(size-i-2, pos) for i in range(size)]
        data.reverse()
    elif dir == 2:
        coords = [(pos, i-1) for i in range(size)]
    elif dir == 3:
        coords = [(pos, size-i-2) for i in range(size)]
        data.reverse()

    for p in range(1, size-1):
        if data[p] == 1 and data[p-1] ==0:
                code.do(CMD_MOVETO, pos=coords[p])
                code.do(CMD_DOWNPEN)
                #print("s: "+str(coords[p]), end=' ')
        if data[p] == 1 and data[p+1] ==0:
                code.do(CMD_MOVETO, pos=coords[p])
                code.do(CMD_UPPEN)
                #print("e: "+str(coords[p]))
