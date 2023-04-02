# importing Flask and other modules
from flask import Flask, request, render_template
 
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

# Main part of our program goes here

# Print initial sender and receiver (for debug)
print("Sender address: " + sender + "\n")
print("Receiver address: " + receiver + "\n")
print("Amount:" + amount + "\n")

# Collect environment data

# Inject data frame into MS SQL Server db

# Execute Smart Contract