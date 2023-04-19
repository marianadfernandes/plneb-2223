from flask import Flask, render_template
import json

app = Flask(__name__)

file = open("dicionario_pt_en_completo.json", encoding="utf8")

db = json.load(file)

@app.route("/")
def home():
    return render_template("welcome.html", title="Welcome!")

@app.route("/terms")
def terms():
    return render_template('terms.html', designations=db.keys())

@app.route("/terms/search")
def procura():
    return render_template("search.html")

@app.route("/term/<t>")
def term(t):
    return render_template('term.html', designation=t, value=db.get(t, "None"))

app.run(host="localhost", port=3000, debug=True)

