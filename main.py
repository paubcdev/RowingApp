# v0.1.6 rower generation process under construction, now generates 4 variables: name+surname, age, weight and
# a 2000m time, but just in seconds this time
import dataframe_creator
import data_treatment

if __name__ == "__main__":
    print("DataFrame:")
    print(dataframe_creator.df)

    print("Slowest rower: ")
    print(data_treatment.slowest)

    print("Fastest rower: ")
    print(data_treatment.fastest)
