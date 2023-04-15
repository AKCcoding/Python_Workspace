email = "Alrae"
another = email[1:-1]
print(another)

#String format
first = 'Alrae'
last = 'Kei'
message = first + ' ' +   last + ' is a engineer'
#another method or concat
msg = f'{first} {last} is a engineer'
print(message)
print(msg)

#for a String length
print(len(first))
print(len(last))
print(first.upper()) 
#capitalize does not make letters uppercase
print(first.capitalize())
#does not get developer after update and returns a boolean value
print(message.replace("engineer","Developer"))
print('Developer' in message)