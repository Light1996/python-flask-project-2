from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/home')
def home():
    return "This is the check to see weather the tests are runing"


@app.route('/')
def route_for_Index_index():
    return render_template('index.html')


@app.route('/git')
def route_for_Git():
    return render_template('git.html')


@app.route('/docker')
def route_for_Docker():
    return render_template('docker.html')


@app.route('/flask')
def route_for_Flask():
    return render_template('flask.html')


@app.route('/ci')
def route_for_cicd():
    return render_template('ci.html')


@app.route('/oop')
def route_for_oop():
    return render_template('oop.html')


@app.route('/aaa')
def route_for_aaa():
    return render_template('aaa.html')


if __name__ == '__main__':
    app.run(debug=True)
