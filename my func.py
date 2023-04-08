print(abs(-5))

a = "I'm string"
print(dir(a))

print(eval("3*3"))

print(float("12"))

print(int("12"))

print(len("Please calculate me"))

alist = ["dog", "cat", "horse", "rabbit"]
print(len(alist))

numbers = [34, 6, 789, 5, 1]
print(max(numbers))

print(max(11, 111, 1111, 111111))

for x in range(0, 10, 2):
    print(x)

for x in range(20, 0, -2):
    print(x)

alist = [1, 2, 3, 4]
print(sum(alist))

alist = list(range(0, 200, 50))
print(alist)

print(sum(alist))

def say_hello(what_is_your_name):
    print("Привіт", what_is_your_name)

say_hello("Кристина")

def budjet(sallary, savings, expencies):
    return sallary + savings - expencies
print((budjet(10000, 5000, 10000)))

new_list = [1, 2, 3]
print(sum(new_list))

sum_1 = 0
for num in new_list:
    sum_1 += num
print(sum_1)

def function_name():
    print(function_name())


