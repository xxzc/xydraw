

CMD_MOVETO = 'G1 X{x} Y{y}'
CMD_UPPEN = 'M5 G4 P{penwait}'
CMD_DOWNPEN = 'M3 S255 G4 P{penwait}'
CMD_INIT = 'M5 G4 P{penwait} G90 G21 G1 F{speed}'
class Commands:
    def init(self, **para):
        self.para = {'penwait': 0.2,
                    'xres': 1.0,
                    'yres': 1.0,
                    'speed': 3000}
        self.para.update(para)
        self.gcode = ''
        self.do(CMD_INIT)

    def do(self, cmd, **para):
        npara = self.para
        npara.update(para)
        self.gcode += cmd.fomart(para) + '\n'

    def save(self, fname):
        with open(fname, 'w') as f:
            f.write(self.gcode)

    

    