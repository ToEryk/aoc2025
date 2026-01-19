day = 5
filepath = f'Day{day}\\input.txt'
input = open(filepath).read()
lines = input.split('\n\n')

ranges = lines[0].split('\n')
ingredients = lines[1].split('\n')

sum = 0
for ingredient in ingredients:
    for r in ranges:
        start = r.split('-')[0]
        end = r.split('-')[1]
        if int(ingredient) >= int(start) and int(ingredient) <= int(end):
            sum += 1
            print(ingredient)
            break
print(sum)
