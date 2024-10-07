import mcschematic

class minecraftCPULoader:
    
    def __init__(self):
        self.instructionSet = {
            "xnor":"0000",
            "xor":"0001",
            "nand":"0010",
            "nor":"0011",
            "and":"0100",
            "or":"0101",
            "add":"0110",
            "sub":"0111",
            "jmp":"1001",
            "li":"1011",
            "dspl":"1111"
        }
        self.schemeticCreator = mcschematic.MCSchematic()
    
    def interpretLine(self, line, index):
        line = line.split(" ")
        instruction = line[0].lower()
        if instruction == "jmp" or instruction == "dspl":
            line.extend([0, 0])
            if instruction == "dspl":
                temp = line[1]
                line[1] = line[3]
                line[3] = temp
        elif instruction == "li":
            line.append(0)
        for i in range(1, 4):
            line[i] = "{0:04b}".format(int(line[i]))
        line = self.instructionSet[instruction][::-1] + line[1][::-1] + line[2][::-1] + line[3][::-1]
        for i, char in enumerate(line):
            if char == "1":
                self.schemeticCreator.setBlock((index*4, i*2, 0), "minecraft:redstone_block")
    
    def interpretFile(self, path, savePath, fileName):
        with open(path, "r") as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                self.interpretLine(line.strip(), i)
        self.schemeticCreator.save(savePath, fileName, mcschematic.Version.JE_1_20_1)


if __name__ == "__main__":
    inputPath = str(input("Enter file path:\n"))
    saveName = str(input("Enter schemetic name:\n"))
    savePath = str(input("Enter save location:\n"))
    loader = minecraftCPULoader()
    loader.interpretFile(inputPath, savePath, saveName)
