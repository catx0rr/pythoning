#!/usr/bin/python3

class Car:
    def __init__(self, model, year, color):
        """ Attributes """

        self.model = model
        self.year = year
        self.color = color

        """ Methods """

    def move(self):
        return f"{self.model} moved forward."


car = Car("Audi", 1993, "white")

print(f"Name: {car.model}\n" +
      f"Year: {car.year}\n" +
      f"Color: {car.color}\n" +
      car.move()
      )
