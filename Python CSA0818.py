# to find square and cube of a number
a = eval(input("enter a number : "))
square = a*a
cube = a*a*a
print("Square and Cube of number are " , square , cube)

# program to find area of circle
r = eval(input("enter value of radius: "))
Ar = 3.14*r**2
print("Area of circle is " , Ar)

# program to find Simple Interest value
p = eval(input("enter the principle value: "))
r = eval(input("enter the rate of interest: "))
t = eval(input("enter the time of period: "))
SI = (p*r*t)/100
print(" The value of simple interest " , SI)

#to swap two numbers
a = int(input("enter any integer : "))
b = int(input("enter another integer : "))
a,b=b,a
print( " here are the swapped numbers " ,a,b)


