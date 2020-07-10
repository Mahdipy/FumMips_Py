class Cu :

    def __init__(self) :

        self.regWrite = 0
        self.pcSrc = 0
        self.AluSrc = 0
        self.AluOp = 0
        self.regDst = 0
        self.memWrite = 0
        self.memRead = 0
        self.memtoReg = 0
        self.branch = 0
        self.jump = 0

    def cu(self , instruct):

        opcode = instruct[26:32]
        opcode = int(opcode, 2)
        print(opcode)
        y = []
        if opcode == 0:
            self.regWrite = 1
            self.pcSrc = 0
            self.AluSrc = 0
            self.regDst = 1
            self.memWrite = 0
            self.memRead = 0
            self.memtoReg = 0
            self.branch = 0
            self.jump = 0
            funcCode = instruct[0:6]
            funcCode = int(funcCode, 2)

            # add
            if funcCode == 32 :
                self.AluOp =  '000'

            # sub
            if funcCode == 34 :
                self.AluOp =  '001'

            # or
            if funcCode == 37 :
                self.AluOp =  '011'

            # and
            if funcCode == 40 :
                self.AluOp =  '010'

            # slt
            if funcCode == 42 :
                self.AluOp =   '110'

        # J
        if opcode == 2 :

            self.regWrite = 0        #d
            self.pcSrc =   0         #d
            self.AluSrc = 1
            self.AluOp = 0           #d
            self.regDst =  0         #d
            self.memWrite = 0        #d
            self.memRead = 0         #d
            self.memtoReg = 0        #d
            self.branch = 0
            self.jump = 1
        # Sw
        if opcode == 43:
            self.regWrite = 0
            self.pcSrc =  0
            self.AluSrc = 1
            self.AluOp = '000'
            self.regDst = 0          #d
            self.memWrite = 1
            self.memRead =0
            self.memtoReg = 0        #d
            self.branch = 0
            self.jump = 0
        # Lw
        if opcode == 35:
            self.regWrite = 1
            self.pcSrc = 0
            self.AluSrc = 1
            self.AluOp =  '000'
            self.regDst = 1
            self.memWrite = 0
            self.memRead = 1
            self.memtoReg = 1
            self.branch = 0
            self.jump = 0
        # addi
        if opcode == 10:
            self.regWrite = 1
            self.pcSrc = 0
            self.AluSrc = 1
            self.AluOp = '000'
            self.regDst = 0
            self.memWrite = 0
            self.memRead = 0
            self.memtoReg = 0
            self.branch = 0
            self.jump = 0
        # slti
        if opcode == 10:
            self.regWrite = 1
            self.pcSrc = 0
            self.AluSrc = 1
            self.AluOp = '110'
            self.regDst = 0
            self.memWrite = 0
            self.memRead = 0
            self.memtoReg = 0
            self.branch = 0
            self.jump = 0
        # andi
        if opcode == 12 :
            self.regWrite = 1
            self.pcSrc = 0
            self.AluSrc = 1
            self.AluOp = '010'
            self.regDst = 0
            self.memWrite = 0
            self.memRead = 0
            self.memtoReg = 0
            self.branch = 0
            self.jump = 0
        # ori
        if opcode == 13 :
            self.regWrite = 1
            self.pcSrc = 0
            self.AluSrc = 1
            self.AluOp = '011'
            self.regDst = 0
            self.memWrite = 0
            self.memRead = 0
            self.memtoReg = 0
            self.branch = 0
            self.jump = 0
        # beq
        if opcode == 4 :
            self.regWrite = 1        #d
            self.pcSrc = 1
            self.AluSrc = 0
            self.AluOp = '001'
            self.regDst = 0          #d
            self.memWrite = 0
            self.memRead = 0
            self.memtoReg = 0        #d
            self.branch = 1
            self.jump = 0
        # bne
        if opcode == 5 :
            self.regWrite = 1       #d
            self.pcSrc = 1
            self.AluSrc = 0
            self.AluOp = '001'
            self.regDst = 0          #d
            self.memWrite = 0
            self.memRead = 0
            self.memtoReg = 0        #d
            self.branch = 0
            self.jump = 0


        return [self.regWrite,self.pcSrc, self.AluSrc, self.AluOp,self.regDst,self.memWrite,self.memRead,self.memtoReg,self.branch,self.jump ]
