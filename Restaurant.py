class Restaurant: # created a class named Restaurant
    def __init__(self, restaurant_name, cuisine_type) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self): # created a method describe_restaurant
        print(f"My restaurant name is {self.restaurant_name.title()} and the cuisine type is {self.cuisine_type}.")
    
    def open_restaurant(self): # created another method named open_restaurant
        print(self.restaurant_name.title(), "is opened.")
    
restaurant = Restaurant('neon', 'club')
restaurant.describe_restaurant()
restaurant.open_restaurant()