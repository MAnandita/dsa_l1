class cat:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    
    def change_name(self, new_name):
        self.name = new_name

    def change_breed(self, new_breed):
        self.breed = new_breed

    def change_age(self, new_age):
        self.age = new_age

    def cat_info(self):
        print(f"Hello I'm a {self.breed} cat named {self.name}. I am {self.age} years old.")

lola = cat("Lola","American Shorthair",2)
lola.cat_info()
    
class ice_cream:
    def __init__(self, flavor, size, preference):
        self.flavor = flavor
        self.size = size
        self.preference = preference
    
    def change_flavor(self, new_flavor):
        self.flavor = new_flavor

    def change_size(self, new_size):
        self.size = new_size

    def change_preference(self, new_preference):
        self.preference = new_preference

    def order(self):
        print(f"Hello I want a {self.size} sized {self.flavor} ice cream in a {self.preference}.")

cookies_cream = ice_cream("cookies and cream","regular","cone")
cookies_cream.order()

