from flask import Flask, render_template, request
from flask_mail import Mail, Message


app = Flask(__name__)

mail = Mail(app)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method == "POST":
        return "Sent Message"
    return render_template('contact.html')


if __name__ == '__main__':
   app.run(debug = True)