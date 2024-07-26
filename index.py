from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

mongodb_uri = 'mongodb+srv://your_collectionname:your_pass@textovert.uzlevw3.mongodb.net/upflairs?retryWrites=true&w=majority'

client = MongoClient(mongodb_uri, serverSelectionTimeoutMS=5000)
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
    app.run(port='5050',debug=True)
