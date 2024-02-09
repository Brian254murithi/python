# Data type
number = 45 # int
num = 56.78 # float
greeting = "Hello there" # str
is_python_interesting = True # bool

# variable storing multiple values
languages = ["python" , "php" , "java"] # list
fruits = ( "apple","banana","pineapple") # tuple
countries = {"Kenya","Chaina","USA"} # set

# Dictionary
details = {
    "firstname" : "Grace",
    "Age" : 17,
    "Course" : "MIT",
    "Nationality" : "North America"
}

# variable
print(details["Course"])
print(details["Nationality"])
print(number)
print(greeting)
print(countries)
print(is_python_interesting)

# Determining the data type
print(type(details))
print(type(countries))

# type casting - Converting one data type to another
print(float(number))
print(int(num))