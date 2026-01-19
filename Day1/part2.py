filepath = 'Day1\\input.txt'
input = open(filepath).read()
lines = input.split('\n')

dial = 50
times_zero = 0

for line in lines:
    dir = line[0]
    if dir =='L':
        if  dial == 0:
            times_zero -= 1
        dial -= int(line[1:])
        while dial < 0:
            times_zero += 1
            dial += 100
        if dial == 0:
            times_zero += 1
    elif dir == 'R':
        dial += int(line[1:])
        while dial >= 100:
            times_zero += 1
            dial -= 100
    print(line+" "+str(dial)+" Times zero: "+str(times_zero))

print(times_zero)