from flask import Flask, request, redirect, render_template, session, flash
from validations import formIsValid
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key="secretsrunsdeep"

mysql = MySQLConnector(app, 'emailValid')

@app.route('/')
def index():
    emails = mysql.query_db("SELECT * FROM emails")
    print emails
    return render_template('/index.html')


@app.route('/submit', methods=['POST'])
def create():
    state = formIsValid(request.form)
    if (state['isValid']):
        query = "INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
    # We'll then create a dictionary of data from the POST data received.
        data = {'email': request.form['email']}
    # Run query, with dictionary values injected into the query.
        mysql.query_db(query, data)
        flash('The email address you entered '+request.form['email']+'is a VALID email address!  Thank yoU!')
        return redirect('/success.html')
    else:
        print "error"
        for error in state['errors']:
            flash(error)
            return redirect('/')

@app.route('/success')
def show():
    query = "SELECT * FROM emails"
    emails = mysql.query_db(query)
    return render_template('success.html', all_emails = emails)




app.run(debug=True)
