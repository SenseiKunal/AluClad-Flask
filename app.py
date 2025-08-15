
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import smtplib
from email.mime.text import MIMEText
import os

app = Flask(__name__)

# Database Configuration (using SQLite for simplicity)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'contacts.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Model
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    mobile = db.Column(db.String(10), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Contact {self.name}>'

# Routes
@app.route('/')
def home():
    product_images = [
        'photo1.jpg', 'photo2.jpg', 'photo3.jpg', 'photo4.jpg',
        'photo5.jpg', 'photo6.jpg', 'photo7.jpg', 'photo8.jpg'
    ]
    return render_template('index.html', product_images=product_images)

@app.route('/modern-windows')
def modern_windows():
    return render_template('modern-windows.html')

@app.route('/office-door')
def office_door():
    return render_template('modern-windows.html')

@app.route('/hospital-window')
def hospital_window():
    return render_template('modern-windows.html')

@app.route('/commercial-window')
def commercial_window():
    return render_template('modern-windows.html')

@app.route('/retail-door')
def retail_door():
    return render_template('modern-windows.html')

@app.route('/industrial-window')
def industrial_window():
    return render_template('modern-windows.html')

# Contact Form Submission
@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        mobile = request.form['mobile']
        message = request.form['message']

        # Save to database
        new_contact = Contact(name=name, email=email, mobile=mobile, message=message)
        db.session.add(new_contact)
        db.session.commit()

        # Email configuration
        sender_email = "fightermankunal3@gmail.com"  # Replace with your email
        receiver_email = "www.ak4554@gmail.com"  # Replace with your email
        password = "vibc tfhc hqyz ekqv"  # Replace with your app password

        subject = "New Contact Form Submission"
        body = f"Name: {name}\nEmail: {email}\nMobile: {mobile}\nMessage: {message}"
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = receiver_email

        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, msg.as_string())
        except Exception as e:
            print(f"Failed to send email: {e}")

        return "Thank you! Your details have been saved and an email has been sent."

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)
