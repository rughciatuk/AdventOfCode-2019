def calc_same_digit(number):
    num_of_char = 1
    index = 1
    while(index < len(number)):
        if number[0] == number[index]:
            num_of_char += 1
        else:
            return num_of_char
        index += 1
    return num_of_char

def check_criteria(number):
    index = 0
    match = False
    while index < (len(number)):
        num_of_char = calc_same_digit(number[index:])
        if num_of_char == 2:
                match = True
        index += num_of_char
    if match:
        return "".join(sorted(number)) == number
    return False

def main():
    with open("../input.txt") as f:
        input_range = f.read().strip().split('-')
        numbers = [number for number in range(int(input_range[0]),int(input_range[1])) if check_criteria(str(number))]
        print(len(numbers))

if __name__ == "__main__":
    main()