def part1():
    f = open('2024/day1.txt')
    col1 = []
    col2 = []
    line = f.readline()
    while line:
        line = line.split()
        col1.append(int(line[0]))
        col2.append(int(line[1]))
        line = f.readline()
    total_distance = 0
    while col1:
        total_distance += abs(min(col1) - min(col2))
        col1.remove(min(col1))
        col2.remove(min(col2))
    f.close()
    return total_distance


def part2():
    f = open('2024/day1.txt')
    col1 = []
    col2 = []
    line = f.readline()
    while line:
        line = line.split()
        col1.append(int(line[0]))
        col2.append(int(line[1]))
        line = f.readline()
    similarity_score = 0
    for i in col1:
        similarity_score += i * col2.count(i)
    f.close()
    return similarity_score


print(part1())
print(part2())
