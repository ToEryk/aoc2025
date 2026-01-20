day = 5
filepath = f'Day{day}\\input.txt'
input = open(filepath).read()
lines = input.split('\n\n')

ranges = lines[0].split('\n')

sum = 0

ranges.sort(
    key=lambda x: int(x.split('-')[0])
)

ranges_start = []
while ranges !=ranges_start:
    ranges_start = []
    for r in ranges:
        ranges_start.append(r)
    for i in range(len(ranges)-1):
        current_end = int(ranges[i].split('-')[1])
        next_start = int(ranges[i+1].split('-')[0])
        next_end = int(ranges[i+1].split('-')[1])
        if next_start <= current_end:
            if next_end > current_end:
                ranges[i] = ranges[i].split('-')[0] + '-' + str(next_end)
            ranges.pop(i+1)
            break


for r in ranges:
    start = r.split('-')[0]        
    end = r.split('-')[1]
    sum += int(end) - int(start) + 1

print(sum)