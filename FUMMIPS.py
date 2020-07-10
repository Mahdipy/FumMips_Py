import cu

class PipLine:
    data_memory = [i for i in range(1000)]
    ins_memory = []
    rg = [2 * i for i in range(0, 32)]
    IF_ID = [0, 0]
    ID_EX = [0, 0, 0, 0, 0,0,0,0,0,0,0]
    EX_MEM = [0, 0, 0, 0, 0,0,0,0,0,0,0]
    MEM_WB = [0, 0, 0, 0, 0,0,0,0,0,0,0]
    z = cu.Cu()
    pc_reg = 0


    def IF(self):
        ins = self.ins_memory[self.pc_reg]
        self.IF_ID[0] = self.pc_reg + 4
        self.IF_ID[1] = ins
        # self.CU(ins[26:32])

    def ID(self):
        ins = str(self.IF_ID[1])
        signals = self.z.cu(ins)
        pc = '0000' + ins[0:26] + '00'
        if signals[9]==1:
            self.pc_reg = int(pc,2)
        num1, num2 = self.readregisterfile(ins[21:26], ins[16:21])
        if signals[4] == 1:
            write_adress = int(ins[11:16], 2)
            self.ID_EX[7] = int(ins[11:16], 2)
        else:
            write_adress = int(ins[16:21], 2)
            self.ID_EX[7] = int(ins[16:21], 2)
        extended = ''
        if ins[0] == '0':
            extended = '0000000000000000' + ins[0:16]
        else:
            extended = '1111111111111111' + ins[0:16]
        # 0->pc  1->read1 2->read2  3->write address 4->extended   5->r1 address 6->r2 address 7->rd address
        self.ID_EX[0] = self.IF_ID[0]
        self.ID_EX[1] = num1
        self.ID_EX[2] = num2
        self.ID_EX[3] = write_adress
        self.ID_EX[4] = int(extended, 2)
        self.ID_EX[5] = int(ins[21:26], 2)
        self.ID_EX[6] = int(ins[16:21], 2)
        self.ID_EX[8] = signals
        # self.EX()

    def readregisterfile(self, num1, num2):
        return self.rg[int(num1, 2)], self.rg[int(num2, 2)]

    def EX(self):
        a_alu = self.ID_EX[1]
        b_alu = self.ID_EX[2]
        if self.ID_EX[8][2] == 0:
            a = self.ALU(self.ID_EX[8][3], a_alu, b_alu)
        else:
            a = self.ALU(self.ID_EX[8][3], a_alu, self.ID_EX[4])
        pc = self.ID_EX[0] + (self.ID_EX[4] * 4)
        self.EX_MEM[0] = pc
        self.EX_MEM[1] = a
        self.EX_MEM[2] = self.ID_EX[2]
        self.EX_MEM[3] = self.ID_EX[3]
        self.EX_MEM[4] = self.ID_EX[7]
        self.EX_MEM[5] = self.ID_EX[8]
        # self.MEM()

    def ALU(self, alu_op, num1, num2):
        if alu_op == '000':
            return num1+num2
        elif alu_op == '001':
            return num1 - num2
        elif alu_op == '011':
            return num2|num1
        elif alu_op == '010':
            return num2&num1
        elif alu_op == '110':
            if num1>num2:
                return 1
            else: return 0

    def MEM(self):
        if self.EX_MEM[1] == 0 and self.EX_MEM[5][1]==1 and self.EX_MEM[5][8]==1:
            self.pc_reg = self.EX_MEM[0]
        elif self.EX_MEM[1] == 0 and self.EX_MEM[5][1]==1 and self.EX_MEM[5][8]==0:
            self.pc_reg = self.EX_MEM[0]
        read = 0
        if self.EX_MEM[5][5] == 1:
            self.data_memory.insert(self.EX_MEM[1], self.EX_MEM[2])
        if self.EX_MEM[5][6] == 1:
            read = self.data_memory[self.EX_MEM[1]]
        self.MEM_WB[0] = read
        self.MEM_WB[1] = self.EX_MEM[1]
        self.MEM_WB[2] = self.EX_MEM[3]
        self.MEM_WB[3] = self.EX_MEM[4]
        self.MEM_WB[4] = self.EX_MEM[5]
        # self.WB()

    def WB(self):
        if self.MEM_WB[4][0] == 1:
            if self.MEM_WB[4][7] == 1:
                print('no')
                self.rg[self.MEM_WB[2]] = self.MEM_WB[0]
            else:
                print('yes')
                self.rg[self.MEM_WB[2]] = self.MEM_WB[1]

    # def forwarding_control(self):
    #     MuxA =''
    #     MuxB =''
    #     if self.ID_EX[5] == self.EX_MEM[4]:
    #         MuxA = '01'
    #     elif self.ID_EX[5] == self.MEM_WB[3]:
    #         MuxA = '10'
    #     else:
    #         MuxA = '00'
    #     if self.ID_EX[6] == self.EX_MEM[4]:
    #         MuxB = '01'
    #     elif self.ID_EX[6] == self.MEM_WB[3]:
    #         MuxB = '10'
    #     else:
    #         MuxB = '00'
    #     return MuxA, MuxB

p = PipLine()
print(p.rg)
instruction = '10101000000100011001110010000000'
p.ins_memory.append(instruction)
p.IF()
p.ID()
p.EX()
p.MEM()
p.WB()

print(p.IF_ID)
print(p.ID_EX)
print(p.EX_MEM)
print(p.MEM_WB)
print(p.rg)