from flask import Flask, render_template

index_file = "index.html"

app = Flask(__name__)

@app.route("/")
def index():
    return render_template(index_file)

if __name__ == "__main__":
    app.run(debug=True)