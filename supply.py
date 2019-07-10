class Supply:

    def __init__(self, brand, cost):
        self.brand = brand
        self.cost = cost

    def price_calculator (self):
        try:
            price = self.cost * 2.5
            price = price / price
        except:

            print('Price = zero.')
        return self.cost * 2.5

class Pen(Supply):
    def special_function(self):
        self.pen_color = "blue"

if (__name__ == '__main__'):
    first_supply = Supply("Steno", 1.59)

    print(first_supply.brand)

    next_supply = Pen("Bic", .15)
    next_supply.pen_color = "orange"

    print(next_supply.brand, next_supply.pen_color)