

CMD_MOVETO = ''
CMD_UPPEN = ''
CMD_DOWNPEN = ''
CMD_INIT = ''
class Commands:
    def init(self, **para):
        self.para = {}
        self.para.update(para)
        self.gcode = ''
        self.do(CMD_INIT)

    def do(self, cmd, **para):
        npara = self.para
        npara.update(para)
        self.gcode += cmd.fomart(para)

    def save(self, fname):
        with open(fname, 'w') as f:
            f.write(self.gcode)

    

    