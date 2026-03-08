
# bool
# int
# float
# str
# list
# set
# fun

# tuple -- frozen -- immutable
number = (10,)
print(number)

numbers = (10, 20, 30)
print(numbers)

fruits = ("apple", "banana", "orange")
print(fruits)

scores = (100, 95, 87)

# scores.sort()  # ERROR
print(tuple(sorted(scores)))

person = ("Alice", 25, "Teacher")
print(person)

animals = "dog", "cat", "lion"
animals = ("dog", "cat", "lion")

print(animals[0])
print(animals[1])

a=1
b=2
a, b = b, a
print(a, b)

colors = ("red", "green", "blue", "yellow")
print(colors[-1])
print(colors[::-1])
print(colors[::2])

flags = (False, False, True)
print(any(flags))
numbers = (1, 7, 5, 11, 3, 6, -1)
print(any(x % 2 == 0 for x in numbers))
print(all(x % 2 == 0 for x in numbers))
print(all(len(color) >= 3 for color in colors))

cars = ("Tesla", "Tesla", "Mitsubishi", "Honda")
print(len(cars))

animals = ("dog", "cat", "lion")
for animal in animals:
    print(animal)
for i in range(len(animals)):
    print(animals[i])
print(len(animals[0]))

print(cars)
print([len(word) for word in cars])  # comprehension
# cars[0] = 'new'  # Error
# cars.add('fiat')

numbers = (1, 2, 3, 2, 2, 5)
print(numbers.count(2))

l1 = []
for x in range(1, 100 + 1):
    l1.append(x)
tuple_1_100 = tuple(l1)

#          0  1  2  3  4   5    6
numbers = (5, 8, 3, 9, 3, 99, 100)
print(numbers.index(3, 3, 5))

numbers = (5, 10, 15, 30)
print(max(numbers))

numbers = (5, 10, 15)
print(min(numbers))

numbers = (9, 3, 7, 1)
print(sorted(numbers))

days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
print(days)

t1 = (10, [1,2,3], 'hi', {1, 2}, (3, 4), True)
print(t1)
print([1,2,3] in t1)

# 1 create tuple with 3 of your favorite movies
# 2 create tuple with all countries in Europe (ask ChatGPT)
# 3 create tuple with all the days of feb (1, 2 ... 28)
# 4 create tuple with all the days of dec (1, 2 .. 31)

# EXTRA -- BONUS
#days_dec = tuple(range(1, 31 + 1))
#days_dec = (x for x in range(1, 31 + 1))
#print(days_dec)

# 5 create tuple of all the month in the year
# 6 create tuple of all USA presidents till today (ask ChatGPT), use len to find out how many are they
# 7 use mean to find the avg of this tuple = (8, 11, -3, 12)

# write a function that gets numbers and return  the max number in a tuple
def get_max(lst1: list) -> tuple:
    pass
# [5, 0, 55, -8, 49] -> (55,)

'''
The Challenge: "The Social Bridge"
Write a function called get_shared_interests that takes two lists of strings as input (e.g., interests of Person A and Person B).
The function should:

**bonus: Identify only the interests that both people share, using a set for an efficient comparison, or set functions

Return a tuple containing:
The sorted list of shared interests
The integer count of how many interests they have in common
Input:
  person_a = ["coding", "hiking", "cooking", "surfing"]
  person_b = ["hiking", "gaming", "coding"]
Output: 
  (['coding', 'hiking'], 2)

def find_common(person_a, person_b) -> tuple(list, int):
    pass

'''






