def greet_user():
    name = input('Type your name:')
    print(f'Hello {name}')
    print('Welcome Savvy')


#functions first before calling
greet_user() 


#if has parameter required to return a value
def greet_someone(name):
    print(f'Hi there {name}')


greet_someone('Vianca')
#will cause an error cause it needs to return value
greet_someone()