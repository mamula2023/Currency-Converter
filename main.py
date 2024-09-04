import tkinter as tk
from tkinter.ttk import Combobox
import currency_converter

bg_color = "#0390fc"
currencies = ["USD", "EUR", "GEL", "GBP"]


def remove_label(label):
    label.place_forget()


def validate(amount):
    if amount.isdecimal():
        return True

    if amount.count('.') == 1:
        if amount.replace('.', '').isdecimal():
            return True
    return False


def swap():
    to = to_drop_down.get()
    to_drop_down.set(from_drop_down.get())
    from_drop_down.set(to)

    to = to_amount.get()
    to_amount.delete(0, tk.END)
    to_amount.insert(0, from_amount.get())
    from_amount.delete(0, tk.END)
    from_amount.insert(0, to)


def convert_action():
    from_currency = from_drop_down.get()
    if not from_currency:
        notice = tk.Label(root, text="Please choose a currency")
        notice.place(x=10, y=10)
        root.after(3000, remove_label, notice)
        return

    amount_entered = from_amount.get()
    if not amount_entered:
        notice = tk.Label(root, text="Please enter amount")
        notice.place(x=10, y=10)
        root.after(3000, remove_label, notice)
        return
    elif not validate(amount_entered):
        notice = tk.Label(root, text="Please enter proper amount")
        notice.place(x=10, y=10)
        root.after(3000, remove_label, notice)
        return

    amount = float(amount_entered)

    to_currency = to_drop_down.get()
    if not to_currency:
        notice = tk.Label(root, text="Please choose a currency")
        notice.place(x=10, y=10)
        root.after(3000, remove_label, notice)
        return

    to_amount.delete(0, tk.END)
    result = currency_converter.convert(from_currency, to_currency, amount)
    if result == -1:
        notice = tk.Label(root, text="error in network")
        notice.place(x=10, y=10)
        root.after(3000, remove_label, notice)
        return


    to_amount.insert(0, result)


def clear():
    from_drop_down.delete(0, tk.END)
    to_drop_down.delete(0, tk.END)
    from_amount.delete(0, tk.END)
    to_amount.delete(0, tk.END)


root = tk.Tk()
root.geometry(f"{int(root.winfo_screenwidth() / 3)}x{int(root.winfo_screenheight() / 3)}")
root.title("Currency Converter")

# create and show left, right and bottom panels
left_side = tk.Frame(root, bg=bg_color)
right_side = tk.Frame(root, bg=bg_color)
bottom_side = tk.Frame(root, bg=bg_color)
left_side.grid(row=0, column=0, sticky=tk.NSEW)
right_side.grid(row=0, column=1, sticky=tk.NSEW)
bottom_side.grid(row=1, column=0, columnspan=2, sticky=tk.NSEW)

# configure and populate left panel
left_side.columnconfigure(0, weight=1)
left_side.rowconfigure(0, weight=1)
inner_left = tk.Frame(left_side, bg=bg_color)
inner_left.grid(row=0, column=0)

from_label = tk.Label(inner_left, text="From", bg=bg_color)
from_drop_down = tk.ttk.Combobox(inner_left, values=currencies)
from_amount = tk.Entry(inner_left)

from_label.pack(pady=10)
from_drop_down.pack(pady=10)
from_amount.pack(pady=10)

# configure and populate right panel
right_side.columnconfigure(0, weight=1)
right_side.rowconfigure(0, weight=1)
inner_right = tk.Frame(right_side, bg=bg_color)
inner_right.grid(row=0, column=0)

to_label = tk.Label(inner_right, text="To", bg=bg_color)
to_drop_down = tk.ttk.Combobox(inner_right, height=5, values=currencies)
to_amount = tk.Entry(inner_right)
to_label.pack(pady=10)
to_drop_down.pack(pady=10)
to_amount.pack(pady=10)

# configure and populate bottom panel
bottom_side.columnconfigure(0, weight=1)
bottom_side.rowconfigure(0, weight=1)
inner_bottom = tk.Frame(bottom_side, bg=bg_color)
inner_bottom.grid(row=0, column=0)

convert_button = tk.Button(inner_bottom, text="Convert", command=convert_action)
convert_button.pack(pady=8)

clear_button = tk.Button(inner_bottom, text="Clear", command=clear)
clear_button.pack(pady=8)

swap_button = tk.Button(inner_bottom, text="Swap", command=swap)
swap_button.pack(pady=8)

root.rowconfigure(0, weight=3)
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

left_side.grid(row=0, column=0, sticky=tk.NSEW)
right_side.grid(row=0, column=1, sticky=tk.NSEW)
bottom_side.grid(row=1, column=0, columnspan=2)

root.mainloop()
