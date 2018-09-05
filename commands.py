

CMD_MOVETO = 'G1 X{pos[0]:.5f} Y{pos[1]:.5f}'
CMD_UPPEN = 'M5 G4 P{penwait}'
CMD_DOWNPEN = 'M3 S255 G4 P{penwait}'
CMD_WAIT = 'G4 P{waittime}'
CMD_INIT = 'M5 G4 P{penwait} G90 G21 G1 F{speed}\n'
class Commands:
    def __init__(self, **para):
        self.para = {'penwait': 0.2,
                    'waittime': 0.2,
                    'xres': 1.0,
                    'yres': 1.0,
                    'speed': 3000}
        self.para.update(para)
        self.gcode = ''
        self.do(CMD_INIT)

    def setto(self, **para):
        self.para.update(para)

    def do(self, cmd, **para):
        npara = self.para
        npara.update(para)
        self.gcode += cmd.format(**npara) + '\n'

    def save(self, fname):
        with open(fname, 'w') as f:
            f.write(self.gcode)



    