from tkinter import *
from tkinter import Tk
from tkinter import ttk


def main_root():
    root = Tk()
    root.title("Rowing App v0.2.1")
    root.geometry("500x250")

    # Define frames
    menu_frame = LabelFrame(root, text="Options", padx=5, pady=5)
    info_frame = LabelFrame(root, text="Info", padx=5, pady=5)

    # Define labels
    author_info = Label(info_frame, text="Made by:\nPau 'paubcdev' \nblanescolomina.pau@gmail.com", justify="left")

    # Define and set buttons
    generator = Button(menu_frame, text="Rower generator")
    generator.grid(row=0, column=0)

    viewer = Button(menu_frame, text="Rower viewer")
    viewer.grid(row=0, column=1)

    close = Button(info_frame, text="Close", width=10, command=root.quit)
    close.grid(row=1, column=1)

    # Set labels
    author_info.grid(row=0, column=0)

    # Set frames
    menu_frame.grid(row=0, column=0, pady=5, padx=5, sticky=NW)
    info_frame.grid(row=3, column=0, padx=5, pady=5, sticky=NW)

    # Run the gui
    root.mainloop()


if __name__ == "__main__":
    main_root()
