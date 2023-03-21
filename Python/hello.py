print("Mohan")

a= 3+8j
z=complex(3,7)
print(a)
print(z)

print('"Mohan"')

y=str(z)
print(y)

l=str(3+4j)
print(l)


k=str([1,1])
print(k)

k=k+'564'
print(k)

print(k[1])
print(k[0])

S = 'ABCDEFGHI'
print(S[1:8:3])
print(S[1:5:2])
print(S[1:-1:-2]+"gukc")
# print(S[1:-1:0]+"gukc")   Zero can't be used



p = 'Hello, world!'
print(p[2:8])

new_p = 'J' + p[2:8]
new_p1 ='t'+ p[1:]

print(new_p)
print(new_p1)


w='Hi'
w+=' Sir'
print(w)

e=20*'Hi '
print(e)
print(len(e))
r=e.replace('Hi','Hello')
print(r)
print(len(r))
print(r.find('Hello'))


s="My name    is      Mohan"
x = s.split()
print(x)
for xs in x:
    print(xs)

print(s.find('Hi'))
print(s.find('Mohan'))
print(s)
for letter in s:
    print(letter,end='')

print(s)

from pickle import FALSE
import random
import string

# LETTERS =string.ascii_letters
# NUMS= '0123456789'
# SPE='!@#$%^&*()_+=-'
# SYMBOLS= LETTERS+NUMS+SPE
# len=int(input("ENTER PASS.LENGTH:"))
# password="".join(random.sample(SYMBOLS,len))
# print(password)


my_list = ["mouse", [8, 4, 6], ['a']]

print(my_list[:])
print(my_list[1][2])
print(my_list[:-2])
print(my_list[1][:-2])

my_list[1][1:2]=[3,9]
print(my_list)
my_list[1][1:5]=[7,7,7]
print(my_list)

my_tuple=(1,'a',"hi",3)
print(my_tuple)

# my_tuple[1:3]=(1,2,2)   error 

p = 'red,green,blue,yellow'
print(p)
l = p.split(',')
print(l)
k=','.join(l)
print(k)

my_list.insert(1,8)
print(my_list)


pow2 = [2 ** x for x in range(10)]
print(pow2)

pow2= [x for x in range(20) if x % 2 == 1]
print(pow2)


my_set = {1, 3}
print(my_set)

my_set.add(2)
print(my_set)

my_set.update([2,3,4,5,5,6])
print(my_set)

my_set.discard(4)
print(my_set)

my_set.remove(2)
print(my_set)

my_set.pop()
print(my_set)

vowels = ('a', 'e', 'i', 'o', 'u')

fSet = frozenset(vowels)
print('The frozen set is:', fSet)
# fSet.add('v')
# print('The frozen set is:', fSet)

def absolute_value(num):
    """This function returns the absolute
    value of the entered number"""

    if num >= 0:
        return num
    else:
        return -num

print(absolute_value(2))

print(absolute_value(-4))

def greet(*names):
    """This function greets all
    the person in the names tuple."""

    # names is a tuple with arguments
    for name in names:
        print("Hello", name )


greet("Avdhesh", "Neelam", "Harsh", "Garvit")


def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

num=int(input("Number:"))
print("The factorial of", num, "is", factorial(num))


my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

print(new_list)

new_list = list(map(lambda x: x * 2 , my_list))

print(new_list)



x = 3.14159

def foo():
    x=3.14
    print("x inside:", x)


foo()
print("x outside:", x)


num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)


from Employee import Employee

employee1=Employee('Mohan','Python',50000,FALSE)

print(employee1.name)