from Utils.function_call_count import count_calls

@count_calls
def print_sth():
    print("Hello, World!")

@count_calls
def another_function():
    print("Called another function")

print_sth()
print_sth()
print_sth()

another_function()
another_function()

"""
print_sth has been called 1 times
Hello, World!
print_sth has been called 2 times
Hello, World!
print_sth has been called 3 times
Hello, World!
another_function has been called 1 times
Called another function
another_function has been called 2 times
Called another function

"""