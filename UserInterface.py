from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
from pandas import *

GROUPS = ("Invest", "Trade", "Track")
BACKGROUND_COLOR = "#7871ee"

class UserInterface:

    def __init__(self, tickers_table):
        self.tickers_table = tickers_table
        self.tickers_list = list(tickers_table["Ticker"].values)
        self.window = Tk()
        self.window.title("Stock Price Tracker")
        self.window.config(bg=BACKGROUND_COLOR)
        self.window.iconphoto(False, PhotoImage(file='./Graphics/icon.ico'))

        canvas = Canvas(width=700, height=200, highlightthickness=0)
        background_img = PhotoImage(file="./Graphics/Background.png")
        canvas.create_image(350, 196.5, image=background_img)
        canvas.grid(row=0, column=0, columnspan=9)

        # Row #1 - Delete stock from the list
        stocks_label = Label(text="Stocks: ", font=('Neue', 12, "bold"), bg=BACKGROUND_COLOR, fg="White")
        stocks_label.grid(row=1, column=3)

        tickers = StringVar()
        self.tickers_box = ttk.Combobox(textvariable=tickers)
        self.tickers_box['values'] = tuple(self.tickers_list)
        self.tickers_box.grid(row=1, column=4)

        remove_img = PhotoImage(file="./Graphics/remove_stock.png")
        remove_button = Button(text="Remove stock",image=remove_img, bg=BACKGROUND_COLOR, fg=BACKGROUND_COLOR,
                               borderwidth=0, command=self.remove_stock_from_list)
        remove_button.grid(row=1, column=5, pady=10)

        # Row #2 - Add new stock to the list
        add_stock_label = Label(text="Add new stock symbol: ", font=('Neue', 12, "bold"), bg=BACKGROUND_COLOR, fg="White")
        add_stock_label.grid(row=2, column=3, rowspan=2)

        self.new_stock = Entry(width=23)
        self.new_stock.insert(END, "Type a Ticker Symbol")
        self.new_stock.grid(row=2, column=4, pady=5)

        groups = StringVar()
        self.groups_box = ttk.Combobox(textvariable=groups, width=20)
        self.groups_box['values'] = GROUPS
        self.groups_box.grid(row=3, column=4)

        add_img = PhotoImage(file="./Graphics/add.png")
        add_button = Button(text="Add", image=add_img, bg=BACKGROUND_COLOR, fg=BACKGROUND_COLOR,
                            borderwidth=0, command=self.add_stock_to_list)
        add_button.grid(row=2, column=5, rowspan=2)

        # Row #3 - Save changes
        save_img = PhotoImage(file="./Graphics/save.png")
        save_button = Button(text="Save changes", image=save_img, bg=BACKGROUND_COLOR, fg=BACKGROUND_COLOR,
                             borderwidth=0, command=self.save_changes)
        save_button.grid(row=4, column=0, columnspan=9, pady=20)

        self.window.mainloop()

    def remove_stock_from_list (self):
        try:
            self.tickers_list.remove(self.tickers_box.get())
            self.tickers_box['values'] = tuple(self.tickers_list)
            self.tickers_table = self.tickers_table[self.tickers_table["Ticker"] != self.tickers_box.get()]
        except ValueError:
            messagebox.showwarning("Wrong Ticker Symbol", "Ticker symbol not available in the tickers file.")

    def add_stock_to_list (self):
        if len(self.new_stock.get()) > 5 or not self.new_stock.get().isalpha():
            messagebox.showwarning("Wrong Ticker Symbol",
                                   "Ticker symbol contains not allowed chars or longer then 5 chars.")
        elif not self.groups_box.get():
            messagebox.showwarning("Please select a group",
                                   "Please select a group from the check box.")
        else:
            self.tickers_list.append(self.new_stock.get())
            self.tickers_box['values'] = tuple(self.tickers_list)
            new_row = DataFrame([[self.new_stock.get(), self.groups_box.get()]], columns=['Ticker', 'Group'])
            self.tickers_table = concat([self.tickers_table, new_row], ignore_index=True)
            messagebox.showinfo("Stock added successfully", "Don't forget to save the changes.")

    def save_changes(self):
        try:
            with open("tickers.txt", "r+") as tickers_list:
                tickers_list.truncate()
                self.tickers_table.to_csv(tickers_list, encoding='utf-8', index=False)
                messagebox.showinfo("Changes saved successfully", "--DONE--")

        except FileNotFoundError:
            messagebox.showerror("ERROR: No thicker.txt file found", "No ticker file found..")