def input_data():
    print("Rower data creator. v0.1.6")
    print("--------------------------")
    size = int(input("How many rowers you want to create? "))
    gender = input("Gender of the rowers? ([m]ale, [f]emale) ")
    age_group = input("From category? ([j]unior, [s]enior, [m]asters) ")

    return gender, size, age_group
