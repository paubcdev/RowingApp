# v0.1.8 rower generation engine, with basic data treatment and export capabilities
import dataframe_creator
from data_selector import selector
from data_exporter import exporter

if __name__ == "__main__":
    print("DataFrame:")
    print(dataframe_creator.df)
    sel = input("Do you want to export the data? (yes, no) ")
    if sel == 'no' or sel == 'n' or sel == 'N' or sel == 'No':
        print(selector())
    else:
        exporter()
