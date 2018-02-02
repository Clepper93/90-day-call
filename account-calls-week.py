from datetime import datetime
from datetime import timedelta
import csv

acctslist = []
#import customer accounts from file, append to a list:
with open('accounts.txt', newline='') as inputfile:
    for row in csv.reader(inputfile):
        acctslist.append(row)

#determine the date 90-96 days from today:
todayplus90 = datetime.today() + timedelta(days=90)
todayplus91 = datetime.today() + timedelta(days=91)
todayplus92 = datetime.today() + timedelta(days=92)
todayplus93 = datetime.today() + timedelta(days=93)
todayplus94 = datetime.today() + timedelta(days=94)
todayplus95 = datetime.today() + timedelta(days=95)
todayplus96 = datetime.today() + timedelta(days=96)

#new list for accounts that match the formula below:
call_list = []

#format dates, determine if any accounts are 90-96 days from today's date, append to call_list, print account name and assigned sales rep of all accounts in call_list:
for acct in acctslist:
    acct[0] = acct[0].replace('/',' ')
    acct[0] = datetime.strptime(acct[0], '%m %d %Y')
    if acct[0].day == todayplus90.day and acct[0].month == todayplus90.month and acct[0].year == todayplus90.year:
        call_list.append(acct)
    elif acct[0].day == todayplus91.day and acct[0].month == todayplus91.month and acct[0].year == todayplus91.year:
        call_list.append(acct)
    elif acct[0].day == todayplus92.day and acct[0].month == todayplus92.month and acct[0].year == todayplus92.year:
        call_list.append(acct)
    elif acct[0].day == todayplus93.day and acct[0].month == todayplus93.month and acct[0].year == todayplus93.year:
        call_list.append(acct)
    elif acct[0].day == todayplus94.day and acct[0].month == todayplus94.month and acct[0].year == todayplus94.year:
        call_list.append(acct)
    elif acct[0].day == todayplus95.day and acct[0].month == todayplus95.month and acct[0].year == todayplus95.year:
        call_list.append(acct)
    elif acct[0].day == todayplus96.day and acct[0].month == todayplus96.month and acct[0].year == todayplus96.year:
        call_list.append(acct)

for acct in call_list:
            print(acct[0],acct[1], acct[2])
