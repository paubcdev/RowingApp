import dataframe_creator


def exporter():
    print("To what format?")
    sel = input("CSV, Excel: ")
    if sel == 'csv' or sel == 'CSV':
        dataframe_creator.df.to_csv('rowers.csv')
        print("Saved as CSV!")
    elif sel == 'excel' or sel == 'EXCEL' or sel == 'Excel':
        dataframe_creator.df.to_excel('rowers.xlsx')
        print("Saved as Excel!")
