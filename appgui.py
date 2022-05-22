from tkinter import *
from tkinter import Tk
from tkinter import ttk


def main():
    root = Tk()
    root.title("Rower generator")
    root.geometry("800x620")

    # Define frames
    numberframe = LabelFrame(root, text="Number of rowers: ", padx=5, pady=5)
    genderframe = LabelFrame(root, text="Gender of rowers: ", padx=5, pady=5)

    # Define labels and entries for number
    numberlabel = Label(numberframe, text="Enter number: ")
    numberentry = Entry(numberframe, width=30)

    # Create dropdown menu for gender selection
    genderlist = ['Select one', 'Male', 'Female']
    gender = StringVar()
    genderlabel = Label(genderframe, text="Select gender: ")
    gendercombo = ttk.Combobox(genderframe, textvariable=gender, values=genderlist)
    gendercombo.current(0)
    gendercombo['state'] = 'readonly'

    # Set the labels and entries
    numberlabel.grid(row=0, column=0, sticky=NW)
    numberentry.grid(row=0, column=1, sticky=N)

    genderlabel.grid(row=0, column=0, sticky=NW)
    gendercombo.grid(row=1, column=0, sticky=W)

    # Set the frames
    numberframe.grid(row=0, column=0, padx=5, pady=5, sticky=NW)
    genderframe.grid(row=0, column=1, padx=5, pady=5, sticky=N)

    root.mainloop()


main()
