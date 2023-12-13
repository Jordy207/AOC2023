import re


digits_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
def part1(lines):
    total = 0
    for line in lines:
        digits = re.findall(r'(\d)', line)
        total += int(digits[0] + digits[-1])
    print(total)


def part2(lines):
    def create_digit(x):
        return x if x.isdigit() else str(digits_list.index(x))

    total = 0
    for line in lines:
        digits = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', line)
        total += int(create_digit(digits[0]) + create_digit(digits[-1]))
    print(total)


with open('inputs/input1-1.txt', 'r') as f:
    lines = f.readlines()
    part1(lines)
    part2(lines)


