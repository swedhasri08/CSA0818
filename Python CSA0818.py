# to calculate square of a number
def sq(n):
    sqr = n**2
    return sqr
n = int(input("enter any integer : "))
a = sq(n)
print(a)

# to find maximum number between two
def max(n1 , n2):
    if n1>n2:
        return n1
    elif n1<n2:
        return n2
    else:
        return("Both are equal")
a=max(29 ,49)
print(a)
