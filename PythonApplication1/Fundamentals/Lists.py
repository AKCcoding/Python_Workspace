names = ['Rae','Kian','Jhansen','Jhanred','Melon']
names[0] = 'Alrae'
print (names)

numbers = ['1','2','3','4','5']
max = numbers[0]
min = numbers[0]
for number in numbers:
        if number > max:
            max = number
for number in numbers:
        if number< min:
            min = number
print(f'Max: {min},{max}')
