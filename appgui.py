from tkinter import *
from tkinter import Tk
from tkinter import ttk
# import dataframe_creator


def root_main():
    root = Tk()
    root.title("Rower generator")
    # root.geometry("800x400")

    def print_test(siz):
        print(siz)

    # Define frames
    number_frame = LabelFrame(root, text="Number of rowers: ", padx=5, pady=5)
    gender_frame = LabelFrame(root, text="Gender of rowers: ", padx=5, pady=5)
    category_frame = LabelFrame(root, text="Category of rowers: ", padx=5, pady=5)

    # Define labels and entries for number
    number_label = Label(number_frame, text="Enter number: ")
    number_entry = Entry(number_frame, width=10)

    # Create dropdown menu for gender selection
    gender_list = ['Select one', 'Male', 'Female']
    gender = StringVar()
    gender_label = Label(gender_frame, text="Select gender: ")
    gender_combo = ttk.Combobox(gender_frame, textvariable=gender, values=gender_list)
    gender_combo.current(0)
    gender_combo['state'] = 'readonly'

    # Create dropdown menu for category selection
    cat_list = ['Select one', 'Junior', 'Senior', 'Masters']
    category = StringVar()
    category_label = Label(category_frame, text="Select category: ")
    category_combo = ttk.Combobox(category_frame, textvariable=category, values=cat_list)
    category_combo.current(0)
    category_combo['state'] = 'readonly'

    # Set the labels and entries
    number_label.grid(row=0, column=0, sticky=NW)
    number_entry.grid(row=0, column=1, sticky=N)

    gender_label.grid(row=0, column=0, sticky=NW)
    gender_combo.grid(row=1, column=0, sticky=W)

    category_label.grid(row=0, column=0, sticky=NW)
    category_combo.grid(row=1, column=0, sticky=W)

    # Set the frames
    number_frame.grid(row=0, column=0, padx=5, pady=5, sticky=NW)
    gender_frame.grid(row=0, column=1, padx=5, pady=5, sticky=N)
    category_frame.grid(row=1, column=0, padx=5, pady=5, sticky=NW)

    # Define and set the buttons
    calculate = Button(root, text="Calculate", width=10, command=lambda: print_test(int(number_entry.get())))
    close = Button(root, text="Close", width=10, command=root.quit)
    calculate.grid(row=2, column=1, sticky=E)
    close.grid(row=3, column=1, sticky=E)

    # Run the gui
    root.mainloop()


if __name__ == "__main__":
    root_main()
