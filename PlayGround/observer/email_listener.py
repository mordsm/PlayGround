from observer import *


email = Emails()
def handle_event1():
    email.send_mail("me","event1 has occurred")
def handle_event2():
    email.send_mail("me","event2 has occurred")

def setup_email_event_handlers():
    subscribe("event1",handle_event1)
    subscribe("event2", handle_event2)