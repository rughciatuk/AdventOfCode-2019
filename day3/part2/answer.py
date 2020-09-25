def get_path(directions):
    x = 0
    y = 0

    path = [(0,0)] # Starting with 0,0

    for movement in directions:
        direction = movement[0]
        if direction == 'R':
            disten = int(movement[1:])
            path += [(x + delta_x, y) for delta_x in range(1, disten + 1)]
            x += disten
        if direction == 'L':
            disten = int(movement[1:])
            path += [(x - delta_x, y) for delta_x in range(1, disten + 1)]
            x -= disten
        if direction == 'U':
            disten = int(movement[1:])
            path += [(x, y + delta_y) for delta_y in range(1, disten + 1)]
            y += disten
        if direction == 'D':
            disten = int(movement[1:])
            path += [(x, y - delta_y) for delta_y in range(1, disten + 1)]
            y -= disten
    return path

def split_input(data):
    return [wire.split(",") for wire in data.split("\n")] 

def find_min_dis_inter(wires_directions):
    wire0_path = get_path(wires_directions[0])
    wire1_path = get_path(wires_directions[1])
    inters = find_inter(wire0_path, wire1_path)
    
    return min([calc_number_of_steps(inter, wire0_path) + calc_number_of_steps(inter, wire1_path) for inter in inters if inter != (0,0)])

def find_inter(path0, path1):
    return set(path0).intersection(set(path1))

def calc_number_of_steps(intersection, path):
    return path.index(intersection)

def main():
    with open("../input.txt") as f:
        directions = split_input(f.read())
        print(find_min_dis_inter(directions))

if __name__ == "__main__":
    main()