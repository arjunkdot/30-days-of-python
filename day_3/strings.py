# Concatenate
string = "Thirty " + "Days " + "Of " + "Python"
print(string)

string_one = "Coding " + "For " + "All"
print(string_one)

company = string_one
print(company)

# Convert case
print(company.upper())
print(company.lower())
print(company.capitalize().title().swapcase())

# Slice
print(company[0:6])

# Find
print(company.find("Coding"))

# Replace
company = company.replace("Coding", "Python")
print(company)

company = company[0:10] + " Everyone"
print(company)

# Split
print(company.split(" "))

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
companies = companies.split(",")

print(company[0])
print(f'Last index is {len(company) - 1}, and character is {company[-1]}')
print(company[10])
print(company[0:18:4])
print(company[0:14:4])

sentence = "You cannot end a sentence with because because because is a conjunction"
fIndex = sentence.index("because")
lIndex = sentence.rindex("because")

print(fIndex)
print(lIndex)
print(sentence[fIndex:lIndex + 8])

print("Coding For All".index("Coding") == 0)
print("   Coding For All      ".replace("\t", ""))

print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

print("I am enjoying this challenge.\nI just wonder what is next.")

print("Name\tAge\tCountry\tCity\nArjun\t1000\tIndia\tVizag")

radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

print(f"{8} + {6} = {8 + 6}")
print(f"{8} - {6} = {8 - 6}")
print(f"{8} * {6} = {8 * 6}")
print(f"{8} / {6} = {8 / 6}")
print(f"{8} % {6} = {8 % 6}")
print(f"{8} // {6} = {8 // 6}")
print(f"{8} ** {6} = {8 ** 6}")
