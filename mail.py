from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER'] = 'smtp-relay.brevo.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = '' #enter your smtp mail id here
app.config['MAIL_PASSWORD'] = '' #enter password here
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

@app.route("/")
def index():
    msg = Message('Hello', sender = '', recipients = [''] )
    msg.body = "Hello Flask! This is a test email sent from Flask-Mail."
    mail.send(msg)
    return "Sent successfully"

if __name__ == '__main__':
    app.run(debug = True)