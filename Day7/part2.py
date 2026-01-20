day = 7
filepath = f'Day{day}\\input.txt'
input = open(filepath).read()
lines = input.split('\n')

lines = [list(line) for line in input.split('\n')]
height = len(lines)
width = len(lines[0])
sum = 0
for i in range(height-1):
    for j in range(width):
        if lines[i][j] == "S":
            lines[i+1][j] = "|"
        if lines[i][j] == "|":
            if lines[i+1][j] == ".":
                lines[i+1][j] = "|"
            if lines[i+1][j] == "^":
                lines[i+1][j-1] = "|"
                lines[i+1][j+1] = "|"
                sum += 1

triangle = [0] * (width)
for i in range(height-1):
    next_triangle = triangle[:]
    for j in range(width):
        if lines[i][j] == ".":
            continue
        if lines[i][j] == "S":
            next_triangle[j] = 1
        if lines[i][j] == "|"and j<width-1 and lines[i][j+1] == "^" and j>0 and lines[i][j-1] == "^":
            next_triangle[j] += triangle[j+1] + triangle[j-1]
            next_triangle[j+1] = 0
            next_triangle[j-1] = 0
        elif lines[i][j] == "|" and j<width-1 and lines[i][j+1] == "^":
            next_triangle[j] += triangle[j+1]
            next_triangle[j+1] = 0
        elif lines[i][j] == "|" and j>0 and lines[i][j-1] == "^":
            next_triangle[j] += triangle[j-1]
            next_triangle[j-1] = 0
        
    triangle = next_triangle[:]



result = 0
for num in triangle:
    result += num
print(result)