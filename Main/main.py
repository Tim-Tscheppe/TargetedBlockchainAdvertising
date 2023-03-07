# importing Flask and other modules
from flask import Flask, request, render_template
 
# Flask constructor
app = Flask(__name__)  
 
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       global first_name
       first_name = request.form.get("fname")
       global last_name
       last_name = request.form.get("lname")
       return "Your name is "+first_name + last_name
    return render_template("form.html")
 
if __name__=='__main__':
   app.run()

print(first_name)
print(last_name)