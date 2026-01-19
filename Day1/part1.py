filepath = 'Day1\\input.txt'
input = open(filepath).read()
lines = input.split('\n')

dial = 50
times_zero = 0

for line in lines:
    dir = line[0]
    if dir =='L':
        dial -= int(line[1:])
        dial %= 100
        if dial < 0:
            print(dial)
            dial += 100
    elif dir == 'R':
        dial += int(line[1:])
        dial %= 100
    if dial == 0:
        times_zero += 1

    print(line+" "+str(dial))

print(times_zero)