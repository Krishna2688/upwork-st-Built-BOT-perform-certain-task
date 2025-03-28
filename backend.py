from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
import os
# from twilio.rest import Client

app = Flask(__name__)
CORS(app)

@app.route('/send_email', methods=['POST'])
def send_email():
    data = request.json

    sender = data["user_email"]
    password = data["password"]
    cc = data["cc"]
    company_name = data["company_name"]
    ref_id = data["ref_id"]
    recipient = data["recipient"]

    subject = f"Your Request (Ref: {ref_id})"

    # Mail Merge
    message = f"""
        Dear {company_name},

        This is an automated message regarding your request with Reference ID: {ref_id}.

        Thank you,
        AI Email Bot
        """

    smtp_host = "smtp.gmail.com"
    smtp_port = 587

    # Create the email content
    msg = MIMEText(f"{message}")
    msg['Subject'] = subject
    msg['From'] = sender
    msg["Cc"] = cc
    msg['To'] = recipient

    try:
        # Send the email
        with smtplib.SMTP(smtp_host, smtp_port) as server:  # Replace with your SMTP server
            server.starttls()
            server.login(sender, password)  # Replace with your email password
            server.send_message(msg)
        return jsonify({"Status":"Message sent successfully!"}), 201
    except Exception as e:
        return jsonify({"Status":f"Failed to send message: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
