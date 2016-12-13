from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World!"

@app.route('/<staffcode>/')
def helloPerson(staffcode):
    return render_template("staffDetails.html", staffcode = staffcode)

app.run(debug=True, host='0.0.0.0')