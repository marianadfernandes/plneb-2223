from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def home():
    return render_template("welcome.html")

@app.route("/elefantes")
def elefantes():
    return render_template('elefantes.html')

@app.route("/eguas")
def eguas():
    return render_template('eguas.html')

@app.route("/engenharia")
def engenharia():
    return render_template('engenharia.html')

app.run(host="localhost", port=3000, debug=True)

