from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.debug = False

app.secret_key = 'yoursecretkey'

@app.route("/hello")
def index():
    flash("What ya your name?")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hi " + str(request.form['name_input']) + ", great to meet you!")
    return render_template("index.html")
