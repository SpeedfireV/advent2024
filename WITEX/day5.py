def part1():
    f = open('2024/day5.txt')
    rules = []
    line = f.readline()
    while line != '\n':
        line = line.replace('\n', '')
        rules.append(line.split('|'))
        line = f.readline()
    updates = []
    line = f.readline()
    while line:
        line = line.replace('\n', '')
        updates.append(line.split(','))
        line = f.readline()
    middle_numbers = 0
    for update in updates:
        process_update = True
        for i in range(len(update)-1):
            if not process_update:
                break
            for j in range(i+1, len(update)):
                for rule in rules:
                    if update[i] == rule[1] and update[j] == rule[0]:
                        process_update = False
        if process_update:
            middle_numbers += int(update[len(update)//2])
    f.close()
    return middle_numbers


def part2():
    f = open('2024/day5.txt')
    rules = []
    line = f.readline()
    while line != '\n':
        line = line.replace('\n', '')
        rules.append(line.split('|'))
        line = f.readline()
    updates = []
    line = f.readline()
    while line:
        line = line.replace('\n', '')
        updates.append(line.split(','))
        line = f.readline()
    middle_numbers = 0
    for update in updates:
        update_sorted = False
        no_operations = True
        while not update_sorted:
            update_sorted = True
            for i in range(len(update)-1):
                if not update_sorted:
                    break
                for j in range(i+1, len(update)):
                    if not update_sorted:
                        break
                    for rule in rules:
                        if not update_sorted:
                            break
                        if update[i] == rule[1] and update[j] == rule[0]:
                            buff = update[i]
                            update[i] = update[j]
                            update[j] = buff
                            no_operations = False
                            update_sorted = False
        if not no_operations:
            middle_numbers += int(update[len(update)//2])
    f.close()
    return middle_numbers


print(part1())
print(part2())
