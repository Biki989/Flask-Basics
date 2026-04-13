from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome, this is HTML</H1></html>"


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/form", methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}!'
    return render_template("form.html")


# PASS / FAIL SIMPLE
@app.route('/success/<int:score>')
def success(score):
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"

    return render_template("result.html", results=res)


# PASS / FAIL + SCORE
@app.route('/successres/<int:score>')
def successres(score):
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"

    exp = {"score": score, "res": res}

    return render_template("result1.html", results=exp)


@app.route("/submit", methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':

        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])

        total_score = (science + maths + c + data_science) / 4

        return redirect(url_for("successres", score=int(total_score)))

    return render_template("getresult.html")

if __name__ == '__main__':
    app.run(debug=True)