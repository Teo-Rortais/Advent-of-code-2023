def replace_numbers(string):
    new_string = string.replace("one", "1")
    new_string = new_string.replace("two", "2")
    new_string = new_string.replace("three", "3")
    new_string = new_string.replace("four", "4")
    new_string = new_string.replace("five", "5")
    new_string = new_string.replace("six", "6")
    new_string = new_string.replace("seven", "7")
    new_string = new_string.replace("eight", "8")
    new_string = new_string.replace("nine", "9")
    return new_string


def replace_step_by_step(string, direction):
    new_string = ""
    if direction == 1:
        for i in range(len(string)):
            new_string += string[i]
            new_string = replace_numbers(new_string)
    else:
        for i in range(len(string)):
            new_string = string[-i-1] + new_string
            new_string = replace_numbers(new_string)
    return replace_numbers(new_string)


sum = 0
input = open("input.txt", "r")
lines = input.readlines()

for line in lines:  # For each lines
    first = '0'
    last = '0'
    line = replace_step_by_step(line, 1) + replace_step_by_step(line, -1)
    for i in range(len(line)):  # For each character of the line
        if (ord(line[i]) >= 48) and (ord(line[i]) <= 57):
            if first == '0':
                first = line[i]
            last = line[i]
    num = first + last
    sum += int(num)
    print(num)

print(sum)
