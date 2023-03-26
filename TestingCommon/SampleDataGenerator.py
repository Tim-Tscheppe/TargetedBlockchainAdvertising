# Python3 program to Create Sample data for our Azure SQL database
# In the future, this could be a piece of a CI/CD pipeline
# @ Tim Tscheppe, Marquette University, 02-19-2023

import csv
import random
import string
import datetime
from datetime import timedelta

print("How many rows of data would you like to generate?")

def GenerateRandomEtherAddress():
    chars = string.ascii_letters + string.digits
    address = '0x' + ''.join(random.choice(chars) for i in range(40))
    return address

def GenerateRandomDate():
    startDate = datetime.datetime.now()
    endDate = startDate + timedelta(days=365)
    randomDate = startDate + (endDate - startDate) * random.random()
    return randomDate

with open('data.csv', 'w', newline='') as file:
     writer = csv.writer(file)
     writer.writerow(['Sender', 'Receiver', 'Tranact Amount', 'Number of Previous Transactions', 'Date / Time'])
     rows = int(input())

     for i in range(rows):
        sender = '0x0000000000000000000000000000000000000000'
        receiver = GenerateRandomEtherAddress()
        amount = random.randrange(0, 1000000)
        prevTransactions = random.randrange(0, 50)
        date = GenerateRandomDate()
        writer.writerow([sender, receiver, amount, prevTransactions, date])







