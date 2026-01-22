#we must import our file_name
import math

#we must print the value with (math.we specify the equation we wanna calculate)
print(math.sqrt(16)) #racine carre
print(math.pi)  #pi
print(math.pow(3, 4)) #puissance
print(math.ceil(9.8)) #nombre qui vient apres 9
print(math.floor(9.8)) #avant 9
print(math.log10(100)) 



#an other way
from math import pi, sqrt, pow, floor, ceil, log, log10


print(pi)
print(sqrt(16))
print(pow(3, 4)) #puissance
print(floor(9.8)) #nombre qui vient apres 9
print(ceil(9.8)) #avant 9
print(log10(100)) 


#from math import *
#from math import pi as banana #means if i print banana it will give me the value of pi

ages=[20, 21, 4, 24, 23, 54, 64, 43]
for age in ages:
    print(age)
    
    #create a directory
    # OS module
    #import os
    #os.mkdir("xyz")
    
    import string

print(string.ascii_uppercase)
print(string.ascii_lowercase)
print(string.digits)
print(string.hexdigits)
print(string.printable)


import random
import math

#print numbers randomly
print(math.ceil(random.random() *100))

print(random.randint(5, 15)) #print num between 5 - 15
    

