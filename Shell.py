# https://1drv.ms/u/s!AhRsWP77xvhXgn7YdnL7ZveDWyVe
import time, random
a = """
t = "h"
if t == "t":
    print("The t value has a value of t")
elif t == "g":
    print("The t value has a value of g")
elif t == "g":
    print("The t value has a value of g")
elif t == "h":
    print("The t value has a value of g")
else:
    print("")

q = int(input("Enter a number"))
if q == 1:
    print("Monday")
elif q == 2:
    print("Tuesday")
elif q == 3:
    print("Wednesday")
elif q == 4:
    print("Thursday")
elif q == 5:
    print("Friday")
elif q == 6:
    print("Saturday")
elif q == 7:
    print("Sunday")
else:
    print("Number out of 1-7")

q = int(input("Enter a number"))
if q % 2 == 0:
    print("Even number")
else:
    print("Odd number")

q2 = int(input("Enter a 3-Digit Number: "))
if q2 >= 100:
    if q2 % 3 == 0:
        print("Divisible by 3")
    else:
        print("Not Divisble by 3")
q3 = int(input("Enter a number: "))
q4 = int(input("Enter a number: "))
q5 = int(input("Enter a number: "))
if not q3 == q4 and not q3 == q5:
    print("Integers are unique.")
else:
    print("Integers are not unique.")
    
days = int(input("How many days will you be at the hotel: "))
daycost = 75
dayfoodcost = int(input("Daily food cost: "))
activitycost = int(input("How much will the activities cost: "))
totalcost = (dayfoodcost+activitycost+daycost)*days
print("Total cost: {}$".format(totalcost))

height = int(input("Please enter your height (only numbers)"))
weight = int(input("Please enter your weight (only numbers)"))
bmi = weight / (height ** 2)
print("Your BMI is: {}.".format(bmi))

q = input("Enter a 2-digit or 3-digit number")

if q >= 10 and q <= 99:
    print("2-digit number")
elif q >= 100 and q <= 999:
    print("3-digit number")
else:
    print("Out of range.")

num = int(input("Enter a number: "))
num1 = int(input("Enter a number: "))

if num % 7 == 0 and num1 % 7 == 0:
    print("Both multiples of 7")
else:
    print("Not multiples of 7")

num = int(input("Enter a number: "))

if num >= 100 and num <= 999:
    if num % 3 == 0:
        print("3-digit number divisible by 3")
    else:
        print("3-digit")
else:
    print("Not 3-digit")
    
cre = int(input("How many credits do you have: "))

if cre >= 120:
    print("You have enough credits to graduate!")
else:
    print("You don't have enough credits to graduate. :(")

price=int(input("Enter price: "))

if price >= 2000:
    print(price/5)
elif price >= 2001 and price <= 5000:
    print(price/25)
elif price >= 5001 and price <= 10000:
    print(price/35)
elif price > 10000:
    print(price/50)
else:
    print(price)

marks = int(input("Enter you marks: "))

if marks >= 90 and marks <= 100:
    print("You got an A!")
elif marks >= 70 and marks <= 89:
    print("You got a B!")
elif marks >= 50 and marks <= 69:
    print("You got a C.")
elif marks > 30 and marks <= 49:
    print("You got a D.")
elif marks <= 30:
    print("You got an F :(")
else:
    print("Invalid value: {}(out of range)".format(marks))

price=int(input("Enter price: "))

if price <= 2000:
    dsc = 5
elif price >= 2001 and price <= 5000:
    dsc = 25
elif price >= 5001 and price <= 10000:
    dsc = 35
elif price > 10000:
    dsc = 50
final = price-(price*(dsc/100))
print("You will pay {} pounds".format())

energy = int(input("Enter how much energy you use: "))
if energy <= 100:
    cost = 2
elif energy > 100 and energy <= 200:
    cost = 1.8
elif energy > 200:
    cost = 1.5

print("You will pay: {} pounds in energy bills".format(price))

days = int(input("How many days have you taken your book out of the library? "))

if days >= 5:
    cost = 40
elif days >= 6 and days <= 10:
    cost = 65
elif days > 10:
    cost = 80
    
final = days*cost/100
print("You will have to pay: {} pound(s)".format(final))

num = int(input("Enter a number: "))

if num >= 10000 and num <= 99999:
    print("Number is 5-digit")
    divided=num//100
    print("Middle digit is: {}.".format(divided%10))
else:
    print("Number is not 5-digit :(")

num0 = int(input("Enter a number:"))
if num0 >= 1000 and num0 < 10000:
    print("4-digit Number.")
    firstdigit = num0//1000
    lst = num0//10*10
    lst2 = num0
    lastdigit = lst2 - lst
    print("Sum of first and last digits {}.".format(firstdigit+lastdigit))
else:
    print("Not a 4-digit number.")
num1 = int(input("Enter another number: "))
if num1 >= 100 and num1 < 1000:
    firstdigit = num1//100
    lst = num1//10*10
    lst2 = num1
    lastdigit = lst2 - lst
    su = firstdigit+lastdigit
    if su % 2 == 0:
        print("Sum of first and last digits is even.")
    else:
        print("Sum is not even.")
else:
    print("Number is not 3-digit")

waterconsumed = int(input("How many gallons of water do you use? "))

if waterconsumed <= 45:
    tax = 1
elif waterconsumed > 45 and waterconsumed <= 75:
    tax = 475
elif waterconsumed > 75 and  waterconsumed <= 125:
    tax = 750
elif waterconsumed > 125 and waterconsumed <= 125:
    tax = 1125
elif waterconsumed > 200 and waterconsumed <= 350:
    tax = 1650
else:
    tax = 2000

print("You have to pay {} in water taxes.".format(waterconsumed/100*tax))

import os
def getdirs(directory):
    sub_folders = {}
    for dir, files, sub_dirs in os.walk(str(directory)):
        sub_folders[str(dir)] = str(files)
    return sub_folders
results = getdirs()
print(results)
q = input("search dirs")
values = []
def searchdict(search,lib)
    values = []
    showtext = ""
    found = False
    for value in lib.values():
        low = value.lower()
        if q.find(value):
            if not value in values:
                values.append(value)
                found=True
        if q.find(low):
            if not value in values:
                values.append(value)
                found=True
      if not found:
          return ()
print(values)

age = int(input("What's your age? "))                                                                              
print("That's cool.")

itemsinstock = ["BrickStock","AppleStock","PlaneStock"]
order = input("What are you going to buy? ")
if order in itemsinstock:
    num = int(input("How many are you going to buy? "))
    if 100-num < 0:
        itemsinstock.remove(order)
        print("Sorry, we only have 100 {}' in store we will dispatch and deliver you all the ones avaliable and will deliver the rest when {} is in stock.".format(order,order))
    else:
        print("Dispatching order... {} left...".format(100-num))
else:
    print("Sorry we dont seem to have {}.".format(order))

answer = "Moscow"
ans = input("What is the capital of Russia? ")
if ans == answer:
    print("Correct!")
else:
    print("Oops, incorrect here is a clue: ")
    ans = input("Here is a clue: It has a famous Colorful Cathedral: ")
    if ans == answer:
        print("Correct!")
    else:
        print("Oops, here is another clue: ")
        ans = input("It is in the west of the country: ")
        if ans == answer:
            print("Correct!!!")
        else:
            print("Sorry, last chance and last clue: ")
            ans = input("Some of it's roads are made of bricks: ")
            if ans == answer:
                print("Correct, just in time.")
            else:
                print("You lose :(")

stock = 100
num = int(input("How many are you going to buy"))
if num > stock:
    print("Unfortunately we only have {} items in stock, (you ordered {} items) we will dispatch you the rest of the items ({}) when they are availble ".format(stock,num,num-stock))
    stock = 0
    print("{} items left in stock.".format(stock))
else:
    print("Thanks for buying our products! We will dispatch and deliver you {} item(s).".format(num))
    stock = stock-num
    print("{} item(s) left in stock.".format(stock))

# Print the sum of all the even and odd numbers from 20,50

even = 0
odd = 0
for i in range(20,50):
    if i % 2 == 0:
        even+=i
    else:
        odd+=i
print("Sum of all the even numbers from 20 to 50 {}, all the odd numbers {}.".format(even,odd))

# Write a program to print the sum of all the 3 digits divisible by 5
su = 0
for i in range(100,1000):
    if i % 5 == 0:
        su+=i

print("The sum of all the 3 digit numbers divisible by 5: {}.".format(su))
num = int(input("Enter a number: "))
total = 1
for i in range(num,0,-1):
    total*=i
    
print(total)

##Write a program to find factors of a given number
##Write a program to check if a given number is prime or not
##WAP to find number of factors of a number

# Factors Code
num = int(input("Enter a number: "))
factors = []
for i in range(1,num):
    if num % i == 0:
        factors.append(i)
        
print("All the factors of {}: {}.".format(num,factors))

#Prime Code
num = int(input("Enter another number: "))
factornum = 0
for i in range(1,num):
    if num % i == 0:
        factornum += 1

if factornum > 1:
    print("Number {} is not prime.".format(num))
else:
    print("Number {} is prime.".format(num))

#Number of factors code
num = int(input("Enter another number (this is the last time I'm asking you :) ): "))
factornum = 0
for i in range(1,num):
    if num % i == 0:
        factornum += 1

print("There are {} factors of {}".format(factornum,num))

num = int(input("Enter a number: "))
largest=smallest=num
for i in range(0,10):
    num = int(input("Enter a number: "))
    if num > largest:
        largest = num
    elif num < smallest:
        smallest = num
print(largest)
print(smallest)

#WAP to input 10 integers and display the largest even and smallest odd integer
#WAP to input 10 integers and find the sum of 2-digit and 3-digit numbers seperately
num1 = int(input("Enter a Number: "))
largest=smallest=num1
for i in range(0,1):
    num = int(input("Enter a Number: "))
    if num > largest and num % 2 == 0:
        largest = num
    elif num < smallest and not num % 2 == 0:
        smallest = num
print("Largest even number: {}, Smallest odd number: {}.".format(largest,smallest))

sum1 = 0
sum2 = 0
for i in range(0,5):
    num = int(input("Enter a number: "))
    if num >= 10 and num > 100:
        sum1+=num
    elif num >= 100 and num <= 1000:
        sum2+=num
print("The sum of all the 2-digit numbers: {}, All the 3-digit numbers: {}".format(sum1,sum2))

#WAP to take 10 integer inputs from the user and print and display "EVEN" if all the number are even else: print "NOT EVEN"
even = True
for i in range(1,10):
    num = int(input("Enter a number: "))
    if  num % 2 != 0:
        even = False
if even:
    print("Even")
else:
    print("Not even")

#WAP to take 5 integer inputs from the user if all the numbers are same then print same else: not same
num = int(input("Enter a number: ")) 
same = True

for i in range(1,4):
    num1 = int(input("Enter a number: "))
    if num != num1:
        same = False


if same:
    print("Same")
else:
    print("Not same")

#WAP to take 10 integers from the user and check if they are in ascending order or not
start = int(input("Enter a number: "))
ascending = True
for i in range(1,10):
    num = int(input("Enter a number: "))
    if num != start+1 and ascending:
        ascending = False
    start = num

if ascending:
    print("Ascending")
else:
    print("Not ascending")

#1*2+3*4+5*6+7*8+9*10

1*2
3*4
5*6
7*8
9*10

total = 0
for i in range(1,10,2):
    total += i * (i - 1)
    print("{} * {} + ".format(i,i+1),end='')

print("\nSum of the series: {}".format(total))

total1 = 0
for i in range(1,10):
    total1 += i / (i + 1)
    print("{} / {} + ".format(i,i+1),end='')

print("\nSum of the series: {}".format(total))

total = 0
n = int(input("Enter a number: "))
x = int(input("Enter another number: "))
for i in range(1,n,2):
    total += x ** i / i + 1
    print("{} / {} /".format(i,i+1),end='')
print("\nTotal: {}.".format(total))

#S = x/2 + (x^2)/3 + (x^3)/4 +  + (x^n)/n+1

import matplotlib.pyplot as plt
import numpy as np

amplifier = 500

def noise(x,y):
    num = np.random.normal(x,y)
    if num > 0.5:
        num = 0.5
    elif num < -0.5:
        num = -0.5
    return num

def fractalNoise(x,y):
    y1 = noise(x, y) * amplifier
    y2 = noise(x, y) * amplifier + amplifier / 2
    y3 = noise(x, y) * amplifier + amplifier
    return y1 + y2 / 2 + y3 / 6

#S = x/2 + (x^2)/3 + (x^3)/4 +  + (x^n)/n+1
x = int(input("Enter a number: "))
n = int(input("Enter another Number: "))
total = 0
for i in range(1,11):
    total += (x ** i) / i + 1
    print("{} ** {} / {} + 1".format(x,i,i))
# x / 2 in the form of x ** n
print("Total: {}.".format(total))

# Write a series for x ** i / i - 1
x = int(input("Enter a number: "))
total = 0

for i in range(1,11):
    total += (x ** (i + 1)) / i
    print("({} ** ({})) / {} ".format(x,i+1,i))

print("Total: {}.".format(total))

# Fibonacci Series: 0 , 1, 1, 2, 3 ,5 ,8 , 13 , 21 ...
# lastnum + num = newnum
# 0 * 1.6
a = 0
b = 1
print(a,"\n" + str(b))
for i in range(1,100):
    c = a + b
    a = b
    b = c
    print(c)

# Tribonacci Series : 0, 1, 1, 2, 5, 12, 29, 70, 169, 408, 985, 2378, 5741, etc
# 2ndlastnum + lastnum + num = newnum
a = 0
b = 1
c = 1
d = 0
print(a)
print(b)
print(c)
for i in range(0,7):
    d = a + b + c
    a = b
    b = c
    c = d
    print(d)

a = 1
b = 2
c = 5
d = 0
for i in range(0,10):
    d = (a + b + c) * 2
    a = b
    b = c
    c = d
    print(d)

b = 1
c = 2
d = 0

print(1)
print(2)

for i in range(0,15):
    d = (c) * 2 + b
    b = c
    c = d
    print(d)

Write a program to print the first 15 numbers of the Pell series.
Pell series is a series which starts from 1 and 2 and subsequent 
number are the sum of twice the previous number and the number 
previous to the previous number.
Pell series: 1,2,5,12,12,29,70,169,408,985,2378,5471,13860

Write a program to find the sum of 1st 10 numbers of Lucas series 
i.e., 2,1,3,4,7,11,18,.... Lucas series is such a series which starts 
from 2 and 1, and subsequent numbers are the sum of the previous two numbers

# Lucas Series
a = 2
b = 1
c = 0

print(2,end=', ')
print(1,end=', ')

for i in range(0, 10):
    c = a + b
    a = b
    b = c
    print(c,end=', ')

# WAP to check if the two numbers amicable and 
# Amicable: sum of factors of first number is equal to second number and Vice Versa




num = 1210
num2 = 1184

def amicable(num, num2):
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i
    if total == num2:
        return True
    else:
        return False


if amicable(num, num2):
    print("True")
else:
    print("False")

# WAP to take a number as an input from the user and check if it is Palendrome or not
# Palendrome number: If the reverse of the number is equal to the number 
# EG: num = 1221 
# Output: Palendrome
# EG: num = 1234
# Output: Not Palendrome
num = int(input("Enter a number:"))
num2 = num
next = 0

while num > 0:
    rem = num % 10
    next = next * 10 + rem
    num //= 10

if num2 == next:
    print("Palendrome")
else:
    print("Not Palendrome")

# WAP to check if a number is an Armstrong Number
# Armstrong Number: The sum of the cube of each digit of a number should be equal to the last digit in the number
num = int(input("Enter a number: "))
num2 = num
last = num - (num // 10 * 10)
total = 0

while num > 0:
    mod = num % 10
    num //= 10
    total += (mod ** last)

if total == num2:
    print("Armstrong")
else:
    print("Not Armstrong")

# Homework: get all the armstrong number from 1-1000 (can use for loop)
for i in range(1,1000):
    num = i
    num2 = num
    last = num - (num // 10 * 10)
    total = 0

    while num > 0:
        mod = num % 10
        num //= 10
        total += (mod ** last)

    if total == num2:
        print("Armstrong: {}".format(total))

def getDays():
    day1 = input("When do you have a lesson?")
    if day1 == "Wednesday":
        print("Ok...")
    elif day1 == "Saturday":
        print("Whoops, you have a lesson right now")
    day2 = input("Do you have another lesson")
    if day2 == "Wednesday":
        print("Ok...")
    elif day2 == "Saturday":
        print("You have a lesson right now!")
getDays()
def attendedLesson():
    at = input("Have you attended todays lesson? ")
    if at == "Yes":
        print("Good Job!")
    else:
        print("You are going to have to right an apology to your teacher...")
        ap = input("Enter your apology for your teacher: ")
        ap2 = input("Enter an apology for your dad: ")
attendedLesson()

# Create a pattern
for x in range(0,5):
    for z in range(0, 5):
        print("*",end=' ')
    print("\n")

# Create a triangle
for x in range(0, 5):
    for z in range(0, x + 1): 
        print("*",end=' ')
    print("\n")

num = 5
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
continues with an input

Try pyramid and Right-Angled Triangle


max = int(input("Enter a number: "))
for x in range(1, max + 1):
    for z in range(0, x): 
        print(x, end=' ')
    print("\n")

max = int(input("Enter a number: "))
for x in range(1, max + 2):
    for z in range(x, 1, -1):
        print("*",end=' ')
    print("\n")

max = int(input("Enter a number: "))
for y in range(0, max // 2):
    for x in range(0, y + 1):
        print("*",end=' ')
    print("\n")
for y in range(0, max // 2):
    for x in range(max // 2, y, -1):
        print("*",end=' ')
    print("\n")

Create the same thing but with 1,2,3,4,5
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
try 
/ |
___



max = int(input("Enter a number: ")) * 2
val = 0

for y in range(0, max // 2):
    val += 1
    for x in range(0, y + 1):
        print(val, end=' ')
    print("\n")


for y in range(1, max // 2):
    val -= 1
    for x in range(max // 2, y, -1):
        print(val, end=' ')
    print("\n")

max = 5

for y in range(0, max):
    for x in range(0, y * 2):
        print(end=' ')
    for x in range(y):
        print("*",end='')
    print("\n")

y:
*
*
*
*
*
x and y:
spaces = max - numberof*
1
5-1 = 4
5-2 = 3
5-3 = 2
    * 8 
   ** 6
  *** 4
 **** 2
/ |
___


for y in range(0, 8, 2):
    spaces = 8 - y 
    num = y + 1

    for x in range(spaces):
        print(end=' ')

    for x in range(num):
        print("*",end='')
    
    print("\n")

# Create a Pyramid

max = int(input("Enter a number: ")) + 1
val = max


for y in range(max):
    for x in range(val):
        print(end=' ')
    
    for x in range(y):
        print("*",end=' ')
    
    print("\n")
    val -= 1

# Create a Diamond Shape
max = int(input("Enter a number: ")) + 1 * 2


for y in range(max // 2):
    for x in range(max - y - 1):
        print(end=' ')
    
    for x in range(y):
        print("*",end=' ')
    
    print("\n")

for y in range(max // 2, max):
    for x in range(y):
        print(end=' ')
    
    for x in range(max - y - 1):
        print("*",end=' ')
    
    print("\n")

Try
*********
 *******
  *****
   ***
    *
   ***
  *****
 *******
*********

max = int(input("Enter a number: "))

for y in range(max - 1):
    for x in range(y + 1):
        print(end=' ')
    
    for x in range(max - y):
        print("*",end=' ')

    print("\n")

for y in range(max):
    for x in range(max - y):
        print(end=' ')
    
    for x in range(y + 1):
        print("*",end=' ')
    
    print("\n")

max = int(input("Enter a number: ")) + 1

for y in range(max):
    for x in range(y):
        print(y, end=' ')
    print("\n")

max = int(input("Enter a number: ")) + 1

for y in range(1, max):
    for x in range(max - y):
        print(y, end=' ')
    print("\n")

max = int(input("Enter a number: ")) + 1

for y in range(1, max):
    for x in range(y, 0, -1):
        print(x, end=' ')
    print("\n")

Try

1

3 2

6 5 4

10 9 8 7

1 

1 2 1 

1 2 3 2 1 

1 2 3 4 3 2 1 

1 2 3 4 5 4 3 2 1

           1 

         1 2 

      1 2 3 

   1 2 3 4 

 1 2 3 4 5

         1 

        1 2 

    1 2 3 

   1 2 3 4 

 1 2 3 4 5

1

2 3 4

5 6 7 8 9
max = int(input("Enter a number: "))

for y in range(0, max):
    spaces = max - y 
    num = y + 1

    for x in range(spaces):
        print(end=' ')

    for x in range(1, num + 1):
        print(x,end='')
    
    print("\n")

1

2 3 4

5 6 7 8 9



max = int(input("Enter a number: "))
count = 1
stop = 2

for y in range(1, max + 1, 2):
    for x in range(1, stop):
        print(count, end=' ')
        count += 1

    print("\n")
    stop += 2

max = int(input("Enter a number: ")) + 1

for y in range(max):
    for x in range(1, y + 1):
        print(x, end=' ')

    for z in range(y - 1, 0, -1):
        print(z, end=' ')

    print("\n")
    

max = int(input("Enter a number: "))
val = max + 1

for y in range(max, 2, -1):
    for x in range(val - y, max):
        print(x, end=' ')

    for z in range(val - y, max, - 1):
        print(z, end=' ')
    
    print("\n")
    val += 1

import random

for y in range(1, 11):
    for x in range(y):
        print(random.randint(x,11), end=' ')
    print("\n")

num = 1
def myfunc():
    return num
print(num) # 1
print(myfunc()) # 1
print(num) #1


num = 1
def myfunc():
    num = 10
    return num
print(num) # 1
print(myfunc()) # 10
print(num) # 10

num = 1
def myfunc ():
    global num
    num = 10
    return num
print (num) # 1
print(myfunc()) # 10
print(num) # 10


def display():
    print("Hello", end = ' ')
display() # Hello
print("there!") # there!

Q26. Write a Python function to calculate the factorial of a 
number (a non-negative integer). The function accepts the number 
whose factorial is to be calculated as the argument.





Q27. Write a Python function that takes a number as a parameter 
and checks whether the number is prime or not.

# Q.26
def factorial(num):
    num = int(num)
    if num < 0:
        num = -num

    return num

print(factorial(-10))

# Q.27
def prime(num):
    val = False

    for i in range(2, num):

        if not num % i == 0:
            val = False

            break

    return val

print(prime(1))

Create a function to enter a string as an argument and check whether the string is palendrome or not
123454321


def palendrome(string):
    half1 = ""
    half2 = ""

    for i in range(len(string) // 2):
        half1 = (half1 + string[i])

    for i in range(len(string), len(string) // 2, -1):
        half2 = (half2 + string[i])

    return half1 == half2

print(palendrome("1221"))


def palendrome(string):
    return string == string[::-1]
     
print(palendrome("1221"))

Check if a given number falls in a given range

def numInRange(num, min, max):
    for i in range(min, max + 1):
        if num == i:
            return True

    return False

print(numInRange(10, 1, 10))

Write a Python function to check whether a number is perfect or not. Go to the editor
According to Wikipedia : In number theory, a perfect number is a positive integer that is equal to the sum of 
its proper positive divisors, that is, the sum of its positive divisors excluding the number itself 
(also known as its aliquot sum). Equivalently, a perfect number is a number that is half the sum of all of 
its positive divisors (including itself).
Example : The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, 
and 1 + 2 + 3 = 6. Equivalently, the number 6 is equal to half the sum of all its positive divisors: 
( 1 + 2 + 3 + 6 ) / 2 = 6. The next perfect number is 28 = 
1 + 2 + 4 + 7 + 14. 
This is followed by the perfect 
numbers 496 and 8128.


def perfect(num):
    sum = 0
    for i in range(1, num - 1):
        if num % i == 0:
            sum += i
    
    return num == sum

print(perfect(8128))

# Write a function to take in a number as argument and check if the cube of each digit sums up to be equal to the orginal number
# Example: 153 = 1 ^ 3 + 5 ^ 3 + 3 ^ 3 = 153

# Power is equal to number of digits in the inputted number

def digits(num):
    digits = 0

    while num > 0:
        digits += 1
        num //= 10

    return digits

def armstrong(num):

    power = digits(num)

    sum = 0

    num2 = num

    while num > 0:
        rem = num % 10

        sum += rem ** power

        num //= 10

    return sum == num2


for i in range(10, 100000000):
    if armstrong(i):
        print("Number {} is armstrong.".format(i))

# WAP to take marks of a student for 5 subjects as user input
# And display the grades A B C D E F based on the mark 
# Create a function that will return the grades as for the marking schemer
# Create another function "average" that will calculate the average
# Last: The grades according to marks in each subject seperately
# The Final grade will be the average marks

subjects = ["Maths", "English", "Science", "French", "Physics"]

def avg(sum):
    return sum / 5

def grade(mark):
    if mark > 90:
        return "A"
    elif mark > 85:
        return "B"
    elif mark > 75:
        return "C"
    elif mark > 70:
        return "D"
    elif mark > 65:
        return "E"
    else:
        return "F"

def markingScheme():
    print("\n")

    print("Marking Scheme: \n >90 A \n >85 B \n >75 C \n >70 D \n >65 E \n Else F.")
    print("\n")

def finalGrade(marks):
    sum = 0
    for i in marks:
        sum += i
    
    average = avg(sum)
    grades = grade(average)

    print("You got a final grade is {} the average mark was {} / 100 marks.".format(grades, average))

def marksOutput(subjects, marks):
    for i in range(5):
        subject = subjects[i]
        mark = marks[i]
        grades = grade(mark)

        print("You got an {} in {}. Mark: {}.".format(grades, subject, mark))

def getMarks():
    marks = []

    for i in subjects:
        mark = int(input("How many marks did you get in {}: ".format(i)))
        marks.append(mark)
    
    print("\n")

    return marks

def main():
    marks = getMarks()
    marksOutput(subjects, marks)

    markingScheme()

    finalGrade(marks)

main()

# Homework: Output marks in a table
subjects = ["Maths", "English", "Science", "French", "Physics"]

def avg(sum):
    return sum / 5

def finalGrade(marks):
    sum = 0
    for i in marks:
        sum += i
    
    average = avg(sum)

    print("Average Mark:\t\t{}".format(average))

def marksOutput(subjects, marks):
    for i in range(5):
        subject = subjects[i]
        mark = marks[i]

        print("{}\t{}".format(subject, mark))

def getMarks():
    marks = []

    for i in subjects:
        mark = int(input("How many marks did you get in {}: ".format(i)))
        marks.append(mark)
    
    print("\n")

    return marks

def main():
    marks = getMarks()
    marksOutput(subjects, marks)


    finalGrade(marks)

main()

# Create a program for a coffee shop
# Brew Ratio: the yield of the coffee divided by dose
# Based on the Brew Ratio, determine the style of coffee
# 1:1.5 - 1:2.5 Normal Coffee, 1:1 - 1:1.5 Ristretto, 1:2.5+ Lungo
# First digit = Dose, Second digit = yield
# Customer: Inputs coffee type and amount of coffee

def main():
    typeCoffee = input("What type of coffee do you want?")
    amount = int(input("How much coffee do you want?"))

    y = 0
    dose = amount

    if typeCoffee == "Normal":
        y = dose
    elif typeCoffee == "Ristretto":
        y = dose + (dose / 4)
    elif typeCoffee == "Lungo":
        y = (dose * 2) + (dose / 2)
    else:
        print("Unfortunately, we do not have that type of coffee.")

        return 0

    print("Yield: {}. \nDose: {}.".format(y, dose))

main()

def add(n):
    if (n == 0):
        return n

    return n + add(n - 1)

print(add(10))

# Factorial: the multiplication of all non-negative / non-zero numbers below it

def factorial(n):
    if n == 1:
        return 1
    
    return n * factorial(n - 1)

def factorial2(num):
    s = 1

    for i in range(num, 1, -1):
        s *= i

    return s


s = time.time()
factorial(999)
e = time.time()
print("Recursive factorial took {} seconds.".format(e - s))

start = time.time()
factorial2(990)
end = time.time()
print("For loop factorial took {} seconds.".format(end - start))

# Find the sum of all the the integers in an inputted list
times = int(input("How many list items do you want to add? "))

s = 0

def main(num):
    global s
    if num == 0:
        return s
    
    i = int(input("Enter a number: "))
    s += i

    main(num - 1)

print(main(times))

# Find the sum of the list recursively in a nested list
# e.g [1, 2, [3,4], [5,6]]
# Output: 21
# Check if the element is list or a number 
# e.g [1, 2, [3,4], [5,6]]
# Check value position 0 in list
# Position 0 is a number


li = [1, 2, 3, 4, 5]

sum = 0
def listLoop(num, l):
    global sum

    if num == -1:
        return sum

    sum += l[num]

    return listLoop(num - 1, l)

print(listLoop(len(li) - 1, li))


l = [1, [2, 3], 3, 4, [5, 6]]
val = int(input("Enter a number: "))

def check(num):
    try:
        t = type(l[num])
    except IndexError:
        return ("Position {} does not exist.".format(num))

    if t == int:
        return ("Position {} is a number.".format(num))
    elif t == list:
        return ("Position {} is a number.".format(num))

print(check(val))

l1 = [1, 2, 3, 4, 5, 6]
li = [1, 2, [3,4], [5]]

def getSum(l):
    sum = 0

    for i in l:
        if type(i) == list:
            for j in i:
                sum += j
        else:
            sum += i

    return sum

print(getSum(li))

l1 = [1, 2, 3, 4, 5, 6]
li = [1, 2, [3,4], [5,6]]

sum = 0
def recursiveSum(num, l):
    global sum

    t = type(l[num])

    if num == -1:
        return sum

    if t == list:
        print("h")
        raise ("List detected: Exit code 1")
        return 1
    else: 
        sum += l[num]

        return recursiveSum(num - 1, l)

print(recursiveSum(len(li) - 1, li))

numbers = [1,2,[3,[7,[8,4],9],10],[5,6]]

def recursiveSum(numbers):
    s = 0
    for element in numbers:
        if type(element) == list:
            s = s + recursiveSum(element)
        else:
            s = s + element
    return s
print(recursiveSum(numbers))

# All of the following with recursion
# Find the greatest common divisor: with recursion
# Reverse a string with recursion: Must do
# Most common multiplier

String = str(input("Enter some text: "))

def invertString(num, returnString, string):
    if num == -1:
        return returnString

    returnString = (returnString  + string[num])

    return invertString(num - 1, returnString, string)

print(invertString(len(String) - 1, "", String))

 
def LCM(num, num2):
    for i in range(2, num):
        if num % i == 0 and num2 % i == 0:
            return i

print(LCM(100, 50))

def LCM(num, num2):
    i = 2
    while num2 >= i:
        if num % i == 0 and num2 % i == 0:
            return i
    
    i += 1

    raise ValueError

print(LCM(20, 4))

# Learn how LCM and GCD works (mathmatically)
# LCM 10, 6
# 10: 10, 20, 30, 40, 50, 60
# 6: 6, 12, 18, 24, 30, 36, 42, 60
# GCD 100, 70
# 100 = 70 * 1 + 30
# 70 = 30 * 2 + 10
# 30 = 10 * 3 + 0
# GCD = 10

l = []
l2 = []  

def min(num, num2):
    if num <= num2:
        return num
    else:
        return num2


def LCM(num, num2, depth):
    global l
    global l2

    for i in range(min(num, num2), depth):
        l.append(num * i)
        l2.append(num2 * i)

    for i in range(len(l)):
        li1 = l[i]
        for j in range(len(l)):
            li2 = l2[j]
            if li1 == li2:
                return li2
    
    return LCM(num, num2, depth + 50)

print(LCM(10, 6, 10))

def lcm(x,y):
    if x>y:
        greater=x
    else:
        greater=y
    i=1
    while True:
        i+=1
        if (greater%x==0 and greater%y==0):
            multiplier=greater
            break
        greater+=1
    return multiplier
print(lcm(10,6))



def GCD(x, y):
    i = 1

    while True:
        i += 1
        if (i % x == 0 and i % y == 0):
            return i

print(GCD(10, 6))

def GCD(x,y):
    if x<y:
        small=x
    else:
        small=y
    for i in range(1,small+1):
        if x%i==0 and y%i==0:
            gcd=i
    return gcd
    
print(GCD(60,48))

# LCM (Lowest Common Multiplier)

def lcm(x, y):

    if x > y:
       greater = x
    else:
       greater = y

    for i in range(2, 10000):
       if(i % x == 0) and (i % y == 0):
           LCM = i
           break

    return LCM

print(lcm(11, 57))

# Homework: Create any geometric shape we created using recursion
# Q1: Square
# Q2: Triangle (right-angled)


def square(length, height, num=0):
    if num == height:
        return 0

    print(("* " * length))

    return square(length, height, num + 1)

square(10, 10)
print("\n")

def triangle(height, num=1):
    if num == (height + 1):
        return 0

    print(("* " * num))

    return triangle(height, num + 1)

triangle(10)

# Inbuilt list functions:
list.append(item)
list.remove(item)
list.index(item)
list[number]
list.get(item)

numbers = [1,2,3,4,5]
print(numbers.pop())       # returns the last element of the list (if no args)
print(numbers)
print(numbers.pop(1))       # returns the removed element from teh list: Syntax: list.pop(index)
print(numbers)
# Output:
# 5
# [1, 2, 3, 4]
# 2
# [1, 3, 4]

l = [1, 2, 3, 4, 5]

l2 = []
for i in l:
    j = l.index(i)
    if j == 1:
        l2.append(5)
    l2.append(i)

print(l2)

# Write a program to create a list of random 5 numbers and copy it to another list. Update the value present at index position 2 in the copied list. Display the original list and the copied list and observe the results
import random

randomNumbers = []
numberCopy = []
for i in range(5):
    randomNumbers.append(random.randint(1, 100))

for i in range(len(randomNumbers) - 1):
    if i == 2:
        numberCopy.append(896)
    else:
        numberCopy.append(randomNumbers[i])

print("Random Numbers list:\n{}".format(randomNumbers))
print("Number Copy list:\n{}".format(numberCopy))

import random
randomNumbers = []
numberCopy = []

for i in range(5):
    randomNumbers.append(random.randint(1, 100))

numberCopy = randomNumbers.copy()
numberCopy[2] = 896

print(numberCopy)

# Copy the elements of one list to another using for loop

l = [1, 2, 3, 4, 5]
l2 = []

def copy(l10, l20):
    for i in range(len(l10)):
        l20.append(l10[i])

copy(l, l2)
print(l2)

import time
l = [1, 2, 3, 4]

scolon = time.time()
l2 = l[:]
ecolon = time.time()

l2 = []

sfor = time.time()
for i in range(len(l)):
        l2.append(l[i])
efor = time.time()

l2 = []

scopy = time.time()
l2 = l.copy()
ecopy = time.time()

print("Colon copying took {} seconds\nFor loop copying took {} seconds\n.copy() took {} seconds.".format(ecolon-scolon, efor-sfor, ecopy - scopy))

# There are three cups on a table, at positions A, B, and C. At the start, there is a ball hidden under the cup at position B.
# However, I perform several swaps on the cups, which is notated as two letters. For example, if I swap the cups at positions A and B, I could notate this as AB or BA.
# Create a function that returns the letter position that the ball is at, once I finish swapping the cups. The swaps will be given to you as a list.
# cup_swapping(["AB", "CA", "AB"]) ➞ "C"

# Ball begins at position B.
# Cups A and B swap, so the ball is at position A.
# Cups C and A swap, so the ball is at position C.
# Cups A and B swap, but the ball is at position C, so it doesn't move.

import random

cups = ["A", "B", "C"]

ballPos = "B"

def swapCups(l):
    global ballPos

    for i in l:
        if i[1] == ballPos:
            ballPos = i[0] 

    return ballPos


def askQuestion():
    userPos = str(input("Where do you think the ball is? "))

    if userPos == ballPos or userPos == ballPos.lower():
        print("Correct!")

        return True
    else:
        print("Almost...")

        return False


while True:
    swapCups(["AB", "CA"])

    if askQuestion():
        break

# Create a function that takes two arrays and insert the second array in the middle of the first array.

# Examples
# tuckIn([1, 10], [2, 3, 4, 5, 6, 7, 8, 9]) ➞ [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# tuckIn([15,150], [45, 75, 35]) ➞ [15, 45, 75, 35, 150]
# tuckIn([[1, 2], [5, 6]], [[3, 4]]) ➞ [[1, 2], [3, 4], [5, 6]]

def tuckIn(l, l2):
    mid = len(l) // 2
    
    for i in range(mid, len(l2) + 1):
        l.insert(i, l2[i - 1])

    return l

# Write a function to take a string as user input
# Print the sum of all the even numbers in the string

str = input("Enter some numbers: ")

def get_sum_of_even_numbers(s):
    sum = 0
    for i in s:
        try:
            if int(i) % 2 == 0:
                sum += int(i)
        except ValueError:
            return "Error: Cannot get sum!"

    return sum

print(get_sum_of_even_numbers(str))

# Write a function to find the sum of all even numbers in a list
def getEven(l):
    sum = 0
    try:
        for i in l:
            int(i)
            if i % 2 == 0:
                sum += i
    except ValueError:
        print("Invalid Input!")

    return sum

print(getEven([2, 4]))

def createPlural(l):
    new = []
    try:
        for i in l:
            str(i)
            if i[-1] == "s":
                new.append(i)
            else:
                new.append((i + "s"))
    except ValueError:
        print("Error: Value must be convertable to string")
        return None

    return new

print(createPlural(["cat"]))

def filter_list(l):
    l2 = []
    for i in range(len(l)):
        if type(l[i]) != str:
            l2.append(l[i])

    return l2

print(filter_list([1, "a", "b", 0, 15]))
print(filter_list([1, 2, "a", "b"]))
print(filter_list([1, 2, "aasf", "1", "123", 123]))

def evenly_divisible(a, b, c):
    sum = 0
    for i in range(a, b + 1):
        if i % c == 0:
            sum += i

    return sum

print(evenly_divisible(1, 10, 20))
print(evenly_divisible(1, 10, 2))
print(evenly_divisible(1, 10, 3))

# Show this!!!
def card_hide(s):
    newS = ""
    for i in range(len(s)):
        if i < len(s) - 4:
            newS = (newS + "*")
        else:
            newS = (newS + str(s[i]))
    
    return newS

print(card_hide("1234123456785678"))

# The "Reverser" takes a string as input and returns that string in reverse order, with the opposite case.
# Examples
# reverse("Hello World") ➞ "DLROw OLLEh"
# reverse("ReVeRsE") ➞ "eSrEvEr"
# reverse("Radar") ➞ "RADAr"
# Create a function that returns the thickness (in meters) of a piece of paper after folding it n number of times. The paper starts off with a thickness of 0.5mm.

#Examples
#num_layers(1) ➞ "0.001m"
# Paper folded once is 1mm (equal to 0.001m)

#num_layers(4) ➞ "0.008m"
# Paper folded 4 times is 8mm (equal to 0.008m)

#num_layers(21) ➞ "1048.576m"
# Paper folded 21 times is 1048576mm (equal to 1048.576m)

def reverse(s):
    newS = ""
    str(s)

    for i in range(len(s) - 1, -1, -1):
        current = str(s[i])
        if current == current.lower():
            newS = newS + current.upper()
        else:
            newS = newS + current.lower()
    
    return newS

print(reverse("hello"))

def num_layers(n):
    n = (n + 1) ** 0.5
    
    num = n * 0.001

    return num

# Create a function that accepts an argument as a list and displays the list and rotates
# rotate([1, 2, 3, 4, 5], 2) -> 34512

def rotate(l, rotation):
    newL = []

    for i in range(rotation, len(l)):
        newL.append(l[i])

    for i in range(rotation):
        newL.append(l[i])

    print(newL)

    return newL

l = [1, 2, 3, 4, 5]


def rotation2(l, rotation):
    newL = l[rotation:5:1]
    newL.insert(len(newL), l[0:rotation:1])

    print(newL)

rotation2(l, 2)

# Write a function to do left rotation
# [1, 2, 3, 4, 5] -> [5, 1, 2, 3, 4] k = 1

def rotate(l, k):
    newL = []

    for i in range(len(l) - k, len(l)):
        newL.append(l[i])

    for i in range(0, len(l) - k):
        newL.append(l[i])

    return newL

nums = [1, 2, 3, 4, 5]

print(rotate(nums, 1))

# Python Program to Map Two Lists into a Dictionary
# Python Program to Create a Dictionary with Key as First Character and Value as Words Starting with that Character

def lists_to_dict(l=[], l2=[]):

    d = {}

    for i in range(len(l)):
        d[l[i]] = l2[i]

    print(d)

    return d

def word_to_dict(l=[]):
    d = {}

    for i in l:
        str(i)

        first = i[0]
        rest = ""

        for j in range(1, len(i)):
            rest = (rest + i[j])

        d[first] = rest

    print(d)

    return d

# Python Program to Generate a Dictionary that Contains Numbers in the Form (x,x*x) 
# Python Program to Count the Frequency of letters Appearing in a String Using a Dictionary
# Search: "Raymond Vleeshouwer"
# {"r": 1, "a": 1}

def lists_to_dict(l=[], l2=[]):
    d = {}

    for i in range(len(l)):
        d[l[i]] = l2[i]

    return d

def num_dict(l):
    d = {}

    for i in l:
        int(i)

        d[i] = i * i

    print(d)

    return d

def letter_frequency(s):
    s = s.lower()
    s = ""
    letters = []
    frequencys = []

    for i in s:
        if not i in letters:
            letters.append(i)
            frequencys.append(1)

# Python Program to Create a List of Tuples with the First Element as the Number and Second Element as the Square of the Number
# Python Program to Remove All Tuples in a List of Tuples with the number Outside the Given Range 

def createTuples(iters):
    l = []
    for i in range(iters):
        t = (i, i*i)
        l.append(t)
    return l

print(createTuples(10))

def deleteTuples(l, min, max):
    k = 0

    for i in l:
        if type(i) == tuple:
            l2 = []

            for j in i:
                if j >= min and j <= max:
                    l2.append(j)

            t = tuple(l2)

            l.remove(i)
            l.insert(k, t)
        k += 1

    return l

l = [1, (2, 50, 2)]

print(deleteTuples(l, 1, 1))

# Do something!!!

def toTuple(ins):
    l = []

    for i in range(ins):
        l.append(input("Enter Something: "))
    
    return tuple(l)

print(toTuple(5))

def getInputs(inputs):
    b = ()
    for i in range(inputs):
        a = input("Enter something: ")
        b = b + (a,)
    return b

print(getInputs(5))

# Check if a string contains the entire alphabet
def containsAlphabet(string):
    alphabet = {'a': False, 'b': False, 'c': False, 'd': False, 'e': False, 'f': False, 'g': False, 'h': False, 'i': False, 'j': False, 'k': False, 'l': False, 'm': False, 'n': False, 'o': False, 'p': False, 'q': False, 'r': False, 's': False, 't': False, 'u': False, 'v': False, 'w': False, 'x': False, 'y': False, 'z': False}

    for i in string:
        low = i.lower()
        if low in alphabet.keys():
            alphabet[low] = True 

    for i in alphabet.values():
        if i == False:
            return "The input sentence does not contain all the letters of the alphabet"

    return "The input sentence has all letters of the alphabet!"

def containsAlphabet(string):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    string = string.lower()

    for i in string:
        if i in alphabet:
            alphabet.remove(i)

    if alphabet == []:
        return "The input string contains all the letters of the alphabet!"
    
    return "The input string does not contain all the letters of the alphabet."

# Check if the entire alphabet is present in the string

alphabet = "abcdefghijklmnopqrstuvwxyz"

string = input("Enter some text: ")
string = string.lower()

def search(s, letters):
    for i in letters:
        if i == s:
            return True

    return False

for i in range(-1, len(string)):
    if search(string[i], alphabet):
        alphabet = alphabet.replace(string[i], "")

if alphabet == "":
    print("The input string has all the letters of the alphabet.")
else:
    print("It doesn't have all the letters of the alphabet.")

# An array is special if every even index contains an even number and every odd index contains an odd number. Create a function that returns true if an array is special, and false otherwise.

def isSpecialList(l):
    for i in range(len(l)):
        cond = (i % 2 == 0 and l[i] % 2 == 0) or (i % 2 != 0 and l[i] % 2 != 0)
        if not cond:
            return False
    
    return True

print(isSpecialList([2, 7, 9, 1, 6, 1, 6, 3]))
=

# Question: Write a function addingAllTheWeirdStuff which adds the sum of all the odd numbers in array2 to each element under 10 in array1. Similarly, addingAllTheWeirdStuff should also add the sum of all the even numbers in array2 to those elements over 10 in array1.

# BONUS: If any element in array2 is greater than 20, add 1 to every element in array1.

def addingAllTheWeirdStuff(array1, array2):
    s = 0
    for i in array2:
        if i % 2 != 0:
            s += i

    for i in range(len(array1)):
        if array1[i] < 10:
            array1[i] = array1[i] + s
    
    for i in array2:
        if i >= 20:
            for i in array1:
                i += 1
            break
    
    return array1

print(addingAllTheWeirdStuff([1, 5, 9, 10, 13], [1, 2, 3, 4, 5]))

# Create a function to accept an array of numbers 
# Create another function to check if the number is false or not
# Create another function to check if the number is divisible by 5
# Return the final list which contains all the numbers which are either divisible by 5 or are odd numbers

def checkFalse(num):
    if num % 2 == 0:
        return False
    else:
        return True

def divisible(num):
    if num % 5 == 0:
        return True
    else:
        return False

def getList():
    amount = int(input("How many objects do you want to add to the list? "))
    l = []

    for i in range(amount):
        l.append(int(input("Enter something: ")))

    final = []

    for i in l:
        if divisible(i) or checkFalse(i):
            final.append(i)

    return final

print(getList())

# Write a program to create a function that accepts a sorted array with missing values insert the given number at the correct position
 
def vladputIn(sortedL, n):
    index = 0

    for i in sortedL:
        if n > i:
            index += 1
        elif n < i:
            break
    
    sortedL.insert(index, n)

    return sortedL

print(vladputIn([1, 5, 7, 9, 11], 6))
print(vladputIn([1, 5, 7, 9, 11], 12))
print(vladputIn([1, 5, 7, 9, 11], 0))

import random, time
# Homework: Write a function that accepts an array of unsorted duplicate values [1, 1, 2, 2, 4, 7, 5] and sort the values without using built-in sorting functions

def sort(array):
    n = len(array)

    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False
        if already_sorted:
            break

    return array

d = {}

# sorting algorithm with dictionary (counts the number of occurences of the number)

def countOccurences(sorted_array):
    occurences = {}

    for i in sorted_array:
        if i in occurences.keys():
            a = {i: occurences.get(i) + 1}
            occurences.update(a)
        else:
            occurences[i] = 1

    return occurences

def sort(array):
    n = len(array)
    
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False
        if already_sorted:
            break

    return countOccurences(array)

d = [7, 1, 2, 7, 1]

print(sort(d))

Mr X is fan of pairs and he likes all things that come in pairs. He even has a doll collection in which the dolls come in pairs. One day while going through his collection he found that there are odd number of dolls. Someone had stolen a doll!!! 
Help Mr. X find which type of doll is missing.. 
Input 
The first line contains an integer T, the number of test cases. 
The first line of each test case contains an integer N, the number of dolls. 
The next N lines are the types of dolls that are left. 
Output 
For each test case, display the type of doll that doesn't have a pair, in a new line. 
 
Input: 
1 
3 
1 
2 
1 
 
Output: 
2 
 
Input: 
1 
5 
1 
1 
2 
2 
3 
Output: 
3 

def helpX(array):
    testCases = array[0]
    numDolls = array[1]

    array.remove(testCases)
    array.remove(numDolls)

    d = {}

    for i in array:
        if i in d.keys():
            new = {i: d.get(i) + 1}
            d.update(new)
        else:
            d[i] = 1

    for key, value in d.items():
        if not value % 2 == 0:
            print(key)

helpX([1, 5, 1, 1, 2, 2, 3])

def swap(string):
    new2 = string.replace("W", "M")
    new = string.replace("M", "W")

    condition = string.find("M") or string.find("W")
    if condition:
        if not new2 == string:
            return new2
        else:
            return new

print(swap(""))

probably know that some characters written on a piece of paper, after turning this sheet 180 degrees, can be read, although sometimes in a different way. So, uppercase letters "H", "I", "N", "O", "S", "X", "Z" after rotation are not changed, the letter "M" becomes a "W", and Vice versa, the letter "W" becomes a "M".

We will call a word "shifter" if it consists only of letters "H", "I", "N", "O", "S", "X", "Z", "M" and "W". After turning the sheet, this word can also be read, although in a different way. So, the word "WOW "turns into the word "MOM". On the other hand, the word "HOME" is not a shifter.

Find the number of unique shifter words in the input string (without duplicates). All shifters to be counted, even if they are paired (like "MOM" and "WOW"). String contains only uppercase letters.

Examples
Shifter.count("SOS IN THE HOME") == 2 // shifter words are "SOS" and "IN"
Shifter.count("WHO IS SHIFTER AND WHO IS NO") == 3 // shifter words are "WHO", "IS", "NO"
Shifter.count("TASK") == 0 // no shift

def count(string):
    l = stringToList(string)
    shifters = ["H", "I", "N", "O", "S", "X", "Z", "M", "W"]
    numShifters = 0
    
    for i in l:
        allShift = True
        for j in i:
            if not j.upper() in shifters:
                allShift = False
                break

        if allShift:
            numShifters += 1

    return numShifters

def stringToList(string):
    l = []
    currentWord = ""
    string = (string + " ")

    for i in string:
        if i == " ":
            l.append(currentWord)
            currentWord = ""
        else:
            currentWord = (currentWord + str(i))
    
    return set(l)

print(count("WHO IS SHIFTER AND WHO IS NO"))

Given a string with consecutive repeated characters in a string. Create a function compactString(text) that will return a shortened string with the characters followed by number of repetitions. 
Example: 
text = "wwwwweetrrrioops" 
Output: w5e2t1r3i1o2p1s1 

def countOccurences(val, string):
    occurences = 0
    for i in string:
        if val == i:
            occurences += 1

    return occurences

def compactString(string):
    new = ""
    for i in set(string):
        new = (new + f"{i}{countOccurences(i, string)}")

    return new


print(compactString("wwwwweetrrrioops"))

def compactString(string):
    d = {}
    new = ""
    for i in string:
        if i not in d.keys():
            d[i] = 1
        else:
            d[i] += 1

    for i in d.keys():
        new = (new + f"{i}{d.get(i)}")

    return new

print(compactString("wwwwweetrrrioops"))

Wolves have been reintroduced to Great Britain. You are a sheep farmer, and are now plagued by wolves which pretend to be sheep. Fortunately, you are good at spotting them. 
Warn the sheep in front of the wolf that it is about to be eaten. Remember that you are standing at the front of the queue which is at the end of the array: 
[sheep, sheep, sheep, sheep, sheep, wolf, sheep, sheep]      (YOU ARE HERE AT THE FRONT OF THE QUEUE) 
   7      6      5      4      3            2      1 
 
If the wolf is the closest animal to you, return "Pls go away and stop eating my sheep". Otherwise, return "Oi! Sheep number N! You are about to be eaten by a wolf!" where N is the sheep's position in the queue. 
Note: there will always be exactly one wolf in the array. 
Examples 
Input: ["sheep", "sheep", "sheep", "wolf", "sheep"] 
Output: "Oi! Sheep number 1! You are about to be eaten by a wolf!" 

Input: ["sheep", "sheep", "wolf"] 
Output: "Pls go away and stop eating my sheep"
['sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'wolf', 'sheep', 'sheep']), 'Oi! Sheep number 2! You are about to be eaten by a wolf!'
['sheep', 'wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep']), 'Oi! Sheep number 5! You are about to be eaten by a wolf!'
['wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep']), 'Oi! Sheep number 6! You are about to be eaten by a wolf!'
['sheep', 'wolf', 'sheep']), 'Oi! Sheep number 1! You are about to be eaten by a wolf!'
['sheep', 'sheep', 'wolf']), 'Pls go away and stop eating my sheep' 

def checkWolves(array):
    array.reverse()
    pos = array.index("wolf")

    if pos == 0:
        return "Pls go away and stop eating my sheep" 
    else:
        for i in range(0, len(array) - 1):
            if i == pos - 1:
                return f"Oi! Sheep number {i + 1}! You are about to be eaten by a wolf!"

print(checkWolves(['sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'wolf', 'sheep', 'sheep']))#, 'Oi! Sheep number 2! You are about to be eaten by a wolf!'
print(checkWolves(['sheep', 'wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep']))#, 'Oi! Sheep number 5! You are about to be eaten by a wolf!'
print(checkWolves(['wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep']))#, 'Oi! Sheep number 6! You are about to be eaten by a wolf!'
print(checkWolves(['sheep', 'wolf', 'sheep']))#, 'Oi! Sheep number 1! You are about to be eaten by a wolf!'
print(checkWolves(['sheep', 'sheep', 'wolf']))#, 'Pls go away and stop eating my sheep'

Our football team finished the championship. The result of each match look like "x:y". Results of all matches are recorded in the collection. 
For example: ["3:1", "2:2", "0:1", ...] 
Write a function that takes such collection and counts the points of our team in the championship. Rules for counting points for each match: 
if x > y: 3 points 
if x < y: 0 point 
if x = y: 1 point 
 
def points(): 
pass 
 
testcases 
points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']), 30) 
points(['1:1','2:2','3:3','4:4','2:2','3:3','4:4','3:3','4:4','4:4']), 10) 
points(['0:1','0:2','0:3','0:4','1:2','1:3','1:4','2:3','2:4','3:4']), 0) 
points(['1:0','2:0','3:0','4:0','2:1','1:3','1:4','2:3','2:4','3:4']), 15) 
points(['1:0','2:0','3:0','4:4','2:2','3:3','1:4','2:3','2:4','3:4']), 12)

def points(l):
    total = 0

    for i in l:
        x, y = i.split(":")

        if x > y:
            total += 3
        elif x == y:
            total += 1

    return total

You get an array of numbers, return the sum of all of the positives ones. 
Example [1, -4, 7, 12] => 1 + 7 + 12 = 20 
Note: if there is nothing to sum, the sum is default to 0. 


def returnSum(l):
    s = 0
    
    for i in l:
        if i > 0:
            s += i

    return s

YouTube had a like and a dislike button, which allowed users to express their opinions about particular content. It was set up in such a way that you cannot like and dislike a video at the same time. There are two other interesting rules to be noted about the interface: Pressing a button, which is already active, will undo your press. If you press the like button after pressing the dislike button, the like button overwrites the previous "Dislike" state. The same is true for the other way round. 
Task 
Create a function that takes in a list of button inputs and returns the final state. 
Examples 
like_or_dislike([Dislike]) ➞ Dislike like_or_dislike([Like, Like])  ➞ Nothing like_or_dislike([Dislike, Like]) ➞Like like_or_dislike([Like, Dislike, Dislike]) ➞ Nothing 
Notes 
If no button is currently active, return Nothing. 
If the list is empty, return Nothing.

Dislike = "Dislike"
Like = "Like"

def like_or_dislike(l):
    if l == None:
        return "Nothing"
    else:
        state = l[0]
        for i in l:
            if i == state:
                state = "Nothing"
            else:
                state = i

        return state

print(like_or_dislike([Dislike, Like, Dislike]))

You will get a list with several scattered numbers 
You must check that the sum of the two values on both sides equals the sum of the rest of the list elements 
And if not, delete the two elements on the sides and check repeatedly, 
until you reach the condition checklist: 
The sum of the list without the sides = the sum of the sides 
If it never equals return an empty list [] 
note: list length can be up to 500 items 
Example: 
Ex1: 
[1,2,3,4,5] ==>1+5!=2+3+4==>[2,3,4] ==>2+4!=3==[3] ==>3+3!=0==>[] 
 
note: (3+3) because 3 is first side and last side... (!= 0) because sum of list without sides = 0 
Ex2: 
[0,104,3,101,0,111] ==>0+111!=104+3+101+0==>[104,3,101,0] ==>104+0=3+101==>[104,3,101,0] 
 
Ex3: 
[1,-1] ==>1-1=0==>[1,-1] 
 
note: (1-1) because 1 is first side and -1 is last side... (= 0) because sum of list without sides (1, -1) = 0 

def total(l):
    s = 0
    for i in l:
        s += i
    return s

def scatter(l, l2):
    l = []
    while True:
        try:
            if not l[0] + l[-1] == total(l2):
                break
        except IndexError:
            return True
        l.pop(0)
        l.pop()

    return False

print(scatter([1, 2, 3, 4, 5], [2, 4]))

Your task is to sum the differences between consecutive pairs in the array in descending order. 
Example 
[2, 1, 10]  -->  9 
 
In descending order: [10, 2, 1] 
Sum: (10 - 2) + (2 - 1) = 8 + 1 = 9 
If the array is empty or the array has only one element the result should be 0 (Nothing in Haskell, None in Rust). 

def sum_diff(l):
    l.sort()
    l.reverse()
    if len(l) == 0 or len(l) == 1:
        return 0
    else:
        s = 0 
        for i in range(len(l) - 1, 0, -1):
            s += (l[i] - l[i - 1])
        return s

print(sum_diff([10, 1, 2]))

Closest elevator 
Given 2 elevators (named "left" and "right") in a building with 3 floors (numbered 0 to 2), write a function elevator accepting 3 arguments (in order): 
left - The current floor of the left elevator 
right - The current floor of the right elevator 
call - The floor that called an elevator 
It should return the name of the elevator closest to the called floor ("left"/"right"). 
In the case where both elevators are equally distant from the called floor, choose the elevator to the right. 
You can assume that the inputs will always be valid integers between 0-2. 
Examples: 
elevator(0, 1, 0); // => "left" 
elevator(0, 1, 1); // => "right" 
elevator(0, 1, 2); // => "right" 
elevator(0, 0, 0); // => "right" 
elevator(0, 2, 1); // => "right" 

def elevator(left, right, call):
    left_diff = abs(left - call)
    right_diff = abs(right - call)
    if left_diff < right_diff:
        return "left"
    else:
        return "right"

print(elevator(0, 2, 1))

Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N. Find the missing element. 
Example 1: 
Input: 
N = 5 
A[] = {1,2,3,5} 
Output: 4 
Example 2: 
Input: 
N = 10 
A[] = {6,1,2,8,3,4,7,10,5} 
Output: 9
do this question with two methods (not the function/class type!)

Given a string S, the task is to create a string with the first letter of every word in the string. 
Example 1: 
Input:  
S = "geeks for geeks" 
Output: gfg 
 
Example 2: 
Input:  
S = "bad is good" 
Output: big 


# Q1:

def add_factorial(n):
    s = 0
    while True:
        s += n
        n -= 1
        if n == 0:
            return s

def find_missing_element(l, n):
    add_fact = add_factorial(n)

    if not sum(l) == add_fact:
        return add_fact - sum(l)
    else:
        return "No missing element"

def find_missing_element2(l, n):
    while True:
        if not n in l:
            return n
        elif n == 0:
            return "No missing element"
        n -= 1

# Q2:

def first_letter(s):
    beforeSpace = False
    newS = ""
    s = " " + s
    for i in s:
        if i == " ":
            beforeSpace = True
        else:
            if beforeSpace:
                newS = newS + str(i)
            beforeSpace = False

    return newS

print(first_letter("ray vle"))

# Create a function that will accept two parameters 1: an array of numbers and 2: s = sum
# Create an algorithm to find the pair of numbers whos summation is equal to s
# s = 5 pair = 2 and 3

def find_pairs(l: list, s: int):
    try:
        for i in range(0, len(l)):
            last, current, next = l[i - 1], l[i], l[i + 1]

            if s == last + current:
                return [last, current]
            elif s == current + next:
                return [current, next]

        return "No value found."

    except Exception:
        return "Error" 

print(find_pairs([1, 2], 3))

def find_pairs(l: list, s: int):
    for i in l:
        for j in l:
            if i + j == s:
                return [i, j]
    return "No value found"

print(find_pairs([1, 2, 5], 6))

Given an array a[] of size N which contains elements from 0 to N-1, you need to find all the elements occurring more than once in the given array.
Input:
N = 5
a[] = {2,3,1,2,3}
Output: 2 3

def reccuring_elements(l):
    l2 = []
    l3 = []

    for i in l:
        if not i in l2:
            l2.append(i)
        else:
            l3.append(i)
    
    return set(l3)

print(reccuring_elements([1, 2, 3, 4, 3, 2, 2, 3, 2, 3]))

def remove_duplicates(l):
    return set(l)

Given an array having both positive and negative integers. The task is to compute the length of the largest subarray with sum 0. 
Input:
N = 8
A[] = {15,-2,2,-8,1,7,10,23}
Output: 5
Explanation: The largest subarray with
sum 0 will be -2 2 -8 1 7.

subarray = a collection of the values inside of an array

Given two strings a and b. The task is to find if the string 'b' can be obtained by rotating another string 'a' by exactly 2 places.

Example 1:

Input:
a = amazon
b = azonam
Output: 1
Explanation: amazon can be rotated anticlockwise by two places, which will make it as azonam.

# Clockwise Shift
def clockwise_shift(a: str, b: str):
    for i in range(2):
        last = a[-1]

        a = a.removesuffix(last)
        a = last + a

    return a == b

# Anti clockwise shift
def anti_clockwise_shift(a: str, b: str):
    for i in range(2):
        first = a[0]

        a = a.removeprefix(first)
        a = a + first

    return a == b


# Anti clockwise shift with a number to control it
def shift(text: str, number: int):
    for i in range(number):
        first = text[0]

        text = text.removeprefix(first)
        text = text + first
    
    return text

print(shift("amazon", 2))

Given two strings 'str1' and 'str2', check if these two strings are isomorphic (similar) to each other.
Two strings str1 and str2 are called isomorphic if there is a one to one mapping possible for every character of str1 to every character of str2 while preserving the order.
Note: All occurrences of every character in str1 should map to the same character in str2

Example 1:

Input:
str1 = aab
str2 = xxy
Output: 1
Explanation: There are two different
charactersin aab and xxy, i.e a and b
with frequency 2 and 1 respectively.

Welcome to the world of the National Football League! 
In the NFL the Triple Crown is given when a receiver has the most receiving yards, the most receiving touchdowns and the most receptions in a single season. 
This year Cooper Kupp managed to get it, however it is quite rare because the last one was in 2005 by Steve Smith. 
Now you will receive a dictionary with the following keys (will always contain each): 
Cooper Kupp 
Justin Jefferson 
Davante Adams 
Each key will have another dictionary as their values with the following keys: 
Receiving yards (value between 1500-2000) 
Receiving touchdowns (value between 10-20) 
Receptions (value between 90-120) 
If one receiver has the most in each category you have to return his name. If there is no receiver with the most values in all categories you should return 'None of them'. 
Example: 
{ 
  'Cooper Kupp':  
    { 
    'Receiving yards': 1786,  
    'Receiving touchdowns': 18,  
    'Receptions': 117}, 
  'Justin Jefferson':  
    { 
    'Receiving yards': 1700,  
    'Receiving touchdowns': 17,  
    'Receptions': 115}, 
  'Davante Adams':  
    { 
    'Receiving yards': 1650,  
    'Receiving touchdowns': 16,  
    'Receptions': 110} 
} 
 
# The output should be 'Cooper Kupp' since he has more receiving yards, more receiving touchdowns and more receptions as well 
Example with two receivers sharing values in at least one category: 
{ 
  'Cooper Kupp':  
    { 
    'Receiving yards': 1900,  
    'Receiving touchdowns': 18,  
    'Receptions': 117}, 
  'Justin Jefferson':  
    { 
    'Receiving yards': 1800,  
    'Receiving touchdowns': 17,  
    'Receptions': 116}, 
  'Davante Adams':  
    { 
    'Receiving yards': 1900,  
    'Receiving touchdowns': 18,  
    'Receptions': 110} 
} 
 
# The output should be 'None of them' since they are tied on receiving yards and receiving touchdowns 


d1 = { 
    'Cooper Kupp':  
    { 
        'Receiving yards': 1900,  
        'Receiving touchdowns': 18,  
        'Receptions': 117
    }, 
    'Justin Jefferson':  
    { 
        'Receiving yards': 1800,  
        'Receiving touchdowns': 17,  
        'Receptions': 116
    }, 

    'Davante Adams':  
    {
        'Receiving yards': 1900,  
        'Receiving touchdowns': 18,  
        'Receptions': 110
    }
}

d2 = { 
  'Cooper Kupp':  
    { 
    'Receiving yards': 1900,  
    'Receiving touchdowns': 18,  
    'Receptions': 117}, 
  'Justin Jefferson':  
    { 
    'Receiving yards': 1800,  
    'Receiving touchdowns': 17,  
    'Receptions': 116}, 
  'Davante Adams':  
    { 
    'Receiving yards': 1900,  
    'Receiving touchdowns': 18,  
    'Receptions': 110} 
}

def spam(d: dict):
    names, yards, touches, receptions = [], [], [], []

    for i in d:
        v = d[i]

        names.append(i)
        yards.append(v['Receiving yards'])
        touches.append(v['Receiving touchdowns'])
        receptions.append(v['Receptions'])


    y_index = yards.index(max(yards))
    t_index = touches.index(max(touches))
    r_index = receptions.index(max(receptions))

    c = y_index == t_index and y_index == r_index and t_index == r_index
    c2 = set(yards) == yards and set(touches) == touches and set(receptions) == receptions

    if c and c2:
        return names[y_index]
    else:
        return "None of them"

s = time()
print(spam(d2))
e = time()
print(f"Took: {e-s} second(s)")

Given two sorted arrays of distinct elements. There is only 1 difference between the arrays. First array has one element extra added in between. Find the index of the extra element. 
 
Example 1: 
 
Input: 
N = 7 
A[] = {2,4,6,8,9,10,12} 
B[] = {2,4,6,8,10,12} 
Output: 4 
Explanation: In the second array, 9 is 
missing and it's index in the first array 
is 4. 
Example 2: 

Input: 
N = 6 
A[] = {3,5,7,9,11,13} 
B[] = {3,5,7,11,13} 
Output: 3 

a = [5, 6]
b = [5]

def find_missing_index(a: list, b: list):
    for i in a:
        if not i in b:
            return a.index(i)

def find_missing_index2(a: list, b: list):
    return a.index(sum(a) - sum(b))

print(find_missing_index(a, b)) # 0.00004220008850097656 seconds
print(find_missing_index2(a, b)) # 0.0000021457672119140625

Homework: Finish This

class Time:
    def __init__(self, start, end):
        self.start = start
        self.end = end + 0.5

    def time_is_good(self, start_time, end_time):
        condition_1 = (start_time > self.end and end_time > self.end)
        condition_2 = (start_time < self.start - 0.5 and end_time < self.start - 0.5)
        if condition_1 or condition_2:
            return True
        else:
            return False

def max_income(planeType: str, length_for_day: int):
    flights = int(600 / (length_for_day + 30))
    print(f"There is a total of {flights} flights possible for {planeType} plane")

    if planeType == '2 seater':
        if length_for_day == 30:
            print(f"You will make: ${flights * 100}")
        if length_for_day == 60:
            print(f"You will make: ${flights * 150}")
    
    if planeType == '4 seater':
        if length_for_day == 30:
            print(f"You will make: ${flights * 120}")
        if length_for_day == 60:
            print(f"You will make: ${flights * 200}")

    if planeType == 'Historic':
        if length_for_day == 30:
            print(f"You will make: ${flights * 300}")
        if length_for_day == 60:
            print(f"You will make: ${flights * 500}")

seater_2 = (int(input("How many minutes should 2 seater plane to fly for? ")) + 30) / 60

seater_4 = (int(input("How many minutes should 4 seater plane fly for? ")) + 30) / 60

historic = (int(input("How many minutes should Historic plane fly for? ")) + 30) / 60

plane_bookings = {"2 seater": (Time(8, 8.5), Time(9, 9.5), Time(10, 10.5)), "4 seater": (Time(14, 14.5), Time(16, 16.5), Time(17.5, 18)), "Historic": (Time(8, 8.5), Time(9, 9.5), Time(10, 10.5), Time(11, 11.5), Time(12, 12.5), Time(13, 13.5), Time(14, 14.5))}

def book(start_time, end_time, planeType):
    times = plane_bookings[planeType]
    can_book_plane = True

    if end_time < start_time:
        print(" (!) End time cannot be earlier than start time")
        return

    if planeType == "2 seater":
        if end_time - start_time > seater_2:
            print(f" (!) Plane cannot operate for more than {seater_2 / 2 * 60} mins")
            return
    elif planeType == "4 seater":
        if end_time - start_time > seater_4:
            print(f" (!) Plane cannot operate for more than {seater_4 / 2 * 60} mins")
            return
    elif planeType == "Historic":
        if end_time - start_time > historic:
            print(f" (!) Plane cannot operate for more than {historic / 2 * 60} mins")
            return

    for i in times:
        if i.time_is_good(start_time, end_time) == False:
            can_book_plane = False

    if can_book_plane:
        print(f"Booking {planeType} at {start_time} - {end_time}.")
        times = times + (Time(start_time, end_time),)
        print(times)
    else:
        print(f"Cannot book {planeType} at {start_time}. Somebody is already flying!")

book(8, 17, "2 seater")

def calculate_profit():
    profits = 0

    seater_2_profits = plane_bookings["2 seater"]
    seater_4_profits = plane_bookings["4 seater"]
    historic_profits = plane_bookings["Historic"]

    if seater_2 == 1:
        print(f"Made £ {len(seater_2_profits) * 100} from 2 seater.\n")
        profits += len(seater_2_profits) * 100
    elif seater_2 == 1.5:
        print(f"Made £ {len(seater_2_profits) * 150} from 2 seater.\n")
        profits += len(seater_2_profits) * 150

    if seater_4 == 1:
        print(f"Made £ {len(seater_4_profits) * 120} from 4 seater.\n")
        profits += len(seater_4_profits) * 120
    elif seater_4 == 1.5:
        print(f"Made £ {len(seater_4_profits) * 200} from 4 seater.\n")
        profits += len(seater_4_profits) * 200

    if historic == 1:
        print(f"Made £ {len(historic_profits) * 300} from Historic.\n")
        profits += len(historic_profits) * 300
    elif historic == 1.5:
        print(f"Made £ {len(historic_profits) * 500} from Historic.\n")
        profits += len(historic_profits) * 500

    print(f"Made £ {profits} in profits today.")

calculate_profit()

Self service checkout.

shopping_tax = 0.055
subtotal = 0

print("Press 0 when you want to checkout")

def get_items():
    global subtotal

    while True:
        quantity = int(input("Please enter quantity (3 maximum): "))

        if quantity == 0:
            return

        price = float(input("Please enter the price: "))

        subtotal += price * quantity

get_items()

total = subtotal + (subtotal / shopping_tax)
print(f"Subtotal: £ {subtotal} Shopping Tax: £ {total - subtotal}")
print(f"Please pay: £ {total}")

# Ubbi Dubbi program
vowels = ["a", "e", "i", "o", "u", "y"]
punctuation = [",", "!", ".", "?"]

def ubbidubbi(eword: str):
    new_data = ""
    current_vowels = ["a", "e", "i", "o", "u"]
    for i in eword:
        if i in current_vowels:
            if i != "e" and eword.index(i) != len(eword):
                current_vowels.remove(i)
                new_data += "ub" + i
            elif not i in punctuation:
                new_data += i
        elif not i in punctuation:
            new_data += i

    return new_data

def ubbidubbi_sentence(esentence: str):
    esentence = esentence.lower()
    ubbidubbis = ""

    for i in esentence.split():
        ubbidubbis += ubbidubbi(i) + " "
    
    return ubbidubbis

print(ubbidubbi_sentence("are you speaking ubbi dubbi?"))

# Homework + 1

def adjacent_repeats(string: str, find: str):
    string, find, repeats = string.lower(), find.lower(), {}
    previous_find = False
    previous_find_index = 0
    index = -1

    for i in string:
        index += 1
        if i == find and previous_find == False:
            previous_find_index = index
            repeats[previous_find_index] = [previous_find_index, 1]
            previous_find = True
        elif i == find and previous_find == True:
            repeats[previous_find_index] = [previous_find_index, (index - previous_find_index) + 1]
        elif i != find:
            previous_find = False
    highest = -1
    highest_tuple = ("ERROR", "ERROR")

    for i in repeats:
        if repeats[i][1] > highest:
            highest = repeats[i][1]
            highest_tuple = (repeats[i][1], repeats[i][0])

    print(highest_tuple)

adjacent_repeats("abxxcabxaaaxcabxxxxc", "x")


def inbounds(num, min, max):
    if num < min:
        num = min
    elif num > max:
        num = max

    return num

def createspaces(numspaces):
    spaces = ""
    for i in range(numspaces):
        spaces += " "
    return spaces

def multi_column_print(L, numcols):
    s = ""

    for i in L:
        i = str(i)
        s += (str(i) + createspaces(inbounds(len(i) - numcols, 1, numcols)))

    return s

L = [2**i for i in range(20)] 
print(multi_column_print(L, 5))

def multi_column_print(L: list, numcols: int):
    s = ""
    for i in L:
        s = f'{s}{i:^{numcols}}'

    return s

L = [2**i for i in range(100000)] 
s = time.time()
print(multi_column_print(L, 5))
e = time.time()
print(f"Took {e-s} seconds to load")

times = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

def get_year_month_and_day():
    date = input('What is the date "YYYY/MM/DD: ')
    splitted_date = date.split("/")
    new_splitted_date = [int(i) for i in splitted_date]
    print(new_splitted_date)

    return new_splitted_date

def is_leap_year(year):
    if year % 4 == 0:
        return True
    else:
        return False

def getDaysInMonth(year, month, dTime):
    leap_year = is_leap_year(year)
    if month == 2 and leap_year:
        return dTime[month] + 1
    else:
        return dTime[month]

l = get_year_month_and_day()

print(getDaysInMonth(l[0], l[1], times))

prices = {"PS5": 499.99, "iPhone 12": 1299.99, "Macbook Pro": 1699.99}
empty = {}

def get_product():
    product = input("Enter a product: ")
    if product in prices.keys():
        print(f"There is 1 {product} in store")
    quantity = int(input("How many: "))

    if quantity > 1:
        print(f" (!) There is only 1 {product} in store.")

    if product in prices.keys():
        print(f"The price of {product} is ${prices[product] * quantity}")
    else:
        print("Hmm. This product doesn't exist, would you like to create a new one?")
        create = input("Would you like create a new product Y / N: ")

        if create == "Y":
            name = input("Name: ")
            price = float(input("Price: "))

            prices[name] = price

def get_revenue():
    amount = input(f"Enter quantity sold ({len(prices)} products)")

    l = amount.split(",")
    total_price = 0
    print(l)
    index = 0
    for i in prices:
        print(f"Sales revenue of {i} is ${prices[i] * int(l[index])}")
        total_price += int(l[index])
        empty[i] = prices[i] * int(l[index])
        index += 1

get_revenue()

class Heater:
    Temperature = 15

    def __init__(self, min: float, max: float, increment: float) -> None:
        self.min = min
        self.max = max
        if increment <= 0:
            self.increment = 5
        else:
            self.increment = increment

    def get_temperature(self) -> int:
        return self.Temperature

    def set_increment(self, increment: float) -> None:
        self.increment = increment

    def warmer(self) -> None:
        if self.Temperature == self.max or self.Temperature + self.increment > self.max:
            return

        self.Temperature += self.increment

    def cooler(self) -> None:
        if self.Temperature == self.min or self.Temperature - self.increment < self.min:
            return

        self.Temperature -= self.increment

class Complex:
    i = 1

    def __init__(self, RealPart: float = 5, ImaginaryPart: float = 5) -> None:
        self.number = RealPart + ImaginaryPart * self.i

        self.RealPart = RealPart
        self.ImaginaryPart = ImaginaryPart

    def add_complex(self, Other) -> None:
        self.RealPart += Other.RealPart
        Other.RealPart += self.RealPart

        self.ImaginaryPart += Other.ImaginaryPart
        Other.ImaginaryPart += self.ImaginaryPart

    def subtract_complex(self, Other) -> None:
        self.RealPart -= Other.RealPart
        Other.RealPart -= self.RealPart

        self.ImaginaryPart -= Other.ImaginaryPart
        Other.ImaginaryPart -= self.ImaginaryPart

    def print_complex(self) -> None:
        print(f"Real Part = {self.RealPart}\nImaginary Part = {self.ImaginaryPart}")

    def multiply_complex(self, Other) -> None:
        self.RealPart *= Other.RealPart
        Other.RealPart *= self.RealPart

        self.ImaginaryPart *= Other.ImaginaryPart
        Other.ImaginaryPart *= self.ImaginaryPart

        print(f"self.RealPart = {self.RealPart}\tOther.RealPart = {Other.RealPart}")
        print(f"self.ImaginaryPart = {self.ImaginaryPart}\tOther.ImaginaryPart = {Other.ImaginaryPart}")
"""