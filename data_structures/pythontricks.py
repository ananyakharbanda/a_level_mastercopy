

# assert
a = 10
assert a == 10 


# get default value for unfound keys from dictionary
details = {'name': 'ananya', 'class': '24s02b'}
# details['address']
print(details.get('address', 'singapore'))

# iterate over map
for key in details.keys():
    print (key + ' ' + details[key])

for key,value in details.items():
    print(key + ' ' + value)

arr = [2,7,9,4,5,-3]
arr.sort(reverse=True)

import random

class Person():
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def __repr__(self):
        return self.name + ' ' + self.lastname

# Sample lists of first and last names
first_names = ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack']
last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor']

# Create a list to hold the Person objects
people = []

# Generate 10 random Person objects and insert them into the list
for _ in range(10):
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    person = Person(first_name, last_name)
    people.append(person)

# # Print the list of Person objects
# for person in people:
#     print(f'Name: {person.name}, Last Name: {person.lastname}')

people.sort(key=lambda x: x.lastname)
print(people)


def dec2bin(num, bits):
    bin = ''
    while num >= 1:
        if num % 2 == 0:
            bin = '0' + bin
        else:
            bin = '1' + bin
        num = num // 2
    if len(bin) < bits:
        bin = '0'*(bits-len(bin)) + bin    
    return bin

print(dec2bin(12, 8))


def bin2dec(num):
    dec = 0
    num_list = []
    for i in num:
        num_list.append(i)
    for j in num_list:
        dec = (dec*2) + int(j)
    return dec

print(bin2dec('1100'))

def dec2hex(num):
    hex = ''
    encoded_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'B', 'C', 'D', 'E']
    while num > 0:
        rem = num % 16
        hex = encoded_list[rem] + hex
        num = num // 16
    return hex

print(dec2hex(100))

def hex2dec(hex_str):
    dec = 0
    enc_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    hex_list = []
    for i in hex_str:
        hex_list.append(i)
    for i in range(len(hex_list)):
        dec = dec + enc_dict[hex_list[i]] * (16 ** (len(hex_list) - 1 - i))
    
    return dec

print(hex2dec('2A'))
        
#to join with white space

xx = ' '.join(['ananya', 'kharbanda', 'singapore'])
print(xx)


a_tuple = (2,5)
# cannot do this
# a_tuple[0] = 5
print(a_tuple)


# recursive functions

def sum_of_digits(num):
    if num < 10:
        sum = num
        return sum
    else:
        return sum_of_digits((num // 10)) + (num % 10)

def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    else:
        return base * power(base, exponent-1)

def sum_of_list(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return sum_of_list(arr[:-1]) + arr[-1]

def is_palindrome(str):
    if len(str) == 1:
        return True
    elif len(str) == 2:
        if str[0] == str[1]:
            return True
    elif str[0] == str[-1]:
        return is_palindrome(str[1:-1])
    else:
        return False
    
# print(sum_of_digits(23453))
# print(power(9, 3))
# print(sum_of_list([1,4,3,2]))
print(is_palindrome('123211'))

class RecPrinter():
    def __init__(self):
        self.a = [10, 12, 14, 25, 34]
    
    def print_rec(self, a):
        if len(a) == 0:
            return
        print(a[0])
        n = a[1:]
        self.print_rec(n)

# x = RecPrinter()
# x.print_rec(x.a)

def factorial(n):
    if n <= 1:
        return n
    return factorial(n-1) * n

# x = factorial(5)
# print(x)

def sum_upto(n):
    if n <= 1:
        return n
    return sum_upto(n-1) + n

# x = sum_upto(5)
# print(x) 

def fibonnaci_ite(n):
    fib_seq = [1,1]
    num = n-2
    while num != 0:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        num -= 1
    return fib_seq
# print(fibonnaci_ite(5))

def get_fibonnaci_rec(n):
    if n <= 2:
        return 1
    return get_fibonnaci_rec(n-1) + get_fibonnaci_rec(n-2)
# print(get_fibonnaci_rec(6))

def fibonnaci_rec_print(n, a=0, b=1, count=0):
    if count == n:
        return
    print(a)
    fibonnaci_rec_print(n, b, a+b, count+1)

fibonnaci_rec_print(10)


# while True:
#     print('true')

# clear python list
a = [1, 2, 3]
# a.clear() # OR

# del a[:]

# get index of an element

a.index(2) # returns 1
print(a.index(2))


import copy
a = [1,6,8,3,7,0]
b = copy.deepcopy(a)
a.clear()
print(a, b)

import random

a = random.randint(1, 4) # includes both end points

import os

x = os.getcwd()
print(x)



import datetime

print(datetime.datetime.now())

x = datetime.datetime.now()
print(x.date())
print(x.hour)
print(x.minute)
print(x.second)


import timeit

# Define a simple function to time
def my_function():
    return sum(range(1000))

# Time the function using timeit
execution_time = timeit.timeit(my_function, number=10000)

print(f"Execution time: {execution_time:.6f} seconds")
