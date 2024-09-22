

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