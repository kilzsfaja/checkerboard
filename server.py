from flask import Flask, render_template

app = Flask(__name__)

# 8x8 checkerbox
@app.route("/", methods=["GET"])
def checkerbox():
    return render_template("index.html", x = 4, y = 4)

# 8x4 checkerbox
@app.route("/<int:y>", methods=["GET"])
def checkerbox_y(y):
    y = int(y / 2)
    return render_template("index.html", x = 4, y = y,)

# x times y checkerbox
@app.route("/<int:y>/<int:x>", methods=["GET"])
def checkerbox_x_y(x, y):
    x = int(x / 2)
    y = int(y / 2)
    return render_template("index.html", x = x, y = y)

if __name__ == "__main__":
    app.run(debug = True)