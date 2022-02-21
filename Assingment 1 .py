# 1 ) Python program to check whether the given number is even or not.

a = int(input("Enter you number : " ))

if a % 2 == 0:
    print("Even")
else:
    print("Odd")
	
# 2) Python program to convert the temperature in degree centigrade to Fahrenheit.

Centigrade = int(input("Enter Value (Centigrade) : "))
far = round(((Centigrade * (9/5) )+ 32),2)
print(far)

# 3) Python program to find the product of a set of real numbers.

count = int(input("Number of real numbers: "))
product = 1
for i in range(count):
    x = float(input("Enter a real number: "))
    product =  product * x
print("The product of the numbers is: ", product)

# 4) Python program to find the factorial of a number using recursion.

import math as m
a1 = int(input("Enter a number: "))
a= m .factorial(a1)
print(a)

# 5) Python program to implement linear search.

numbers = [2,5,9,8,3,2,1,9,5,7,55,88,6,4]
a = 0
x = int(input("Enter the number to be found out: "))
for i in range(len(numbers)):
    if (x==numbers[i]):
        print(" Number found at position", i)
        f = 1
        break
if(a==0):
    print("Number not found")
	
# 6) Python program to implement binary search.

def binarySearch(numbers, low, high, x):
    if (high >= low):
        mid = low + (high - low)//2
        if (numbers[mid] == x):
            return mid
        elif (numbers[mid] > x):
            return binarySearch(numbers, low, mid-1, x)
        else:
            return binarySearch(numbers, mid+1, high, x)
    else:
        return -1
numbers = [ 1,4,6,7,12,17,25 ]   //binary search requires sorted numbers
x = 7
result = binarySearch(numbers, 0, len(numbers)-1, x)
if (result != -1):
    print("Search successful, element found at position ", result)
else:
    print("The given element is not present in the array")
	
# 7) Python program to find the largest number in a list without using built-in functions.

numbers = [2,8,6,4,15,9,28,17,11,26]
big = numbers[0]
position = 0
for i in range(len(numbers)):
    if (numbers[i]>big):
        big = numbers[i]
        position = i
print("The largest element is ",big," which is found at position ",position)

# 8) Python program to delete an element from a list by index.

numbers = [5,6,9,8,3,2,1,4,7,8,9]
print(numbers)
x = int(input("Position of the element to be deleted: "))
numbers.pop(x)
print(numbers)

# 9) Python program to print all the items in a dictionary.
Attendance = {'Amey' : '01','Abhinav':'02','Shreyashi' : '03'}
for k,v in Attendance.items():
    print(k, ":", v)
	
# 10) Python program to find the average of 10 numbers using while loop.

x = 0
sum = 0.0
while(x<10):
    number = float(input("Enter a real number: "))
    x =x+1
    sum = sum+number
avg = sum/10;
print("Average :",avg)