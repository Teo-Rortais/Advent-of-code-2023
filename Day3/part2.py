def full_number(framed_lines, i, j):
    i += 1
    j += 1
    number = framed_lines[i][j]

    if number in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
        t = 1
        char = ""
        while True:
            number += char
            char = framed_lines[i][j + t]
            t += 1
            if char not in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                break
        t = 1
        char = ""
        while True:
            number = char + number
            char = framed_lines[i][j - t]
            t += 1
            if char not in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                break

    else:
        number = ""

    return number


def frame_tab(lines_input):
    framed_lines = lines_input
    for i in range(len(lines_input)):
        if i < len(lines_input) - 1:
            framed_lines[i] = "." + framed_lines[i][0:-1] + "."
        else:
            framed_lines[i] = "." + framed_lines[i] + "."
    framed_lines.insert(0, (len(lines_input) + 1) * ".")
    framed_lines.append((len(lines_input) + 1) * ".")

    return framed_lines


def adjacent(framed_lines, i, j):
    i += 1
    j += 1
    adjacent_numbers = []
    flag = True

    for m in [i - 1, i, i + 1]:
        for n in [j - 1, j, j + 1]:
            if framed_lines[m][n] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                for number in adjacent_numbers:
                    if number == int(full_number(framed_lines, m-1, n-1)):
                        flag = False
                if flag == True:
                    adjacent_numbers.append(int(full_number(framed_lines, m-1, n-1)))
                flag = True

    return adjacent_numbers


input = open("input.txt", "r")
framed_lines = frame_tab(input.readlines())
input = open("input.txt", "r")
lines = input.readlines()
buffer = ""
sum = 0
flag = False
i = 0
j = 0

for line in lines:  # For each line
    for char in line:  # For each character of the line
        if char == "*":  # We test if it's a gear
            list_adjacent_gear = adjacent(framed_lines, i, j)
            if len(list_adjacent_gear) == 2:
                sum += list_adjacent_gear[0] * list_adjacent_gear[1]

        # To keep the position of the char
        j += 1
        if j > (len(lines[0]) - 1):
            j = 0

    # To keep the position of the char
    i += 1
    if i > len(lines):
        i = 0

print(sum)
