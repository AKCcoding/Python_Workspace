try:
    age = int(input('Age: '))
    print(age)
    salary = 20000
    risk = salary/age
except ValueError:
    print('Invalid Value')
except ZeroDivisionError:
    print('Age cannot be 0')