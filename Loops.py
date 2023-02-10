prices = [10,20,30]

total = 0 
for price in prices:
    total += price
print(f'Total: {total}')

#nested loop
for x in range(4):
    for y in range(3):
        print(f'{x},{y}')

#F output
numbers = [5,2,5,2,2]

for number in numbers:
    print('x' * number)