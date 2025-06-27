#### MASTERING LOOPS IN PYTHON ####
"""
The only reason I had to include this section is that things were getting messy as I forgot much information I already covered.
This is completely normal, and I am sure you will also forget some information as you progress.
So, it is okay to revisit topics and refresh your memory.
This section is a summary of loops in Python, including for loops, while loops, range, and iterators.
"""

### Loops in Python ###
"""
Loops allow us to repeat a block of code multiple times until a certain condition is met. 
In Python, we have two types of loops: for loops and while loops. The type of loop to use depends totally on your problem set. 
The two types of loops (in python) are described with examples below.
"""

### For Loops in Python ###
"""
For loops are used to iterate over a sequence (like a list, tuple, or string) or any iterable object.
"""

### Example of a for loop ###
numbers = [1, 2, 3, 4, 5]

for number in numbers: # This is a for loop that iterates over each element in the numbers list.
    print(number) # This prints each number in the list.
print("________________________________________")


# Another example of using a for loop. 
"""
Imagine that we have a list of temperatures in Celsius and want to convert them into Fahrenheit
"""
temperatures_celsius = [22, 25, 17, 15, 18]
temperatures_fahrenheit = []

for temp in temperatures_celsius:
    temperatures_fahrenheit.append((temp * 9/5) + 32)

print(temperatures_fahrenheit)
print("________________________________________")


### Nested For Loops in Python ###
"""
Nested for loops allow us to iterate over multiple sequences or perform operations that require multiple iterations.
"""
sensors = ["Temperature", "Humidity", "Pressure"]
days = ["Monday", "Tuesday", "Wednesday"]

for sensor in sensors:
    for day in days:
        print(f"Reading {sensor} on {day}")
print("________________________________________")

    
### You can also use the range() function to generate a sequence of numbers. ###
numbers_range = range(5)

for number in numbers_range:
    print(number)  # This prints numbers from 0 to 4 (5 is not included).
print("________________________________________")



### The range function can also take three arguments: start (optional), stop (required), and step (optional). ###
# In the above example, we can change the range to start from 1 and go up to 5.

numbers_range = range(1, 6)  # This generates numbers from 1 to 5 (6 is not included).

for number in numbers_range:
    print(number)  # This prints numbers from 1 to 5.
print("________________________________________")


numbers_collection_range = range(1, 11, 2)  # This generates numbers from 1 to 10 with a step of 2.

for number in numbers_collection_range:
    print(number)  # This prints odd numbers from 1 to 9.
print("________________________________________")



### While Loops in Python ###
"""
A while loop executes a block of code as long as a certain condition is True.
"""

count = 10

while count > 0:
    print(count)  # This prints the current value of count.
    count -= 1  # This decreases the value of count by 1 in each iteration
print("_________________________________________")





fruits = ["apple", "orange", "kiwi"]
iter_obj = iter(fruits)
while True:
    try:
        fruit = next(iter_obj)
        print(fruit)
    except StopIteration:
        break