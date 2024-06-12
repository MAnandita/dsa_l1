#Object Oriented Programming

#Class - blueprint of an object
#Object - an occurance/use of the blueprint

class fruit:
    def __init__(self, color, taste, shape, preference):
        self.color = color
        self.taste = taste
        self.shape = shape
        self.preference = preference

    def get_shape(self):
        return self.shape
    
    def increase_preference(self):
        self.preference += 1

    def set_shape(self, new_shape):
        self.shape = new_shape
    
    def show_fruit(self):
        print(f"Hello, I am a fruit that is {self.color}, {self.shape}, {self.taste}, and {self.preference}.")

strawberry = fruit("red", "sweet", "oblate", 8)
strawberry.show_fruit()
strawberry.set_shape("round")
print(strawberry.get_shape())

mango = fruit("orange","sweet","oval",6)
mango.show_fruit()


