def part1():
    f = open('2024/day4.txt')
    matrix = []
    line = f.readline()
    for i in range(5):
        matrix.append('.' * len(line) + '.........')
    while line:
        matrix.append('.....' + line.replace('\n', '') + '.....')
        line = f.readline()
    for i in range(5):
        matrix.append(matrix[0])
    words_found = 0
    dir_x = [
        [0, 0, 0],
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3],
        [0, 0, 0],
        [-1, -2, -3],
        [-1, -2, -3],
        [-1, -2, -3]
    ]
    dir_y = [
        [1, 2, 3],
        [1, 2, 3],
        [0, 0, 0],
        [-1, -2, -3],
        [-1, -2, -3],
        [-1, -2, -3],
        [0, 0, 0],
        [1, 2, 3]
    ]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'X':
                for a in range(8):
                    if (matrix[i+dir_x[a][0]][j+dir_y[a][0]] == 'M' and
                            matrix[i+dir_x[a][1]][j+dir_y[a][1]] == 'A' and
                            matrix[i+dir_x[a][2]][j+dir_y[a][2]] == 'S'):
                        words_found += 1
    return words_found


def part2():
    f = open('2024/day4.txt')
    matrix = []
    line = f.readline()
    for i in range(5):
        matrix.append('.' * len(line) + '.........')
    while line:
        matrix.append('.....' + line.replace('\n', '') + '.....')
        line = f.readline()
    for i in range(5):
        matrix.append(matrix[0])
    words_found = 0
    cases = [
        ['M', 'M', 'S', 'S'],
        ['S', 'M', 'M', 'S'],
        ['S', 'S', 'M', 'M'],
        ['M', 'S', 'S', 'M'],
    ]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'A':
                x = [
                    matrix[i+1][j+1],
                    matrix[i+1][j-1],
                    matrix[i-1][j-1],
                    matrix[i-1][j+1]
                ]
                for case in cases:
                    if x == case:
                        words_found += 1
    return words_found


print(part1())
print(part2())
