from email import message
from flask import Flask, render_template, request
from flask_mail import Mail, Message
from config import mail_username, mail_passwoerd


app = Flask(__name__)

app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = mail_username
app.config['MAIL_password'] = mail_passwoerd


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
        message = "sent message"
    return render_template('contact.html')
if __name__ == '__main__':
   app.run(debug = True)