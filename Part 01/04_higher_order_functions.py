# Reduce must be imported
from functools import reduce

##  Higher Order Functions ##

def add_one(value):
    return value + 1

def add_two(value):
    return value + 5

def sum_two_values_and_add_one(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)

print(sum_two_values_and_add_one(5, 2, add_one))
print(sum_two_values_and_add_one(5, 2, add_two))

## Clousures ##

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add

add_clousure = sum_ten(1)
print(add_clousure(5))


## Built-in Higher Order Functions ##

numbers = [2, 5, 10, 21, 37]

# Map 

def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))

# Filter

def filter_greater_that_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_that_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))

# Reduce
# This function makes a secuence with the last add value and iterate it with the next value of "numbers"

def sum_two_values(first_value, second_value):
    return first_value + second_value

print(reduce(sum_two_values, numbers))