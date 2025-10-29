# sum of digit
num = int(input("enter any number :"))
sum = 0
temp = num
while temp>0:
    digit=temp%10
    sum+=digit
    temp=temp//10
print("Sum of digits : " , sum)

# Armstrong Number
n=int(input("enter any number : "))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=n**3
    temp=temp//10
if sum==num:
    print("yes , it is an armstrong number")
else:
    print("no . it is not an armstrong number")

# to check a perfect number
n=int(input("enter any Number : "))
sum=0
for i in range(1,n):
    if(n%i==0):
        sum=sum+i
if (sum==n):
    print("It is perfect number")
else:
    print("not a perfect number ")

# to find factors of a number
x = int(input("enter any number :"))
y=[]
print("The factors of " , x , "are :")
for i in range(1,x):
    if x%i==0:
        y.append(i)
print(y)
print(" Number of factors are " , len(y))
