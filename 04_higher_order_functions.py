##  Higher order functions ##

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
