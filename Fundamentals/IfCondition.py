is_hot = False
is_cold = False

if is_hot:
    print('Its a hot weather')
    print('Drink Plenty of Water')
elif is_cold:
    print('Its Cold')
    print('Stay warm')
else:
    print('Normal Day')

price = 20
has_good_credit = False
has_high_income = True
has_no_balance = True
no_criminalrecord = False
good_citizen = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down Payment : ${down_payment}")

if has_high_income and has_no_balance:
    print('Eligible Loaner')

if good_citizen and not no_criminalrecord:
    print('Good citizen no criminal record')