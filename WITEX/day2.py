def part1():
    f = open('2024/day2.txt')
    line = f.readline()
    safe_reports = 0
    while line:
        line = line.split()
        line = list(map(int, line))
        is_increasing = True
        is_safe = True
        if line[0] > line[1]:
            is_increasing = False
        for i in range(len(line)-1):
            if ((abs(line[i] - line[i+1]) not in [1, 2, 3]) or
                (is_increasing and line[i] > line[i+1]) or
                    (not is_increasing and line[i] < line[i+1])):
                is_safe = False
                break
        if is_safe:
            safe_reports += 1
        line = f.readline()
    f.close()
    return safe_reports


def part2():
    f = open('2024/day2.txt')
    line = f.readline()
    safe_reports = 0
    while line:
        line = line.split()
        line = list(map(int, line))
        for i in range(-1, len(line)):
            is_safe = True
            line_backup = line.copy()
            if i >= 0:
                line.pop(i)
            is_increasing = True
            if line[0] > line[1]:
                is_increasing = False
            for i in range(len(line)-1):
                if ((abs(line[i] - line[i+1]) not in [1, 2, 3]) or
                    (is_increasing and line[i] > line[i+1]) or
                        (not is_increasing and line[i] < line[i+1])):
                    is_safe = False
                    break
            if is_safe:
                safe_reports += 1
                break
            line = line_backup.copy()
        line = f.readline()
    f.close()
    return safe_reports


print(part1())
print(part2())
