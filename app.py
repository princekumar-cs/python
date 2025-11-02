from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            obtained = float(request.form["obtained"])
            total = float(request.form["total"])
            percentage = (obtained / total) * 100
            return render_template("index.html", result=round(percentage, 2))
        except:
            return render_template("index.html", error="Invalid input!")
    return render_template("index.html")

if __name__ == "__main__":
    app.run()

