import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import session

class OTP:
    def __init__(self, receiver_email):
        self.email = receiver_email
        self.otp = self.__generate_otp()
    def __generate_otp(self, length=6):
        """Generate a 6-digit OTP code"""
        digits = "0123456789"
        otp = ''.join(random.choice(digits) for _ in range(length))
        return otp
    def send_otp_email(self):
        """Send OTP code to the specified email address."""
        try:
            sender_email = "your_email@gmail.com"
            sender_password = "your_password"

            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = self.email
            msg['Subject'] = "Your OTP Code"

            # Email body
            body = f"Your OTP code is: {self.OTP}"
            msg.attach(MIMEText(body, 'plain'))

            # Connect to Gmail's SMTP server
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()  # Start TLS encryption
            server.login(sender_email, sender_password)  # Login to the email account

            # Send email
            text = msg.as_string()
            server.sendmail(sender_email, self.email, text)
            server.quit()
            session[self.email] = {'otp': self.otp}
            print("OTP sent successfully!")

        except Exception as e:
            print(f"Failed to send email: {e}")
    def verify_otp(self, email_user, user_otp):
        # Retrieve OTP from session
        generated_otp = session.get(email_user, {}).get('otp')

        # Compare OTPs
        if user_otp == generated_otp:
            return True
        else:
            return False