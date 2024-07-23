from flask import Flask
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# Set configuration parameters
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

# Initialize Flask-Mail
mail = Mail(app)

@app.route('/')
def index():
    try:
        msg = Message('Hello', sender='nanjilad@gmail.com', recipients=['nanjiladavid2@gmail.com'])
        msg.body = "Hello Flask! This message is sent from Flask-Mail"
        mail.send(msg)
        return 'Message sent'
    except Exception as e:
        return f'An error occurred: {e}'

if __name__ == '__main__':
    app.run(port=4000, debug=True)