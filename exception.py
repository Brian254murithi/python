try:
    print(x)
except:
    print("Name Error occurred")
finally:
    print("Success")

num1 = 20
num2 = 0

try:
    print(num1 / num2)


except:
    print("Zero division error occurred")

# user-defied function
try:
    def multiply(x, y):
        return x * y
except:
    print("Exception occurred")

finally:
    print("success")
print(multiply(10 , 20))


# types of block (try block, except block, finally block)