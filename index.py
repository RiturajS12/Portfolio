from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb+srv://Textovert:Kyundu17@textovert.uzlevw3.mongodb.net/')
db = client['upflairs'] 
collection = db['queries']  

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
    
    collection.insert_one({'name': name, 'message': message})
    
    return redirect(url_for('contact'))

if __name__ == '__main__':
    app.run(debug=True)
