import supply
from MyTraining import *
#import Pen

paper = supply.Supply('Xerox', 0)
red_pen = supply.Pen('Bic', 0.99)

red_pen.pen_color = "red"

print (red_pen.brand, red_pen.cost)
print (red_pen.pen_color)

print (paper.cost)

price = paper.price_calculator()
print(price)

print(Module3.some_function3("karen", "austin"))