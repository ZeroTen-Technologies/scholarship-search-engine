from flask import Flask, render_template      

app = Flask(__name__, static_folder="templates")

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/black")
def black():
    return render_template("black/index_1.html")

@app.route("/rtl")
def rtl():
    return render_template("rtl/index_1.html")

@app.route("/white")
def white():
    return render_template("white/index_1.html")
    
if __name__ == "__main__":
    app.run(debug=True)
