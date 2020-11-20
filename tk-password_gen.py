

from tkinter import *
from tkinter import ttk
from string import ascii_lowercase
from string import ascii_uppercase
from string import digits
from random import choice


class Password:
    def __init__(self, master):
        self.spec = "!@#$%^&*"
        master.title("Password generator")
        master.resizable(False, False)
        master.configure(background="#e1d8b9")

        self.style = ttk.Style()
        self.style.configure("TFrame", background="#e1d8b9")
        self.style.configure("TButton", background="#e1d8b9")
        self.style.configure("TLabel", background="#e1d8b9")
        #self.style.configure("Header.TLabel", font=("Ariel", 18, "bold"))
        self.style.configure("TScale", background="#e1d8b9")
        self.style.configure("TCheckbutton", background="#e1d8b9", font=("ariel", 12))

        self.password_frame = ttk.Frame(master, borderwidth=2, relief="ridge" )
        self.password_label = ttk.Label(self.password_frame, font=("ariel", 14))

        self.button_frame = ttk.Frame(master)

        self.lower_check = ttk.Checkbutton(master, text="a-z")
        self.lower_check.state(["!alternate"])
        self.lower_check.state(["selected"])

        self.upper_check = ttk.Checkbutton(master, text="A-Z")
        self.upper_check.state(["!alternate"])
        self.upper_check.state(["selected"])

        self.nums_check = ttk.Checkbutton(master, text="0-9")
        self.nums_check.state(["!alternate"])

        self.special_check = ttk.Checkbutton(master, text="!@#...")
        self.special_check.state(["!alternate"])
        
        self.generate_button = ttk.Button(self.button_frame, text="Generate", command=self.generate_password_button)
        self.copy_button = ttk.Button(self.button_frame, text="Copy", command=self.copy_password)

        self.length_input = IntVar(value=5)

        self.number_slider = Scale(master, variable=self.length_input, orient="horizontal", length=150, showvalue=0, command=self.generate_password_slider, background="#e1d8b9", foreground="#e1d8b9", activebackground="#e1d8b9", highlightbackground="#e1d8b9", highlightcolor="#e1d8b9")
        self.number_slider["from"] = 6
        self.number_slider["to"] = 16
        self.number_slider["resolution"] = 1

        self.password_frame.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
        self.button_frame.grid(row=4, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
        self.password_label.pack()
        self.lower_check.grid(row=1, column=0, padx=2)
        self.upper_check.grid(row=1, column=1, padx=2)
        self.nums_check.grid(row=1, column=2, padx=2)
        self.special_check.grid(row=1, column=3, padx=2)
        ttk.Label(master, textvariable=self.length_input).grid(row=2, column=0, columnspan=4)
        self.number_slider.grid(row=3, column=0, columnspan=4,pady=5)

        self.generate_button.grid(row=0, column=0, padx=10, sticky="w")
        self.copy_button.grid(row=0, column=1, padx=10, sticky="e")

    def generate_password_slider(self, num):
        pool = ""
        if self.lower_check.instate(["selected"]):
            pool += ascii_lowercase
        if self.upper_check.instate(["selected"]):
            pool += ascii_uppercase
        if self.nums_check.instate(["selected"]):
            pool += digits
        if self.special_check.instate(["selected"]):
            pool += self.spec
        
        password = "".join([choice(pool) for _ in range(int(num))])
        self.password_label.config(text=password)

    def generate_password_button(self):
        pool = ""
        if self.lower_check.instate(["selected"]):
            pool += ascii_lowercase
        if self.upper_check.instate(["selected"]):
            pool += ascii_uppercase
        if self.nums_check.instate(["selected"]):
            pool += digits
        if self.special_check.instate(["selected"]):
            pool += self.spec
        
        password = "".join([choice(pool) for _ in range(self.length_input.get())])
        self.password_label.config(text=password)

    def copy_password(self):
            self.button_frame.clipboard_clear()
            self.button_frame.clipboard_append(self.password_label["text"])
            self.button_frame.update()



def main():
    root=Tk()
    password = Password(root)
    root.mainloop()

if __name__ == "__main__":
    main()






        