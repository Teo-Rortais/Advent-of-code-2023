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


def is_key(framed_lines, i, j):
    flag = False
    i += 1
    j += 1
    for m in [i - 1, i, i + 1]:
        for n in [j - 1, j, j + 1]:
            if framed_lines[m][n] not in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."):
                flag = True

    return flag


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
    for char in line:   # For each character of the line
        if (ord(char) >= 48) and (ord(char) <= 57):     # We test if it's a digit
            buffer += char
            if is_key(framed_lines, i, j):      # We test if it's adjacent to a symbol
                flag = True
        elif buffer != "":      # When the number is complete
            if flag:    # We test if it's a gear
                flag = False
                sum += int(buffer)     # We add the numbre to the sum
            buffer = ""

        # To keep the position of the char
        j += 1
        if j > (len(lines[0]) - 1):
            j = 0

    # To keep the position of the char
    i += 1
    if i > len(lines):
        i = 0

print(sum)
