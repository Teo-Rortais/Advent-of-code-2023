sum = 0
input = open("input.txt", "r")
lines = input.readlines()

for line in lines:  # For each lines
    first = '0'
    last = '0'
    for i in range(len(line)):  # For each character of the line
        if (ord(line[i]) >= 48) and (ord(line[i]) <= 57):
            if first == '0':
                first = line[i]
            last = line[i]
    num = first + last
    sum += int(num)

print(sum)
