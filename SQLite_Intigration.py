from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/enternew')
def new_student():
    return render_template('new_students.html')

@app.route('/addrec', methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            addr = request.form['add']
            city = request.form['city']
            pin = request.form['pin']

            with sql.connect("database.db") as con:
                cur = con.cursor()

                cur.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, addr TEXT, city TEXT, pin TEXT)")
                cur.execute("INSERT INTO students (name, addr, city, pin) VALUES (?, ?, ?, ?)", (nm, addr, city, pin))

                con.commit()
                msg = "Record successfully added."
        except Exception as e:
            con.rollback()
            msg = "Error in insert operation: " + str(e)
            print(msg)

        finally:
            return render_template('sql_result.html', msg = msg)
            con.close()

@app.route('/list')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM students")

    rows = cur.fetchall()
    return render_template('list.html', rows = rows)

if __name__ == '__main__':
    app.run(debug = True)