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
        if str_i[0:len(str_i)//2] == str_i[len(str_i)//2:]:
            invalid_numbers.append(i)
    print(f'Start: {start} End: {end}')


for number in invalid_numbers:
    sum += number

print(sum)