day = 2
filepath = f'Day{day}\\input.txt'
input = open(filepath).read()
lines = input.split('\n')
ranges = lines[0].split(',')
sum = 0
invalid_numbers = []

for ids in ranges:
    start, end = ids.split('-')
    start = int(start)
    end = int(end)


    for i in range(start, end + 1):
        str_i = str(i)
        
        for j in range(len(str_i)//2,0,-1):
            pattern = str_i[0:j]
            patinstring = len(str_i)//len(pattern)
            if pattern * patinstring == str_i:
                invalid_numbers.append(i)
                break

for number in invalid_numbers:
    print(number)


for number in invalid_numbers:
    sum += number

print(sum)