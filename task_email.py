import streamlit as st
import requests
import json, os
import csv
import smtplib
from email.mime.text import MIMEText


def send_email(data):

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
        return "SUCCESS"
    except Exception as e:
        return "FAILED"

# Streamlit UI
st.title("📧 Email Bot")

# User Login
email = st.text_input("Enter your email to log in:")
password = st.text_input("Password", type="password")
if email:
    st.session_state["user_email"] = email
if password:
    st.session_state["password"] = password

# File to store conversations persistently
CONVERSATION_FILE = "email.csv"

# Email Input Form
recipient = st.text_input("Recipient Email")
cc_email = st.text_input("CC Email (optional)")
company_name = st.text_input("Company Name")
ref_id = st.text_input("Reference ID")
attachment = st.file_uploader("Upload Attachment (Optional)", type=["pdf", "docx", "png", "jpg"])

st.session_state["recipient"] = recipient
st.session_state["cc_email"] = cc_email
st.session_state["company_name"] = company_name
st.session_state["ref_id"] = ref_id

if st.button("Send Email"):
    with st.spinner():
            files = {"attachment": attachment.getvalue()} if attachment else {}
            data = {
                "user_email": st.session_state["user_email"],
                "password": st.session_state["password"],
                "recipient": st.session_state["recipient"],
                "cc": st.session_state["cc_email"],
                "company_name": st.session_state["company_name"],
                "ref_id": st.session_state["ref_id"],
            }
            #with st.echo():
            #    st.write(data)

            #headers = {'Content-Type': 'application/json'}

            #response = requests.post(url="http://192.168.1.182:8080/send_email", data=json.dumps(data), headers=headers, verify=False)

            response = send_email(data)


            if response == "SUCCESS":
                st.success("Email sent successfully!")
                data["status"] = "SUCCESS"
            else:
                st.error("Failed to send email.")
                data["status"] = "FAILED"

            data.pop("password")
            st.session_state["data"] = data

            # Persist conversations to file
            if os.path.exists(CONVERSATION_FILE):
                with open(CONVERSATION_FILE, "a") as f:
                    # fieldnames = ['user_email', 'recipient', 'cc', 'company_name', 'ref_id', 'status']
                    writer = csv.writer(f)
                    # writer.writerows(st.session_state["data"].keys())
                    writer.writerow(st.session_state["data"].values())
            else:
                with open(CONVERSATION_FILE, "w", newline='') as f:
                        # fieldnames = ['user_email', 'recipient', 'cc', 'company_name', 'ref_id', 'status']
                        writer = csv.writer(f)
                        writer.writerow(st.session_state["data"].keys())
                        writer.writerow(st.session_state["data"].values())
# # View Sent Emails
# if st.button("View Sent Emails"):
#     response = requests.get(f"http://127.0.0.1:8000/sent_emails?user_email={email}")
#     if response.status_code == 200:
#         emails = response.json()
#         for email in emails:
#             st.write(email)
#     else:
#         st.error("Could not fetch emails.")
