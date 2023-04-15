name = 'Leeeee'

if len(name) < 3:
    print('Name must be at least 3 characters.')
elif len(name) > 50:
    print('Name is too long')
else:
    print('Name looks good')

weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == 'L':
    converted = weight * 0.45
    print(f'You are {converted} Kilos')
else:
#one dash returns float and double slash return int
    converted = weight / 0.45
    print(f'You are {converted} Pounds')

i = 1
while i <= 5:
    print('*' * i)
    i = i + 1
print("Done")

