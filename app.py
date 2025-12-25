from flask import Flask, render_template, request
import random
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# 🔐 Gmail credentials
SENDER_EMAIL = "krushnacsahu2002@gmail.com"
APP_PASSWORD = "eguq bngj gzpd jrzf"

def send_otp(receiver_email, otp):
    msg = MIMEText(f"Your OTP is: {otp}\n\nThis OTP is valid for 5 minutes.")
    msg["Subject"] = "Your OTP Code"
    msg["From"] = SENDER_EMAIL
    msg["To"] = receiver_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.send_message(msg)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        email = request.form["email"]
        otp = random.randint(100000, 999999)

        try:
            send_otp(email, otp)
            message = "✅ OTP sent successfully! Check your email."
        except Exception as e:
            message = "❌ Failed to send OTP. Try again."

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
