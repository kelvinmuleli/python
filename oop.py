"object oriented programming"
class People:
    def __init__(self,name,age,email,password):
        self.name = name
        self.age = age
        self.email = email
        self.password = password

person1 = People("nyali", 14,"tuma1@gmail.com","5947")
person2 = People("tobius",13,"jiomo1@gmail.com""1235")

print("hi, my name is",{person1.name})