sum = 0
id = '0'
flag = True
input = open("input.txt", "r")
lines = input.readlines()

for line in lines:  # For each lines
    line = line.split(':')
    id = line[0].split()[1]
    content = line[1].split(';')
    for i in range(len(content)):  # For each draw
        draws = content[i].split(',')
        for draw in draws:  # For each color in a draw
            info = draw.split()

            # We test if the number of cubes of the same color exceeds the authorized number
            if (int(info[0]) > 12 and info[1] == 'red') or (int(info[0]) > 13 and info[1] == 'green') or (int(info[0]) > 14 and info[1] == 'blue'):
                flag = False

    # If the authorized number is not exceeded we update the sum and we reinitialize the flag
    if flag:
        sum += int(id)
    else:
        flag = True

print(sum)
