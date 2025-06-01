class Fish:
    def swim(self):
        print("The fish is swimming")
    def habitat(self):
        print("The fish lives in water")

class Bird:
    def fly(self):
        print("The bird is flying")
    def habitat(self):
        print("The bird lives in the sky")

class FlyingFish(Bird, Fish):
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print ("The flying fish is swimming!")
    
    def habitat(self):
        print("The flying fish lives both in water and the sky!")

pez_volador = FlyingFish()

pez_volador.swim()
pez_volador.fly()
pez_volador.habitat()

print(FlyingFish.mro())
