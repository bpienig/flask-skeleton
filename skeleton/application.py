from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def default():
    return render_template('index.html')

@app.route('/docs')
def skeleton():
    return render_template('skeleton.html')
	
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)