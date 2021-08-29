from observer import *
from whatsapp import *


def handle_event1(data):
    send_whatsapp("me", "event1 has occurred")


def setup_whatsapp_event_handlers():
    subscribe("event1", handle_event1)


setup_whatsapp_event_handlers()
post_event("event1", "testing")
