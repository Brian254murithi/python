# inbuilt functions
number = max(89,70,12,45,123)
print(number)

x = min(75,36,26,257)
print(x)

z = pow(2,3)
print(z)

# user defined function
def details():
    print("brian")

details() # calling a functions

def students():
    name = "brian"
    age = 19
    course = "MIT"
    print(name,age,course)

students()

# parameters
def students(name, age, course):
    print(name, age, course)

students("vincent", 18, "MIT")
students("vincent", 18, "MIT")
students("vincent", 18, "MIT")
students("vincent", 18, "MIT")
students("vincent", 18, "MIT")

# create a user-defined function
def employees(fullname, age, gender, position, salary):
    print(fullname, age, gender, position, salary)

employees("Brian Murimi", 19, "Male","Accountant", "Ksh 100,000")
employees("Morris Mutwiri", 20, "Male","CEO", "Ksh 200,000")
employees("Edwin Mbui", 20, "Male","Baser", "Ksh 70,000")
employees("Angela Wanjiru", 19, "Female","Secretary", "Ksh 100,000")
employees("Yvonne Wambui", 19, "Female","caretaker", "Ksh 50,000")
