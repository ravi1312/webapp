from flask import Flask
from flask import render_template, redirect, request, url_for, flash,abort
app = Flask(__name__,template_folder='templates')

@app.route('/')
def hello_world():
        return render_template('home.html')
@app.route('/payment')
def base():
    return render_template('payment.html')
if __name__ == "__main__":
        app.run(host='0.0.0.0',port=8080)


