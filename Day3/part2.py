day = 3
filepath = f'Day{day}\\input.txt'
input = open(filepath).read()
lines = input.split('\n')
batteries = 12
powers = []
sum = 0

for line in lines:
    first_index = 0
    first_max = line[first_index]
    current_index = first_index
    current_max = first_max
    powers_line = []
    max_index = 0


    for battery in range(batteries, 0, -1):    
        
        current_max = line[max_index]
        j=max_index + 1
        for number in line[max_index+1:len(line)-(battery-1)]:
            if number > current_max:
                current_max = number
                max_index = j
            j += 1
        powers_line.append(current_max)
        max_index += 1        
    powers.append(powers_line)

for power in powers:
    result = ""
    for p in power:
        result += p
    sum += int(result)
print(sum)
        