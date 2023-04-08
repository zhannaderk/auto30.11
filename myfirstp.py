print("Hello, World!")

if 4 > 2:
    print("Four is greater than two!")

# This is a comment
print("Привіт, світе!")

# variables
x = 1  # x is type of integer
y = "Jane"  # 'Jane' is type of string
z = 1.1  # z is type of float
print(x)
print(y)
print(z)

# casting
x = str(1)  # x will be '1'
y = int(1)  # y will be 1
z = float(1)  # z will be 1.0
print(x, y, z)
print(type(x))

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = 5
y = 10
print(x * y)

x = 5
print(type(x))

x = int(1)  # x will be ..
y = int(2.8)  # y will be ..
z = int("3")  # z will be ..
print(x, y, z)

a = """I
like
programming"""
print(a)

a = "Hello"
b = "World"
c = a + b
print(c)

age = 30
wer = "My name is Jane, and I am {}"
print(wer.format(age))

print(4 > 2)
print(1 == 9)
print(100 < 9)

a = 1
b = 100
if b > a:
    print("b is greater than a")

a = 50
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
elif a > b:
    print("a is greater than b")

age = 11
if age == 6:
    print('Ти в першому класі')
elif age == 7:
    print('Ти в другому класі')
elif age == 8:
    print('Ти в третьому класі')
else:
    print('Не час ходити до початкової школи')

a = 17
b = 18
if b > a:
    print("You are so young")
elif a == b:  # ??
    print('You are 18')
else:
    print("You are allowed")

print("Хочеш почути брудний жарт?")
age = 12
if age >= 12:
    print("Порося впало в багнюку!")
else:
    print("Поки що це серкрет!")

age = 6
if age == 6 or age == 7 or age == 8:
    print("Ти в початковій школі")
else:
    print('Не час ходити до початкової школи')

mylist = ["apple", "banana", "cherry"]
print(mylist)

список_чарівника = ['павукові лапки', 'язик змії', 'крило кажана']
for i in список_чарівника:
    print(i)

mylist = ["apple", "banana", "cherry", "apple", "cherry"]
print(mylist)

mylist = ["apple", "banana", "cherry"]
print(mylist[0])

mylist = ["apple", "banana", "cherry"]
print(mylist[-1])

mylist = ["apple", "banana", "cherry", "pineapple"]
mylist[1] = "avocado"
print(mylist)

mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(mylist[2:5])

mylist = ["apple", "banana", "cherry"]
mylist.append("orange")
print(mylist)

mylist = ["apple", "banana", "cherry"]
mylist.insert(1, "avocado")
print(mylist)

mylist = ["apple", "banana", "cherry"]
mylist.remove("apple")
print(mylist)

i = 1
while i < 10:
    print(i)
    i += 1


def my_function():
    print("Hello")

