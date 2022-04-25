import data_creator
import input_data
import pandas as pd

gender, size, age_group = input_data.input_data()

name_list = data_creator.name_generator(gender, size)
age_list = data_creator.age_generator(age_group, size)
weight_list = data_creator.weight_generator(gender, size)
two_thousand_list = data_creator.two_thousand_generator(gender, age_group, size)

dic = {'name': name_list, 'age': age_list, 'weight': weight_list, '2000m time': two_thousand_list}
df = pd.DataFrame(dic)