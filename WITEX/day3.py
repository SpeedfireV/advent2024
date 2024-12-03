def part1():
    f = open('2024/day3.txt')
    product = 0
    memory = f.read()
    for i in range(memory.count('mul(')):
        index = memory.index('mul(')
        memory = memory.replace('mul(', '****', 1)
        index += 4
        num1 = ''
        num2 = ''
        corrupted = False
        while memory[index] != ',':
            if memory[index].isdecimal():
                num1 += memory[index]
                index += 1
            else:
                corrupted = True
                break
        index += 1
        while memory[index] != ')':
            if memory[index].isdecimal():
                num2 += memory[index]
                index += 1
            else:
                corrupted = True
                break
        if not corrupted:
            product += int(num1)*int(num2)
    f.close()
    return product


def part2():
    f = open('2024/day3.txt')
    product = 0
    memory = f.read()
    dos = []
    donts = []
    for i in range(memory.count('do()')):
        dos.append(memory.index('do()'))
        memory = memory.replace('do()', '****', 1)
    for i in range(memory.count("don't()")):
        donts.append(memory.index("don't()"))
        memory = memory.replace("don't()", '*******', 1)
    do_range = []
    do = True
    for index in range(len(memory)):
        if do:
            do_range.append(index)
            if index in donts:
                do = False
        else:
            if index in dos:
                do = True
    for i in range(memory.count('mul(')):
        index = memory.index('mul(')
        memory = memory.replace('mul(', '****', 1)
        index += 4
        num1 = ''
        num2 = ''
        corrupted = False
        if index not in do_range:
            corrupted = True
        while memory[index] != ',':
            if memory[index].isdecimal():
                num1 += memory[index]
                index += 1
            else:
                corrupted = True
                break
        index += 1
        while memory[index] != ')':
            if memory[index].isdecimal():
                num2 += memory[index]
                index += 1
            else:
                corrupted = True
                break
        if not corrupted:
            product += int(num1)*int(num2)
    f.close()
    return product


print(part1())
print(part2())
