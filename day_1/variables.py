import math

# Day 1: 30 Days of python programming

first_name = 'Arjun'
last_name = 'K.'
full_name = first_name + last_name
country = 'India'
city = 'Vizag'
age = 1000
year = 2025
is_married, is_true, is_light_on = True, True, False

# Check data type of the variables

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

# Find length of first_name

print(len(first_name))

# Compare length of first_name & last_name

print(len(first_name) - len(last_name))

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

# Calculations

radius = 30
area_of_circle = math.pi * (radius ** 2)
print('Area of circle: ', area_of_circle)
circum_of_circle = 2 * math.pi * radius
print('Circumference of circle: ', circum_of_circle)

# Calculate area with user input

def calculate_area(radius):
    return math.pi * (radius ** 2)

user_radius = input('Enter the radius of the circle: ')
print(calculate_area(float(user_radius)))

user_first_name = input('Enter your first name: ')
user_last_name = input('Enter your last name: ')
user_country = input('Enter your country: ')
user_age = input('Enter your age: ')

print('Your inputs: ', user_first_name, user_last_name, user_country, user_age);

