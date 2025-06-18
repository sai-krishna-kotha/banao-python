import json
import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os
load_dotenv()

def send_email(event, context):
    try:
        # print("Event received:", event)
        body = json.loads(event['body'])
        # print("Parsed body:", body)

        receiver_email = body['receiver_email']
        subject = body['subject']
        body_text = body['body_text']

        if not receiver_email or not subject or not body_text:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing required fields"})
            }

        print("Preparing email...")

        # Creating email
        msg = EmailMessage()
        msg.set_content(body_text)
        msg['Subject'] = subject
        msg['From'] = "Sai Krishna Kotha"
        msg['To'] = receiver_email


        sender_email = os.environ.get("EMAIL")
        password = os.environ.get("EMAIL_PASSWORD")
        # print(f"This is my email :{sender_email}")
        # print(f"This is my password :{password}")
        
        print("Connecting to SMTP...")

        # Connecting to SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)

        print("Email sent!")

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Email sent successfully!"})
        }

    except Exception as e:
        print("Error occurred:", str(e))
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }