from datetime import datetime
from datetime import timedelta
import csv

acctslist = []
#import customer accounts from file, append to a list:
with open('accounts.txt', newline='') as inputfile:
    for row in csv.reader(inputfile):
        acctslist.append(row)

#determine the date 90 days from today:
todayplus90 = datetime.today() + timedelta(days=90)

#new list for accounts that match the formula below:
call_list = []

#format dates, determine if any accounts are 90 days from today's date, append to call_list, print account name and assigned sales rep of all accounts in call_list:
for acct in acctslist:
    acct[0] = acct[0].replace('/',' ')
    acct[0] = datetime.strptime(acct[0], '%m %d %Y')
    if acct[0].day == todayplus90.day and acct[0].month == todayplus90.month and acct[0].year == todayplus90.year:
        call_list.append(acct)
        for acct in call_list:
            print(acct[1], acct[2])
            


                
