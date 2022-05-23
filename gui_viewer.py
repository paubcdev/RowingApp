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
        show_frame.grid_forget()
        fast_label = Label(show_frame, text="Fastest rowers: ")
        fastest_label = Label(show_frame, text=data_treatment.fastest)
        fast_label.grid(row=0, column=0)
        fastest_label.grid(row=1, column=1, sticky=NW)
        show_frame.grid(row=1, column=0, padx=5, pady=5, sticky=NW)

    def slow():
        show_frame.grid_forget()
        slow_label = Label(show_frame, text="Slowest rowers: ")
        slowest_label = Label(show_frame, text=data_treatment.slowest)
        slow_label.grid(row=0, column=0)
        slowest_label.grid(row=1, column=1, sticky=NW)
        show_frame.grid(row=1, column=0, padx=5, pady=5, sticky=NW)

    def heavy():
        show_frame.grid_forget()
        heavy_label = Label(show_frame, text="Heaviest rowers: ")
        heaviest_label = Label(show_frame, text=data_treatment.heaviest)
        heavy_label.grid(row=0, column=0)
        heaviest_label.grid(row=1, column=1, sticky=NW)
        show_frame.grid(row=1, column=0, padx=5, pady=5, sticky=NW)

    def light():
        show_frame.grid_forget()
        light_label = Label(show_frame, text="Lightest rowers: ")
        lightest_label = Label(show_frame, text=data_treatment.lightest)
        light_label.grid(row=0, column=0)
        lightest_label.grid(row=1, column=1, sticky=NW)
        show_frame.grid(row=1, column=0, padx=5, pady=5, sticky=NW)

    fast_button = Button(options_frame, text="Fastest", width=10, command=lambda: fast())
    slow_button = Button(options_frame, text="Slowest", width=10, command=lambda: slow())
    heavy_button = Button(options_frame, text="Heaviest", width=10, command=lambda: heavy())
    light_button = Button(options_frame, text="Lightest", width=10, command=lambda: light())

    fast_button.grid(row=0, column=0)
    slow_button.grid(row=0, column=1)
    heavy_button.grid(row=0, column=2)
    light_button.grid(row=0, column=3)

    options_frame.grid(row=0, column=0, padx=5, pady=5, sticky=NW)

    close = Button(root, text="Close", width=10, command=root.quit)
    close.grid(row=3, column=1, padx=5, pady=5, sticky=E)

    root.mainloop()


if __name__ == "__main__":
    root_main()
