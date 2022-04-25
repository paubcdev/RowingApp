import random
from constants import MALE_NAMES, FEMALE_NAMES, SURNAMES


def name_generator(gender, size):
    name = []
    for i in range(0, size):
        # picks a name at random from the list of names in the constant and appends it to the output list
        if gender == 'male' or gender == 'm':
            rand_index = random.randint(0, (len(MALE_NAMES)-1))  # because of list indexing, the actual length is 1 less
            name_surname = MALE_NAMES[rand_index] + " " + SURNAMES[rand_index] + "."
            name.append(name_surname)
        elif gender == 'female' or gender == 'f':
            rand_index = random.randint(0, (len(FEMALE_NAMES)-1))  # same as before
            name_surname = FEMALE_NAMES[rand_index] + " " + SURNAMES[rand_index] + "."
            name.append(name_surname)
        else:
            raise TypeError("Please specify a valid gender")
    return name


def age_generator(age_group, size):
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


def weight_generator(gender, size):
    weight = []
    for i in range(0, size):
        if gender == 'male' or gender == 'm':
            weight.append(round(random.uniform(70.0, 110.9), 2))
        elif gender == 'female' or gender == 'f':
            weight.append(round(random.uniform(60.0, 90.0), 2))
    return weight


def two_thousand_generator(gender, age_group, size):
    two_thousand_sec = []
    for i in range(0, size):
        if gender == 'male' or gender == 'm':
            if age_group == 'junior' or age_group == 'j':
                two_thousand_sec.append(random.randrange(390, 480))
            elif age_group == 'senior' or age_group == 's':
                two_thousand_sec.append((random.randrange(350, 460)))
            elif age_group == 'masters' or age_group == 'm':
                two_thousand_sec.append((random.randrange(400, 500)))
        elif gender == 'female' or gender == 'f':
            if age_group == 'junior' or age_group == 'j':
                two_thousand_sec.append(random.randrange(400, 490))
            elif age_group == 'senior' or age_group == 's':
                two_thousand_sec.append((random.randrange(360, 470)))
            elif age_group == 'masters' or age_group == 'm':
                two_thousand_sec.append((random.randrange(410, 510)))
    two_thousand = []
    for j in two_thousand_sec:
        m, s = divmod(j, 60)
        min_sec = f"{m}:{float(s)}"
        two_thousand.append(min_sec)
    return two_thousand

