users = {"ofra": {"email":"ofrasharon1@gmail.com","phone":"972544646526"},
         "shmuel": {"email":"shmuel.sharon@gmail.com","phone":"972543246462"},
                           "david": {"email":"shdavid10@gmail.com","phone":"972506562311"},
                           "me": {"email":"sharon.moshe@gmail.com","phone":"972506562311"}}

class User():
    def __init__(self,name,phone,email):
        self.name = name
        self.phone = phone
        self.email = email
        self.subscribers = []

    def get_subscriber(self,name):
        for subscriber in self.subscribers:
            if subscriber.name == name:
                return subscriber
for key,value in users.items():
    user = User(key,value["phone"],value["email"])
    user.subscribers.append(user)







