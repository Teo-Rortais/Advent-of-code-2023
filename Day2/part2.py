sum = 0
min_red = 0
min_green = 0
min_blue = 0
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

            # We are looking for the maximum of each color
            if info[1] == "red":
                if int(info[0]) > min_red:
                    min_red = int(info[0])
            elif info[1] == "green":
                if int(info[0]) > min_green:
                    min_green = int(info[0])
            elif info[1] == "blue":
                if int(info[0]) > min_blue:
                    min_blue = int(info[0])

    # Calculate the sum and reinitialize the variables "min"
    sum += min_red * min_green * min_blue
    min_red = 0
    min_green = 0
    min_blue = 0

print(sum)
