from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'your_username_of_pythonanywhere.mysql.pythonanywhere-services.com'
app.config['MYSQL_USER'] = 'your_username_of_pythonanywhere'
app.config['MYSQL_PASSWORD'] = 'your_db_password'
app.config['MYSQL_DB'] = 'your_username_of_pythonanywhere$default'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/certificates')
def certificates():
    return render_template('certificate.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/messages', methods=['POST'])
def submit_review():
    name = request.form['name']
    message = request.form['message']

    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute('INSERT INTO queries (name, message) VALUES (%s, %s)', (name, message))
    conn.commit()
    cursor.close()

    return redirect(url_for('contact'))

if __name__ == '__main__':
    app.run(debug=True)
