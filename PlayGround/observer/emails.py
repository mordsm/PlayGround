import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging
import base64
from user import *
logger = logging.getLogger(__name__)
class Emails:
    def __init__(self):

        self.sender_email = "sharon.moshe@gmail.com"

    def send_mail(self, name_email, message_text):
        receiver = user.get_subscriber(name_email)


        if receiver == None:
            receiver=name_email
        message = MIMEText(message_text)

        #message = MIMEMultipart("alternative")
        message["Subject"] = "multipart test"
        message["From"] = self.sender_email
        message["To"] = receiver

        logger.debug('++++++++++++++++++++++++++++++++++')
        logger.debug(message)
        logger.debug('++++++++++++++++++++++++++++++++++')
        try:
            raw = base64.urlsafe_b64encode(message.encode('UTF-8')).decode('ascii')
        except Exception as e:
            logger.debug('---------------')
            logger.debug(e)
            logger.debug('---------------')

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            # server.login("sharon.moshe@gmail.com", "mordsmi4")
            result = None
            while result == None:
                try:
                    password = input("Type your password and press enter:")
                    result = server.login(self.sender_email, password)
                except UnicodeEncodeError:
                    print ("enter only english and numbers")
                except smtplib.SMTPAuthenticationError:
                    print("please check your password")
            server.sendmail(
                self.sender_email, receiver.email, message
            )


# receiver = input("Type the receiver name or his email:")
#emails = Emails()
#emails.send_mail("me", "testing")
