#ACTIVITIES OF LAB1
#Number is even or odd
n=input("Enter a number")
if int(n)%2==0:
    print("The number is even")
else:
    print("The number is odd")
   
#Accept integers until 10 and then sum
sum=0
s=input("Enter an integer")
n=int (s)
while n!=0:
    sum=sum+n
    s=input("Enter an integer")
    n=int(s)
print("Sum of given integers is",sum)

#Whether the number is prime or not
isPrime=True
i=2
n=int(input("Enter a Number"))
while i<n:
    remainder=n%i
    if remainder==0:
        isPrime=False
        break
    else:
        i=i+1
if isPrime:
    print("number is Prime")
else:
    print("Number is not Prime")

#five integer values and there sum
sum=0
i=0
while i<=4:
    s=input("Enter a number")
    n=int(s)
    sum=sum+n
    i=i+1
print("sum is",sum)

#Sum of all values between 0 & 10 using while loop
sum=0
i=1
while i<=10:
    sum=sum+i
    i=i+1
print("sum is",sum)

#Input from the keyboard
name=input("What is your name")
print("Hello"+ (" ")+name)

job=input("What is your job")
print("Your job is"+" "+job)

num=input("Give me a number")
print("You said"+" "+(num))

#Guessing game
import random

min=1
max=9
number=random.randint(min,max)
guess=None
another=None
TRY=0
running=True
print("alright")

while running:
    guess=input("What is your lucky number")
    if int(guess)<number:
        print("Wrong,too low")
    elif int(guess)>number:
        print("Wrong,too high")
    elif guess.lower()=="exit":
        print("Better luck next time")
    elif int(guess)==number:
        print("Yes, that's the one, %s." %number)
        if TRY<2:
            print("Impressive , only %s tries." %TRY)
        elif TRY>2 & TRY<10:
            print("Pretty good, %s tries." %TRY)
        else:
            print("Bad, %s tries." %TRY)
        running=False
    TRY=+1

#LAB TASKS

#reversing a number
n=int(input("Enter an integer"))
rev_no=0
while (n>0):
    remainder=n%10
    rev_no=(rev_no*10)+remainder
    n=n//10
print("The reversed number is"+ " "+format(rev_no))

#finding factorial of a number
n=int(input("Enter a number"))
fac=1
i=1
while i<=n:
    fac=fac*i
    i=i+1
print("Factorial of",n,"is" ,fac)

#Marks of Students
n = int(input('Enter a marks of student:'))
if n>100 or n<0:
    print('invalid input')
else:
    if n<50:
        print("You Got F Grade, Better luck next time:",n)
    elif n>50 and n<60:
        print("Your Grade is E, Improvement suggested",n)
    elif n>61 and n<70:
        print("D is your Grade",n)
    elif n>71 and n<80:
        print("C is your Grade",n)
    elif n>81 and n<90:
        print("Your Grade is B,Good",n)
    elif n>91 and n<100:
        print("Your Scored a Great Deal, Excelent",n)

#Set of integers and their sum
n=int(input("enter numbers to add : "))
even=0
odd=0

for num in range(1,n+1):
    n=int(input("enter the values : "))
    if(num%2==0):
        even=even+num
    else:
       odd=odd+num

print("total of even numbers=",even)
print("total of odd numbers=",odd)

#Fibonacci Series
n=int(input("enter the terms : "))
fe=0
se=1
if n<0:
    print("enter positive values")
else:
    print(fe,se,end="")
for x in range(2,n):
    next=fe+se
    print(next,end="")
    fe=se
    se=next



























        
