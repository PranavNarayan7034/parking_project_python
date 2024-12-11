# ---- parking system -----
from datetime import datetime
import myfunctions as n

print('WELCOME TO ABC PARKING')
print()

while True:
    ur = input('''Choose 1 for Parking
    choose 2 for exit    ::: ''')
    print()
    if ur == '1':
        vn = input('Enter your vehicle no:')
        fn = int(input('choose a floor to park your vehicle(1/2/3):'))
        ti = input('how much time you need to park (please add in hrs) ?:')
        d1 = datetime.now()
        d2 = datetime.now()
        if fn==1:
            n.insertdata('first_floor',vn,d1,d2)
    elif ur == '2':
        vn = input('Enter your vehicle no:')
        fn = int(input('Enter the floor no of your vehicle:'))

        print('You can exit from your parking slot, Thank you for using ABC parking')
    else:
        print('Invalid input')
    i = input('Do you want to continue or exit from app ?').lower()
    if i=='exit':
        print('Thank you for using ABC parking...')
        break