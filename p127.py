from Rectangle import *
from Triangle import *

rect = Rectangle()
trey = Triangle()

rect.set_values(40, 50)
print('Initial Rec Area:', rect.area())
trey.set_values(4, 5)

print('Rectangle Area after class property overwritten by Triangle:', rect.area())
print('Triangle Area:', trey.area())
