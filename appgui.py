from tkinter import *
from tkinter import Tk
from tkinter import ttk


def root_main():
    root = Tk()
    root.title("Rower generator")
    # root.geometry("800x620")

    # Define frames
    number_frame = LabelFrame(root, text="Number of rowers: ", padx=5, pady=5)
    gender_frame = LabelFrame(root, text="Gender of rowers: ", padx=5, pady=5)

    # Define labels and entries for number
    number_label = Label(number_frame, text="Enter number: ")
    number_entry = Entry(number_frame, width=30)

    # Create dropdown menu for gender selection
    gender_list = ['Select one', 'Male', 'Female']
    gender = StringVar()
    gender_label = Label(gender_frame, text="Select gender: ")
    gender_combo = ttk.Combobox(gender_frame, textvariable=gender, values=gender_list)
    gender_combo.current(0)
    gender_combo['state'] = 'readonly'

    # Set the labels and entries
    number_label.grid(row=0, column=0, sticky=NW)
    number_entry.grid(row=0, column=1, sticky=N)

    gender_label.grid(row=0, column=0, sticky=NW)
    gender_combo.grid(row=1, column=0, sticky=W)

    # Set the frames
    number_frame.grid(row=0, column=0, padx=5, pady=5, sticky=NW)
    gender_frame.grid(row=0, column=1, padx=5, pady=5, sticky=N)

    # Run the gui
    root.mainloop()


root_main()
