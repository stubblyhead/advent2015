class Computer:
    def __init__(self, instr):
        self.reg_a = 0
        self.reg_b = 0
        self.instructions = instr
        self.pointer = 0

    def hlf(self, r):
        if r == 'a':
            self.reg_a /= 2
        elif r == 'b':
            self.reg_b /= 2
        else:
            raise ValueError(f"r must be either a or b; received {r}")

    def tpl(self, r):
        if r == 'a':
            self.reg_a *= 3
        elif r == 'b':
            self.reg_b *= 3
        else:
            raise ValueError(f"r must be either a or b; received {r}")

    def inc(self, r):
        if r == 'a':
            self.reg_a += 1
        elif r == 'b':
            self.reg_b += 1
        else:
            raise ValueError(f"r must be either a or b; received {r}")
        
    def jmp(self, offset):
        self.pointer += offset

    def jie(self, r, offset):
        if r not in ['a','b']:
            raise ValueError(f"r must be either a or b; received {r}")
        else:
            if r == 'a' and self.reg_a % 2 == 0:
                self.pointer += offset
            elif r == 'b' and self.reg_b % 2 == 0:
                self.pointer += offset

    def jio(self, r, offset):
        if r not in ['a','b']:
            raise ValueError(f"r must be either a or b; received {r}")
        else:
            if r == 'a' and self.reg_a % 2 == 1:
                self.pointer += offset
            elif r == 'b' and self.reg_b % 2 == 1:
                self.pointer += offset

    def run(self):
        while self.pointer < len(self.instructions):
            instr = self.instructions[self.pointer].split()
            if instr[0] == 'hlf':
                self.hlf(instr[1])
                self.pointer += 1
            elif instr[0] == 'tpl':
                self.tpl(instr[1])
                self.pointer += 1
            elif instr[0] == 'inc':
                self.tpl(instr[1])
                self.pointer += 1
            elif instr[0] == 'jmp':
                self.jmp(int(instr[1]))
            elif instr[0] == 'jie':
                self.jie(instr[1][0],int(instr[2]))
            elif instr[0] == 'jio':
                self.jio(instr[1][0],int(instr[2]))

                