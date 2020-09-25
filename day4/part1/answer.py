def check_criteria(number):
    for index in range(len(number) - 1):
        if number[index] == number[index + 1]:
            break
    else:
        return False

    return "".join(sorted(number)) == number

def main():
    with open("../input.txt") as f:
        input_range = f.read().strip().split('-')
        numbers = [number for number in range(int(input_range[0]),int(input_range[1])) if check_criteria(str(number))]
        print(len(numbers))

if __name__ == "__main__":
    main()