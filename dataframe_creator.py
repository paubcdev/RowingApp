from main import gender, age_group, size
import data_creator
import pandas as pd

name_list = data_creator.name_generator(gender, size)
age_list = data_creator.age_generator(age_group, size)
weight_list = data_creator.weight_generator(size)
dic = {'name': name_list, 'age': age_list, 'weight': weight_list}

df = pd.DataFrame(dic)
