import copy
import random

dimension = (10,10)
bomb_count = 12

row = [" " for _ in range(dimension[1])]
table = [copy.deepcopy(row) for _ in range(dimension[0])]
visible_table = copy.deepcopy(table)

while bomb_count > 0:
    x = random.randint(0, dimension[1] - 1)
    y = random.randint(0, dimension[0] - 1)
    if table[y][x] != "*":
        table[y][x] = "*"
        bomb_count = bomb_count - 1


def constraints(y, x):
    lower_x = x - 1 if x - 1 >= 0 else 0
    upper_x = x + 1 if x + 1 <= dimension[1] - 1 else dimension[1] - 1
    lower_y = y - 1 if y - 1 >= 0 else 0
    upper_y = y + 1 if y + 1 <= dimension[0] - 1 else dimension[0] - 1
    return [lower_x, upper_x, lower_y, upper_y]


def check_neighbors(y, x):
    c = constraints(y, x)
    for tile_y in range(c[2], c[3] + 1):
        for tile_x in range(c[0], c[1] + 1):
            if table[tile_y][tile_x] == "*":
                if table[y][x] == " ":
                    table[y][x] = 1
                else:
                    table[y][x] = table[y][x] + 1


for y in range(dimension[1]):
    for x in range(dimension[0]):
        if table[y][x] == "*":
            continue
        check_neighbors(y, x)


def print_table(t):
    print("   0 1 2 3 4 5 6 7 8 9")
    for y in range(dimension[1]):
        print(f"{y} |", end="")
        for x in range(dimension[0]):
            print(str(t[y][x]) + "|", end="")
        print()



print_table(visible_table)

temp_list = list()


def open_up_empty_cells(current):
    c = constraints(temp_list[current][0], x=temp_list[current][1])
    for tile_y in range(c[2], c[3] + 1):
        for tile_x in range(c[0], c[1] + 1):
            if table[tile_y][tile_x] == "*":
                continue
            elif table[tile_y][tile_x] == " ":
                if [tile_y, tile_x] not in temp_list:
                    temp_list.append([tile_y, tile_x])
            else:
                visible_table[tile_y][tile_x] = table[tile_y][tile_x]
    current = current + 1
    if current < len(temp_list):
        open_up_empty_cells(current)


while True:
    input_arr = input("Give row and column number (r,c):").split(",")
    input_y = int(input_arr[0])
    input_x = int(input_arr[1])

    if table[input_y][input_x] == "*":
        visible_table[input_y][input_x] = table[input_y][input_x]
        print_table(visible_table)
        print("Game Over!")
        break
    elif table[input_y][input_x] == " ":
        temp_list.append([input_y, input_x])
        open_up_empty_cells(0)
        temp_list.clear()
    else:
        visible_table[input_y][input_x] = table[input_y][input_x]

    print_table(visible_table)
