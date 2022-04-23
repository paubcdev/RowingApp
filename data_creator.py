import random
from constants import MALES, FEMALES
name = []
age = []
genders = []
weight = []

gender = input("What gender? ([m]ale, [f]emale) ")
size = int(input("How many? "))
age_group = input("Which category? ([j]unior, [s]enior, [m]asters) ")

for i in range(0, size):
    # picks a name at random from the list of names in the constant and appends it to the output list
    if gender == 'male' or gender == 'm':
        name.append(MALES[random.randint(0, len(MALES))])
    elif gender == 'female' or gender == 'f':
        name.append(FEMALES[random.randint(0, len(FEMALES))])
    else:
        raise TypeError("Please specify a valid gender")

for i in range(0, size):
    # picks an age at random from the specified age group
    if age_group == 'junior' or age_group == 'j':
        age.append(random.randrange(16, 18))
    elif age_group == 'senior' or age_group == 's':
        age.append(random.randrange(19, 35))
    elif age_group == 'masters' or age_group == 'm':
        age.append(random.randrange(36, 99))
    else:
        raise TypeError("Please specify a valid category.")

for i in range(0, size):
    weight.append(round(random.uniform(70.0, 110.9), 2))

print(name)
print(age)
print(weight)
