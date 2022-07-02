from flask import Flask, render_template, request
from flask_mail import Mail, Message
from config import mail_username, mail_password


app = Flask(__name__)

app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = mail_username
app.config['MAIL_PASSWORD'] = mail_password


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
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        msg = Message(subject=f"Mail from {fname} {lname}", body=f"Name : {fname} {lname}\nEmail : {email}\nPhone : {phone}\nMessage : {message}", sender=mail_username, recipients=['tejasprojects123@gmail.com'])
        print(msg)
        mail.send(msg)
        return render_template('contact.html', failed=True)

    return render_template('contact.html')

    
if __name__ == '__main__':
   app.run(debug = True)