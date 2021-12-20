from flask import Flask
from flask import render_template, redirect, request, url_for, flash,abort
app = Flask(__name__,template_folder='templates')

@app.route('/')
def hello_world():
        return render_template('flipkart2.html')
@app.route('/mobiles')
def mobiles():
    return render_template('mobile2.html')
@app.route('/payment')
def payment():
    return render_template('payment2.html')
if __name__ == "__main__":
        app.run(host='0.0.0.0',port=8080)
