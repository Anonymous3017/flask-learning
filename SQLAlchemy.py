from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = 'secret_key'
db = SQLAlchemy(app)

# Define the students table model
class Students(db.Model):
    id = db.Column('student_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))

    def __init__(self, name, city, addr, pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin

# Route for the home page, displays all students
@app.route('/')
def show_all():
    with app.app_context():
        return render_template('show_all.html', students=Students.query.all())

# Route for adding a new student
@app.route('/new', methods=['GET', 'POST'])
def new():
    # Handle form submission
    if request.method == 'POST':
        # Validate form input
        if not request.form['name'] or not request.form['city'] or not request.form['addr']:
            flash('Please enter all the fields', 'error')
        else:
            # Create a new student object
            student = Students(request.form['name'], request.form['city'], request.form['addr'], request.form['pin'])

            with app.app_context():
                # Add the student to the database
                db.session.add(student)
                db.session.commit()

            flash('Record was successfully added')
            return redirect(url_for('show_all'))

    # Render the new student form
    return render_template('new.html')

if __name__ == '__main__':
    with app.app_context():
        # Create the database tables if they don't exist
        db.create_all()

    # Start the Flask application
    app.run(debug=True)
