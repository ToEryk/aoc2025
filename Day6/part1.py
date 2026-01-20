day = 6
filepath = f'Day{day}\\input.txt'
input = open(filepath).read()
lines = input.split('\n')

height = len(lines)
width = len(lines[0].split())
sum = 0

for i in range(width):
    liczby = []
    for j in range(height-1):
        liczby.append(int(lines[j].split()[i]))
    operator = lines[height-1].split()[i]
    if operator == '+':
        wynik = 0
        for liczba in liczby:
            wynik += liczba
        sum += wynik        
    elif operator == '*':
        result = 1
        for liczba in liczby:
            result *= liczba
        sum += result

print(sum)


