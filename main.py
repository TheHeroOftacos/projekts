from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/paldies')
def index():
    return render_template("end.html")

#@app.route('/admin')
def index():
    return render_template("admin.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')