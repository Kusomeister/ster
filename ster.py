import math



def data_conv(tuple):
    x,z,theta = [float(i) for i in tuple]
    return (x, z,math.radians((theta%360)-90))


def linear(tuple): # z = x*tan(theta) + b
    x,z,theta = tuple               
    coeff = math.tan(theta) 
    lin =  (coeff, z-x*coeff) 
    return lin 

def c_lin(linear, x):
    a, b = linear
    return a*x + b


def intersection(linear1, linear2): #intersection of two linear functions
    a1, b1 = linear1
    a2, b2 = linear2
    numerator = b2-b1
    denominator = a1-a2
    x = numerator/denominator
    z = c_lin(linear1,x)
    return (x, z) 
x1 = input("First measuring point x coordinate: ")
z1 = input("First measuring point z coordinate: ")
t1 = input("First measuring point angle: ")

x2 = input("Second measuring point x coordinate: ")
z2 = input("Second measuring point z coordinate: ")
t2 = input("Second measuring point angle: ")

xs, zs = [str(i) for i in intersection(linear(data_conv((x1,z1,t1))),linear(data_conv((x2,z2,t2))))]

print("\n\nNearest stronghold is at x: "+xs+", z: "+zs)
