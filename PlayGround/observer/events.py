from observer import *


if __name__ == "__main__":


    subscribe("event1",email.send_mail)
    post_event("event1","testing2")