from flask import Flask, request, render_template
from datetime import date, datetime

app = Flask(__name__)


@app.route("/")
def home():
    name = request.args.get("name", "world")
    return render_template("home.html", name=name)


@app.route("/agecalc", methods=["POST"])
def compute_age():
    name = request.form.get('name')
    birthday = request.form.get('birthday')
    birthdayObject = datetime.strptime(birthday, "%Y-%m-%d")
    currentDate = date.today()
    age = (currentDate.year - birthdayObject.year) - ((currentDate.month,
                                                       currentDate.day) < (birthdayObject.month, birthdayObject.day))
    return render_template("profile.html",
                           # render_template automatically protects from XSS.
                           # It works by using the Jinja2 template engine which enables automatic escaping by default
                           age=age,
                           name=name,
                           birthday=birthday)
