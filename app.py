from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('index.html')
    elif request.method == "POST":
        name = request.form.get("name", "World")
        return render_template("greet.html", name=name)

# flask --debug run
