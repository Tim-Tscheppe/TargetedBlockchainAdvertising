# importing Flask and other modules
from flask import Flask, request, render_template
import datetime
import csv
import pyodbc
import pandas as pd
 
# Flask constructor
app = Flask(__name__)  
 
@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       global sender
       sender = request.form.get("sender")
       global receiver
       receiver = request.form.get("receiver")
       global amount
       amount = request.form.get("amount")
       return "Success!: " + amount + " has been sent from " + sender + " to " + receiver
    # Return the 'success' form here
    return render_template("form.html")
 
if __name__=='__main__':
   app.run()

# Collect environment data to construct data frame
currDate = datetime.datetime.now()

# Inject data frame into MS SQL Server db (Note that configuration has to be changed depending on where ur SQL instance is running)
conn = pyodbc.connect("SAMPLEDRIVER};"
                      "Server=MYSERVER;"
                      "Database=MYDB;"
                      "Trusted_Connection=yes;")

cursor = conn.cursor()

## Create Table for Transactions 
cursor.execute('''
    CREATE TABLE ethereumtransactions (
        Sender_Address nvarchar(50),
        Receiver_Address nvarchar(50),
        Date nvarchar(50),
        Transact_Amt int,
        )
               ''')

df = pd.DataFrame()
pd.read_csv('templates/data_template.csv')

with open('data_template.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Sender_Address', 'Receiver_Address', 'Date','Transact_Amt'])
    rows = 1
    
    a = 0
    for i in range(rows):
        CustomerID = a
        a += 1
        Sender_Address = sender
        Receiver_Address = receiver
        Transact_Amt = amount
        Date = Date
        writer.writerow([ Sender_Address, Receiver_Address, Date, Transact_Amt])

# Execute Smart Contract