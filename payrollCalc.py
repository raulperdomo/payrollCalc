#!/usr/bin/python
import datetime
def setPeriod():
    date = input('Please enter the date the period began (mm/dd): ')
    date = date.split('/')
    period = datetime.date(datetime.date.today().year,int(date[0]),int(date[1]))
    td = datetime.timedelta(days=14)
    endPeriod = period + td
    return f'{period} to {endPeriod}'

def employeeHours(period):
    name = input('Which employee? ')
    hours = 0.0
    print(f'Please enter the shift lengths during the period {period} followed by the letter "q".')
    while 1:
        try:
            hour = input()
            if hour == 'q':
                break
            else:
                hours += float(hour)
        except:
            print('Bad formatting.')
    return [ name, hours ]

def report(period, empList):
    print()
    print('*********Payroll Report*********')
    print(period.center(32))
    print()
    for name in empList:
        print(f'{name[0].title()} worked {name[1]} hours\nand earned {name[2]} in commission.')
        print()

period = setPeriod()
print(f'---Payroll for the period {period}---')
employees = [employeeHours(period)]
while 1:
    print("Would you like to enter another employee? [y]/n ")
    yn = input()
    if yn == 'n':
        break
    else:
        employees.append(employeeHours(period))
for x in range(len(employees)):
    commish = input(f'How much commission did {employees[x][0]} make? ') 
    employees[x].append(commish)
report(period, employees)



