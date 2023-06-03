class Car:
    def __init__(self, model, color) -> None:
        self.model = model
        self.color = color
        print(f"My car's model is {model.title()} and the color is {color}")
my_car = Car('audi', 'dark')