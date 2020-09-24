def calc_fuel(mass):
    fuel = (mass//3) - 2
    if fuel <= 0:
        return 0
    return calc_fuel(fuel) + fuel

def main():
    mass_sum = 0
    with open("../input.txt") as f:
        for mass in f:
            mass_sum += calc_fuel(int(mass))

    print(mass_sum)

if __name__ == "__main__":
    main()