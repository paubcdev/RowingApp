import data_creator

if __name__ == "__main__":
    gender = input("What gender? ([m]ale, [f]emale) ")
    size = int(input("How many? "))
    age_group = input("Which category? ([j]unior, [s]enior, [m]asters) ")

    print(data_creator.name_generator(gender, size))
    print(data_creator.age_generator(age_group, size))
    print(data_creator.weight_generator(size))
