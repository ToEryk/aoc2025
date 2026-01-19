day = 3
filepath = f'Day{day}\\input.txt'
input = open(filepath).read()
lines = input.split('\n')

powers = []
sum = 0

for line in lines:
    left_index = 0
    max_left = line[left_index]
    
    i = 1
    for number in line[1:len(line)-1]:
        if number > max_left:
            max_left = number
            left_index = i
        i += 1

    right_index = left_index + 1
    max_right = line[right_index]


    for number in line[left_index+1:len(line)]:
        if number > max_right:
            max_right = number
        i += 1

    jolt = int(max_left)*10 + int(max_right)
    powers.append(jolt)

for power in powers:
    print(power)
    sum += power
print(sum)
        