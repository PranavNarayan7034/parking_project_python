# ---- parking system -----
print('WELCOME TO ABC PARKING')
print()
first_floor = []
second_floor = []
third_floor = []
while True:
    ur = input('''Choose 1 for Parking
    choose 2 for exit    ::: ''')
    print()
    if ur == '1':
        vn = input('Enter your vehicle no:')
        fn = int(input('choose a floor to park your vehicle(1/2/3):'))
        ti = input('how much time you need to park (please add in hrs) ?:')
        info = {'Vehicle_no':vn,'Floor_no':fn,'Time':ti}
        if fn == 1:
            first_floor.append(info)
        elif fn == 2:
            second_floor.append(info)
        elif fn== 3:
            third_floor.append(info)
        else:
            print('invalid floor no...')

        print(first_floor)
        print(second_floor)
        print(third_floor)
    elif ur == '2':
        vn = input('Enter your vehicle no:')
        fn = int(input('Enter the floor no of your vehicle:'))
        if fn==1:
            for i,j in enumerate(first_floor):
                if j['Vehicle_no'] == vn:
                    first_floor.pop(i)
        elif fn==2:
            for i,j in enumerate(second_floor):
                if j['Vehicle_no'] == vn:
                    first_floor.pop(i)
        elif fn==3:
            for i,j in enumerate(third_floor):
                if j['Vehicle_no'] == vn:
                    first_floor.pop(i)
        else:
            print('invalid floor no')



        print('You can exit from your parking slot, Thank you for using ABC parking')
    else:
        print('Invalid input')
    i = input('Do you want to continue or exit from app ?').lower()
    if i=='exit':
        print('Thank you for using ABC parking...')
        break
