def part1(lines):
    possible_games = []
    for line in lines:
        id = int(line.split(':', )[0].replace('Game ', ''))
        possible_games.append(id)
        grabs = line.split(':', )[1].split(';', )
        grabs[-1] = grabs[-1].replace('\n', '')
        for grab in grabs:
            colors = grab.split(',', )
            impossible = False
            for color in colors:
                if 'blue' in color and int(color.replace(' blue', '')) > 14:
                    possible_games.remove(id)
                    impossible = True
                    break
                elif 'red' in color and int(color.replace(' red', '')) > 12:
                    possible_games.remove(id)
                    impossible = True
                    break
                elif 'green' in color and int(color.replace(' green', '')) > 13:
                    possible_games.remove(id)
                    impossible = True
                    break
            if impossible:
                break
    print(sum(possible_games))


def part2(lines):
    powers = []
    for line in lines:
        grabs = line.split(':', )[1].split(';', )
        grabs[-1] = grabs[-1].replace('\n', '')
        red = 0
        blue = 0
        green = 0
        for grab in grabs:
            colors = grab.split(',', )
            for color in colors:
                if 'blue' in color and int(color.replace(' blue', '')) > blue:
                    blue = int(color.replace(' blue', ''))
                elif 'red' in color and int(color.replace(' red', '')) > red:
                    red = int(color.replace('red', ''))
                elif 'green' in color and int(color.replace(' green', '')) > green:
                    green = int(color.replace('green', ''))
        powers.append(red * blue * green)
    print(sum(powers))

with open('inputs/input1-2.txt', 'r') as f:
    lines = f.readlines()
    part1(lines)
    part2(lines)
