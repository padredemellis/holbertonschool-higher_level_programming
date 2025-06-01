class FlyMixin:
    def fly(self):
        print("The creature flies!")

class SwimMixin:
    def swim(self):
        print("The creature swims!")

class Dragon(FlyMixin, SwimMixin):
    def roar(self):
        print("The dragon roars!")

chimuelo = Dragon()

chimuelo.swim()
chimuelo.fly()
chimuelo.roar()
