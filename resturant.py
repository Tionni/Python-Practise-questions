class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant + "offers " + self.cuisine_type + " cuisine")

    def open_resteurant(self):
        print(self.restaurant + " restaurant is open")

r1 = Restaurant("Qwetu", "italian" )
r1.describe_restaurant()
r1.open_resteurant()
   