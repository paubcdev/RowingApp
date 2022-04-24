# v0.1-5 rower generation process under construction, now generates 4 variables: name+surname, age, weight and
# a 2000m time, but just in seconds this time
import data_creator
import pandas as pd

if __name__ == "__main__":
    gender = input("What gender? ([m]ale, [f]emale) ")
    size = int(input("How many rowers you want to create? "))
    age_group = input("Which category? ([j]unior, [s]enior, [m]asters) ")

    name_list = data_creator.name_generator(gender, size)
    age_list = data_creator.age_generator(age_group, size)
    weight_list = data_creator.weight_generator(gender, size)
    two_thousand_list = data_creator.two_thousand_generator(gender, age_group, size)

    dic = {'name': name_list, 'age': age_list, 'weight': weight_list, '2000m time': two_thousand_list}
    df = pd.DataFrame(dic)

    print("DataFrame")
    print(df)
