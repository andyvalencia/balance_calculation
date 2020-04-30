# import math

# def trigfuncs(angle):
#     radians = math.radians(angle)
#     rsin = math.sin(radians)
#     rcos = math.cos(radians)
#     rtan = math.tan(radians)
#     return (math.degrees(rsin), math.degrees(rcos), math.degrees(rtan))

# def main():
#     angle = int(input('Enter an angle value: '))
#     print(trigfuncs(angle))
    
# main()

# #math.acos(x) returns the arc cosine of x in radians
# #same for ''asine(x) ''atan(x)'''

# #test number 2, just to calculate the sin of an angle

# def trigfuncs(angle) :
#     radians = math.radians(angle)
#     rsin = math.sin(radians)
#     return (math.degrees(rsin))

# def main():
#     angle = int(input('Enter an angle value: '))
#     print(trigfuncs(angle))

# main()

# #this is try number 3

# import math
# rsin = math.radians(a)
# a = int(input())


# print(math.sin(rsin)



import math

def radian_to_degree(radian):
    return (radian*180)/math.pi


def trigfuncs(angle):
    radians = math.radians(angle)
    rsin = math.sin(radians)
    rcos = math.cos(radians)
    rtan = math.tan(radians)
    print("With an Angle of %f degrees you return a sine of %f radians - cosine of %f radians - and tangent of %f radians" % (angle, rsin, rcos, rtan))
    return (radian_to_degree(rsin), radian_to_degree(rcos), radian_to_degree(rtan))

def main():
    angle = float(input('Enter an angle value: '))
    print(trigfuncs(angle))



main()