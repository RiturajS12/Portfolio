from flask import Flask,render_template

app = Flask(__name__)


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
    
def handler(request):
    return app(request)
