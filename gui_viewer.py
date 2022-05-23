import data_treatment
from tkinter import *
from tkinter import Tk
from tkinter import ttk


def root_main():
    root = Tk()
    root.title("Rower viewer")

    options_frame = LabelFrame(root, text="Options: ", padx=5, pady=5)

    fast_label = Label(options_frame, text="Fastest rowers: ")
    fastest_label = Label(options_frame, text=data_treatment.fastest)
    fast_label.grid(row=0, column=0, sticky=NW)
    fastest_label.grid(row=1, column=1, sticky=NW)

    options_frame.grid(row=0, column=0, padx=5, pady=5, sticky=NW)

    close = Button(root, text="Close", width=10, command=root.quit)
    close.grid(row=3, column=1, sticky=E)

    root.mainloop()


if __name__ == "__main__":
    root_main()
