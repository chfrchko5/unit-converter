from flask import Flask, render_template, request

index_file = "index.html"

app = Flask(__name__)

@app.route("/")
def index():
    return render_template(index_file)


@app.route("/convert-length", methods=["POST"])
def convert_length():
    a = request.form["lengthFrom"]
    b = request.form["lengthTo"]
    c = request.form["lengthInput"]

    return f"you want {c} to go from {a} to {b} ?"


if __name__ == "__main__":
    app.run(debug=True)