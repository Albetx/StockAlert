from tkinter import *
import tkinter.ttk as ttk

GROUPS = ("Invest", "Trade", "Track")
BACKGROUND_COLOR = "#7871ee"

class UserInterface:

    def __init__(self, tickers_table):
        self.tickers_table = tickers_table
        self.tickers_list = tuple(tickers_table["Ticker"].values)
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
        tickers_box = ttk.Combobox(textvariable=tickers)
        tickers_box['values'] = self.tickers_list
        tickers_box.grid(row=1, column=4)

        remove_img = PhotoImage(file="./Graphics/remove_stock.png")
        remove_button = Button(text="Remove stock",image=remove_img, bg=BACKGROUND_COLOR, fg=BACKGROUND_COLOR, borderwidth=0)
        remove_button.grid(row=1, column=5, pady=10)

        # Row #2 - Add new stock to the list
        add_stock_label = Label(text="Add new stock symbol: ", font=('Neue', 12, "bold"), bg=BACKGROUND_COLOR, fg="White")
        add_stock_label.grid(row=2, column=3, rowspan=2)

        new_stock = Entry(width=23)
        new_stock.insert(END, "Type Ticker Symbol")
        new_stock.grid(row=2, column=4, pady=5)

        groups = StringVar()
        groups_box = ttk.Combobox(textvariable=groups, width=20)
        groups_box['values'] = GROUPS
        groups_box.grid(row=3, column=4)

        add_img = PhotoImage(file="./Graphics/add.png")
        add_button = Button(text="Add", image=add_img, bg=BACKGROUND_COLOR, fg=BACKGROUND_COLOR, borderwidth=0)
        add_button.grid(row=2, column=5, rowspan=2)

        # Row #3 - Save changes
        save_img = PhotoImage(file="./Graphics/save.png")
        save_button = Button(text="Save changes", image=save_img, bg=BACKGROUND_COLOR, fg=BACKGROUND_COLOR, borderwidth=0)
        save_button.grid(row=4, column=0, columnspan=9, pady=20)





        self.window.mainloop()