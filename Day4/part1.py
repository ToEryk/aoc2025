day = 4
filepath = f'Day{day}\\input.txt'
input = open(filepath).read()
lines = input.split('\n')

height = len(lines)
width = len(lines[0]) 

dx = [1,0,-1]
dy = [1,0,-1]

area = [[]]
sum = 0

for i in range (height+2):
    area.append([])
    for j in range (width+2):
        if i == 0 or i == height+1 or j == 0 or j == width+1:
            area[i].append('*')
        else:
            area[i].append(lines[i-1][j-1])

for y in range(len(area)):
    for x in range(len(area[y])):
        if area[y][x] == '@':
            check = 0
            for dirx in dx:
                for diry in dy:
                    if area[y+diry][x+dirx] == '@':
                        check += 1
            if check <5:
                sum += 1

print(sum)

