from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/welcome_get/<name>')
def welcome_get(name):
    return 'Welcome %s as a get' % name

@app.route('/welcome_post/<name>')
def welcome_post(name):
    return 'Welcome %s as a post' % name

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('welcome_post' ,  name=user))
    else:
        user  = request.args.get('nm')
        return redirect(url_for('welcome_get', name=user))
    
if __name__ == '__main__':
    app.run(debug=True)