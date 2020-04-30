import math 

'''tension_string = float(61.0) 
object_mass = input(6) #this time we choose 6    #mass of object in kg
g =  9.8        #gravity constant to 1 d.c
object_weight = int(rod_mass) * g
#possible angles to choose: 40, 60, 90
angle_chosen = input (40) #40 degrees
midpoint_of_object = input(3) #meters
length_of_object = input(6) #meters'''

""" 
this project should work for when you want to test if an object attached to a wall and a string will be in equilibrum, you add the values
and the code will work it out for you

"""
print('please put the mass of your object')
    input() #value to be stored as object_mass

print('please input the lentgh of your object')
    input() #this value stored as length_of_object

print('now please put the angle at which the object is at')
    input() #this value should be stored as midpoint_of_object

#MAYBE IN HERE ADD A DELAY (SHOW THAT THE 'MACHINE IS THINKING')

def momentum_vertical():
    """calculate the weight of the rod"""
    def rod_weight(): 
        math.multiply(float(rod_mass * g))
        return value
    rod_weight()
    return float(rod_weight()) #outcome


def momentum_horizontal():
    """ This calculated horizontal momentum with the equation below (calculate 3*tension*sin(angle))"""
    def angle():
        calculate math.sin(angle_chosen)
        return float(math.sin(angle_chosen()))

    calculate midpoint_of_object()*tension_string()*angle()
    return value 
    


if momentum_vertical() == momentum_horizontal:
    print('The object will be in equilibrium')
elif print('The object will not be in euqilibrium and it will fall')    
