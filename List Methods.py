numbers = [8,1,2,3,4,5,5]
unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)

print(numbers.__contains__(8))
#create another copy of numbers list
number2 = numbers.copy()
print(number2)
#sorts from min to max
numbers.sort()
print(numbers)
#reverse from max to min
numbers.reverse()
print(numbers)
#counts how many occurences sample is 2 of 5
print(numbers.count(5))
#check if it is in array if not return boolean value
print (50 in numbers)
#finds and returns index with that value
print(numbers.index(3))
#append is adding a number/object at last index
numbers.append(99)
print(numbers)
#insert at any index
numbers.insert(0,999)
#remove specified value
numbers.remove(99)
print(numbers)
numbers.pop()
print(numbers)
#clear all objects in the array
numbers.clear()
print(numbers)