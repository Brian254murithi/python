# While loop
number = 5
while number <= 10 :
    print(number)
    number += 1

# Decrement
number = 105
while number >= 100:
    print(number)
    number -= 1
# extra work
number = 100
while number <= 105:
    print(number)
    number += 1

# Break statement
x = 20
while x <= 25:
    print(x)
    if x == 24:
        break
    x += 1

# continue statement
y = 79
while y < 85:
    y += 1
    if y == 83:
        continue
    print(y)

# for loop
languages =["python","java","c++"]
for z in languages:
    print(z)

# Range
for mynumber in range(5):
    print(mynumber)

for mynum in range(2,6):
    print(mynum)


for count in range(20, 30, 2):
    print(count)