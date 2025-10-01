# 26-09-2025 - Assignment
# With the help of the python documentation understand and provide with working examples on how to
# use the below functions
# filter
# enumerate
# zipformat
# slice

# Enumerate
from idlelib.outwin import OutputWindow

Seasons = ['Fall','Spring','Summer','Autumn','Winter']
All_Seasons = list(enumerate(Seasons))
print(All_Seasons)

# output
# [(0, 'Fall'), (1, 'Spring'), (2, 'Summer'), (3, 'Autumn'), (4, 'Winter')]

#*******************************************************************************

# Zip

for item in zip([1,2,3,4,5],['Fall','Spring','Summer','Autumn','Winter']):(item)

# Output
# (1, 'Fall')
# (2, 'Spring')
# (3, 'Summer')
# (4, 'Autumn')
# (5, 'Winter')

list(zip(range(3), ['Fall','Spring','Summer','Autumn','Winter']))

# Output
# [(0, 'Fall'), (1, 'Spring'), (2, 'Summer')]

# Using zip and * to Unzip a list

list_num = [1,2,3]
list_seasons = ['Autumn','Spring', 'Summer']
list(zip(list_num,list_seasons))

# output
# [(1, 'Autumn'), (2, 'Spring'), (3, 'Summer')]

*******************************************************************************

# Format

# Basic Usage
name = "Tanuj"
print("Hello, {}!".format(name))

# Output
# Hello, Tanuj!

# Multiple Placeholder
name = "Tanuj"
age = 26
print("Name: {}, Age: {}".format(name,age))

# Output
# Name: Tanuj, Age: 26

# Named placeholder

print ("Name: {name}, Age: {age}".format(name="Tanuj", age=26))

# Output
# Name: Tanuj, Age: 26

#Format numbers

print("pi is approximately {:.3f}".format(pi))

# output
# pi is approximately 3.14

*******************************************************************************

# Slice

# Basic usage
Seasons = ['Fall','Spring','Summer','Autumn','Winter']
print(Seasons[1:3])

# output
# ['Spring', 'Summer']

# Using step arg

Seasons = ['Fall','Spring','Summer','Autumn','Winter']
print(Seasons[::2])

# Output
# ['Fall', 'Summer', 'Winter']

# Negative index

Seasons = ['Fall','Spring','Summer','Autumn','Winter']
print(Seasons[-2:])

# output
# ['Autumn', 'Winter']

# Reverse a list using slice

Season = "Summer"
print(Season[::-1])

# output
# remmuS

*******************************************************************************

# Filter

Seasons = ['Fall','Spring','','Summer','Autumn','','Winter','']
non_emp = filter(None,Seasons)
print(list(non_emp))

