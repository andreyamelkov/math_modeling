import numpy as np
from lab3ex1 import g
import lab3ex1
import math
a=np.pi/3
h=100
#np.tan(30)
B_deg=30
B_rad=np.radians(B_deg)

a=g*h*((np.tan(B_rad))**2)
b=2*((np.cos(a)**2))
c=1-(np.tan(B_rad)*(np.tan(a)))
d=(a/(b*c))**(1/2)

print(d)
 

 