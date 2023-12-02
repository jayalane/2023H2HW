
import math

for x in range(-16, 16, 1):
    th = x / 4 * 3.1415926535
    if x == 0:
        print (x / 4, 1)
    else:
        print (x / 4, math.sin(th) / th)
    

