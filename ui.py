def menu_options() -> int:
    print('''
Program Options:
1) Add new patient
2) print all patients
3) Get next patient
4) remove a leaving patient
5) End the program
''')
    while True:
        print('Enter your choice (from 1 to 5) :', end = ' ')
        choice = input()
        if not choice.isdecimal():
            print('Invalid Input, try again')
        elif not int(choice) in [1, 2, 3, 4, 5]:
            print('Invalid Choice, try again')
        else:
            break
    return int(choice)


def add_patient() -> tuple[int, str, int]:
    while True:
        print('Enter specialization number (from 1 to 20) :', end = ' ')
        specialization = input()
        if not specialization.isdecimal():
            print('Invalid Input, try again')
        elif not int(specialization) in range(1, 21):
            print('Invalid specialization, try again')
        else:
            specialization = int(specialization)
            break
    print('Enter Patient name :', end=' ')
    name = input()
    while True:
        print('Status is 0 (normal), 1 (urgent) and 2 (super urgent)')
        print('Enter status number (from 0 to 2) :', end = ' ')
        status = input()
        if not status.isdecimal():
            print('Invalid Input, try again')
        elif not int(status) in [0, 1, 2]:
            print('Invalid status, try again')
        else:
            status = int(status)
            break
    specialization -= 1
    return specialization, name, status

def get_next_patient() -> int:
    while True:
        print('Enter specialization number (from 1 to 20) :', end=' ')
        specialization = input()
        if not specialization.isdecimal():
            print('Invalid Input, try again')
        elif not int(specialization) in range(1, 21):
            print('Invalid specialization, try again')
        else:
            specialization = int(specialization)
            break
    specialization -= 1
    return specialization

def remove_leaving_patient() -> tuple[int, str]:
    while True:
        print('Enter specialization number (from 1 to 20) :', end = ' ')
        specialization = input()
        if not specialization.isdecimal():
            print('Invalid Input, try again')
        elif not int(specialization) in range(1, 21):
            print('Invalid specialization, try again')
        else:
            specialization = int(specialization)
            break
    print('Enter Patient name :', end=' ')
    name = input()
    specialization -= 1
    return specialization, name