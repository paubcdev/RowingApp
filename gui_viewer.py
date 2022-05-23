import data_treatment
from tkinter import *
from tkinter import Tk
# from tkinter import ttk


def root_main():
    root = Tk()
    root.title("Rower viewer")

    options_frame = LabelFrame(root, text="Options: ", padx=5, pady=5)
    show_frame = LabelFrame(root, text="", padx=5, pady=5)

    def fast():
        fast_label = Label(show_frame, text="Fastest rowers: ")
        fastest_label = Label(show_frame, text=data_treatment.fastest)
        fast_label.grid(row=0, column=0, sticky=NW)
        fastest_label.grid(row=1, column=1, sticky=NW)

    def slow():
        slow_label = Label(show_frame, text="Slowest rowers: ")
        slowest_label = Label(show_frame, text=data_treatment.slowest)
        slow_label.grid(row=0, column=0, sticky=NW)
        slowest_label.grid(row=1, column=1, sticky=NW)

    fast_button = Button(options_frame, text="Fastest", width=10, command=lambda: fast())
    slow_button = Button(options_frame, text="Slowest", width=10, command=lambda: slow())

    fast_button.grid(row=0, column=0)
    slow_button.grid(row=0, column=1)
    """buttons_list = [fast_button, slow_button]
    for i in buttons_list:
        a = 0
        i.grid(row=1, column=a, sticky=NW)
        a += 1"""

    options_frame.grid(row=0, column=0, padx=5, pady=5, sticky=NW)
    show_frame.grid(row=1, column=0, padx=5, pady=5, sticky=NW)

    close = Button(root, text="Close", width=10, command=root.quit)
    close.grid(row=3, column=1, sticky=E)

    root.mainloop()


if __name__ == "__main__":
    root_main()
