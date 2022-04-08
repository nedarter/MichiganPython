from flask import Flask,render_template,request,redirect
import pandas as pd

app = Flask(__name__)


@app.route("/")
def index():
    data = pd.read_csv("data.csv").to_dict("records")

    print(data)

    return render_template("index.html", data=data)

@app.route("/AddNew",methods=["POST"])
def AddNew():

    name = request.form["Name"]
    email= request.form["Email"]

    with open("data.csv", "a") as f:
        f.write(f"{name},{email}\n")
 
    return redirect("/")

app.run(debug=True)

