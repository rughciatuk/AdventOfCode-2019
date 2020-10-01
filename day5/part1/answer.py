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


def find_pair(base_opcodes):
    for noun in range(0,100):
        for verb in range(0,100):
            test_opcodes = base_opcodes.copy()
            test_opcodes[1] = noun
            test_opcodes[2] = verb
            if(run_opcode(test_opcodes) == 19690720):
                return (100* noun + verb)
    return -1

def main():
    with open("../input.txt") as f:
        opcodes = [int(x) for x in f.read().split(",")]
        print(find_pair(opcodes))

if __name__ == "__main__":
    main()