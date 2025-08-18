
import math

age = 1000
height = 172.05
cmplx = 4 + 4j

def print_area():
    base = float(input('Enter base: '))
    height = float(input('Enter height: '))
    print('The area of the triangle is: ', 0.5 * base * height)

def print_perimeter():
    side_a = float(input('Enter side A: '))
    side_b = float(input('Enter side B: '))
    side_c = float(input('Enter side C: '))
    print('The perimeter of triangle is: ', side_a + side_b + side_c)

def print_rect_area():
    length = float(input('Enter length: '))
    width = float(input('Enter width: '))
    print('The area of rectangle is: ', length * width)

def print_circle():
    radius = float(input('Enter radius: '))
    print('The area of circle is: ', math.pi * radius ** 2)

def print_slope(): 
    x1 = float(input('Enter x1: '))
    x2 = float(input('Enter x2: '))
    y1 = float(input('Enter y1: '))
    y2 = float(input('Enter y2: '))
    print('The slope is: ', (y2 - y1) / (x2 - x1))
    print('The Euclidean distance is:', math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))

print(len('python') != len('dragon'))
print('jargon' in 'I hope this course is not full of jargon.')

strlen = str(float(len('Python')))

def is_even():
    num = int(input('Enter number: '))
    print("is even" if num % 2 == 0 else "is odd")

print(type('10') != type(10))

def calculate_pay():
    hours = float(input('Enter hours: '))
    rate = float(input('Enter rate per hour: '))
    print('Your weekly earning is: ', hours * rate)

def seconds_lived():
    years = int(input('Enter number of years you have lived: '))
    print('You have lived for', years * 60 * 60 * 24 * 365, 'seconds')

def print_table():
    for i in range(1, 6):
        print(f"{i:<2} 1  {i:<2} {i**2:<3} {i**3}")

print_area()
print_perimeter()
print_rect_area()
print_circle()
print_slope()
is_even()
calculate_pay()
seconds_lived()
print_table()
