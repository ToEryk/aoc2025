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

for line in lines:
    for char in line:
        print(char,end="")
    print()
print(sum)