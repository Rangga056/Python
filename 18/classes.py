class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print("Moving...")

    def get_make_model(self):
        print(f"I'm a {self.make} and {self.model}")


my_car = Vehicle("Tesla", "Model 2")

my_car.moves()
my_car.get_make_model()

your_car = Vehicle("Corvete", "Viper")
your_car.get_make_model()
your_car.moves()

# INHERITANCE #


class Airplane(Vehicle):
    def __init__(self,  make, model, faa_id):
        super().__init__(make, model)  # this will inherit the previous __init__ method
        self.faa_id = faa_id

    def moves(self):
        print("Flies along..")


class Truck(Vehicle):
    def moves(self):
        print("Rumbles along..")


class GolfCart(Vehicle):
    pass  # This will inherit everything from the Vehicle class


cessna = Airplane("Cessna", "Skyhawk", "F-911")
truck = Truck("Mack", "Pinacle")
golfwagon = GolfCart("Yamaha", "JC111")

cessna.get_make_model()
truck.get_make_model()
golfwagon.get_make_model()

print("\n\n")

for v in (my_car, your_car, cessna, truck, golfwagon):
    v.get_make_model()
    v.moves()
