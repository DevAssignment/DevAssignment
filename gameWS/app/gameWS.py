from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # TODO
    return render_template("index.html")

@app.route('/login')
def login():
    # TODO
    return render_template()

@app.route('/playerProgress')
def progress():
    # TODO
    return render_template()

@app.route('exercises')
def exercises():
    # TODO
    return render_template()

@app.route('specificExercise')
def specificexercise():
    # TODO
    return render_template()

@app.route('test')
def diagnosticTest():
    # TODO
    pass

if __name__ == '__main__':

    app.run()


