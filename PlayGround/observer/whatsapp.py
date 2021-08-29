import pywhatkit
import datetime
from user import user


def send_whatsapp( name, message_text,hour=None,minute=None):
    if hour is None:
        now = datetime.datetime.now()
        if now.minute <= 57:
            hour = now.hour
            minute = now.minute+2
        else:
            hour = now.hour +1
            minute = 0

    #user = User()
    subscriber = user.get_subscriber(name)
    pywhatkit.sendwhatmsg("+"+subscriber.phone, message_text, hour, minute,wait_time=0)

