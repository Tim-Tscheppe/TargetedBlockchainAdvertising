# importing Flask and other modules
from flask import Flask, request, render_template
 
# Flask constructor
app = Flask(__name__)  
 
@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       global sender
       sender = request.form.get("sender")
       global last_name
       last_name = request.form.get("lname")
       return "Your name is "+ sender + last_name
    # Return the 'success' form here
    return render_template("form.html")
 
if __name__=='__main__':
   app.run()

# Main part of our program goes here

# Print initial sender and receiver
print("Sender address: " + sender + "\n")
print("Receiver address: " + last_name + "\n")

# Collect environment data

# Inject all out data into Azure db

# Execute Smart Contract