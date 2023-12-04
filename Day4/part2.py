def number_of_matcing_numbers(user_number, winning_number):
    number = 0
    for win in winning_number:
        for use in user_number:
            if use == win:
                number += 1
    return number


input = open("input.txt", "r")
lines = input.readlines()
scratch_cards = len(lines)*[1]
id = 0

for line in lines:
    line = line.split(":")
    id = int(line[0].split()[1])
    num = number_of_matcing_numbers(line[1].split("|")[0].split(), line[1].split("|")[1].split())
    for i in range(scratch_cards[id - 1]):  # For the number of scratch card we have for this number
        for j in range(num):
            scratch_cards[id + j] += 1

print(sum(scratch_cards))