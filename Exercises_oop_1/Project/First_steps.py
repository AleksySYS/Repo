class Vehicle:
    
    
    def __init__(self):
        self.color()
        self.mark()
        self.type_of_car()

    def color(self):
        self.color = "Brown"
        print(f'Color of vehicle is: {self.color}')
        
    def mark(self):
        self.mark = "Audi"
        print(f'Mark of this car is: {self.mark}')
        
    def type_of_car(self):
        self.type_of_car = "Hatchback"
        print(f'Type of the car is: {self.type_of_car}')
        
Vehicle()
    