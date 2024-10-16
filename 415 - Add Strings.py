import math
num1 = "123"
num2 = "34"
value = []
sum = 0
for i in num1:
    value.append(ord(i))
for i in num2:
    value.append(ord(i))
for i in value:
    sum += i
print(type(sum))