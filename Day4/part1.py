def points_calculator(user_number, winning_number):
    points = 0
    for win in winning_number:
        for use in user_number:
            if use == win:
                if points == 0:
                    points = 1
                else:
                    points = points * 2
    return points


input = open("input.txt", "r")
lines = input.readlines()
sum = 0

for line in lines:
    line = line.split(":")
    sum += points_calculator(line[1].split("|")[0].split(), line[1].split("|")[1].split())

print(sum)
