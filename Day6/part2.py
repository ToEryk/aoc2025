day = 6
filepath = f'Day{day}\\input.txt'
input = open(filepath).read()
lines = input.split('\n')

height = len(lines)
width = len(lines[0].split())
sum = 0

index = 0
for i in range(width):
    liczby = []
    col_width = 1
    for j in range(height-1):
        if len(lines[j].split()[i]) > col_width:
            col_width = len(lines[j].split()[i])
    numbers = []
    for col in range(col_width):        
        number_str = ''
        for j in range(height-1):
            number_str += lines[j][index]
        index += 1
        numbers.append(int(number_str))
    operator = lines[height-1].split()[i]
    if operator == '+':
        wynik = 0
        for liczba in numbers:
            wynik += liczba
        sum += wynik        
    elif operator == '*':
        result = 1
        for liczba in numbers:
            result *= liczba
        sum += result
    index += 1


print(sum)


# 123 328  51 64 
#  45 64  387 23 
#   6 98  215 314
# *   +   *   +  