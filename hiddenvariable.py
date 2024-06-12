class user:
    #if you make a variable outside of the init but with one underscore, you can access 
    #it directly through objects
    _password = "AM123"

    #if you make a variable outside of the init but with 2 underscores,
    #you can't access it directly though objects
    #to access it, you need to access it from within the class

    __password = "AM123"

    def __init__(self, name, email, username):
        self.name = name
        self.email = email
        self.username = username
    
    def get_password(self):
        return self.__password

millie = user("Millie","millieb@gmail.com","MillieB")
print(millie.get_password())
#accessable
print(millie._password)
#not accessable
#print(millie.__password)