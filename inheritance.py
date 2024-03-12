class Animal():
    def animals(self):
        print("can breath")

    def fish(self):
        print("swims under water")

    def monkey(self):
        print("can smell")

    def tiger(self):
        print("can run")

class Human(Animal):
    def pp(self):
        print("pp lives kwa kichaka")

h = Human()

print(h.monkey())