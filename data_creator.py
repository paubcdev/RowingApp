import random
from constants import MALE_NAMES, FEMALE_NAMES, SURNAMES


def name_generator(gender, size):
    name = []
    for i in range(0, size):
        # picks a name at random from the list of names in the constant and appends it to the output list
        if gender == 'male' or gender == 'm':
            rand_index = random.randint(0, len(MALE_NAMES))
            name_surname = MALE_NAMES[rand_index] + " " + SURNAMES[rand_index] + "."
            name.append(name_surname)
        elif gender == 'female' or gender == 'f':
            rand_index = random.randint(0, len(FEMALE_NAMES))
            name_surname = FEMALE_NAMES[rand_index] + " " + SURNAMES[rand_index] + "."
            name.append(name_surname)
        else:
            raise TypeError("Please specify a valid gender")
    return name


def age_generator(size):
    age = []
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
    return age


def weight_generator(size):
    weight = []
    for i in range(0, size):
        weight.append(round(random.uniform(70.0, 110.9), 2))
    return weight


gender_ = input("What gender? ([m]ale, [f]emale) ")
size_ = int(input("How many? "))
age_group = input("Which category? ([j]unior, [s]enior, [m]asters) ")

print(name_generator(gender_, size_))
print(age_generator(size_))
print(weight_generator(size_))
