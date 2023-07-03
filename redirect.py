from flask import Flask, redirect,  url_for, render_template, request
#Initialize the flask application
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Login.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST' and request.form['username'] == 'admin' :
        return redirect(url_for('success'))
    return redirect(url_for('index'))

@app.route('/success')
def success():
    return 'logged in successfully'

if __name__ == '__main__' :
    app.run(debug = True)