test = "1,9,10,3,2,3,11,0,99,30,40,50"

def run_opcode(opcodes):
    index = 0
    while opcodes[index] != 99:
        if opcodes[index] == 1:
            opcodes[opcodes[index+3]] = opcodes[opcodes[index+1]] + opcodes[opcodes[index+2]]
        elif opcodes[index] == 2:
            opcodes[opcodes[index+3]] = opcodes[opcodes[index+1]] * opcodes[opcodes[index+2]]
        else:
            raise
        index += 4
    return opcodes[0]


def main():
    with open("../input.txt") as f:
        opcodes = [int(x) for x in f.read().split(",")]
        opcodes[1] = 12
        opcodes[2] = 2
        print(opcodes)
        print(run_opcode(opcodes))

if __name__ == "__main__":
    main()