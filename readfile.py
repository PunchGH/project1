
from tkinter import *
from forex_python.converter import CurrencyRates

c = CurrencyRates()

# API requests to get list of Currency
c.get_rates('USD')
currency = c.get_rates('USD')


# Function to get list of currency
def getcurrency_list(currency):
    currency_list = ['USD']
    for key in currency.keys():
        currency_list.append(key)
    return currency_list


# Function to calculate exchange and show result
def leftClickButton(event):
    amount = float(get_amount.get())
    first_currency_input = first_currency.get()
    second_currency_input = second_currency.get()
    currency_rate = round(c.get_rate(first_currency_input, second_currency_input), 2)
    result_amount = f"{round(c.convert(first_currency_input, second_currency_input, amount), 2):,}"

    label_currency_rate.configure(text="อัตราแลกเปลี่ยน : " + str(currency_rate))
    label_result_amount.configure(text=result_amount)


currency_list = getcurrency_list(currency)

# UI
mainWindow = Tk()
# mainWindow.geometry("600x400")

# Add Header
label_header = Label(mainWindow, text="โปรแกรมคำนวนอัตราแลกเปลี่ยน", font=("Helvetica", 18))
label_header.grid(row=0, columnspan=3, padx=15, pady=15)

# Label
label_first_currency = Label(mainWindow, text="สกุลเงินต้นทาง", font=("Helvetica", 16))
label_first_currency.grid(row=2, column=0, padx=5, pady=5)
label_middle = Label(mainWindow, text="     >>>     ")
label_middle.grid(row=2, column=1)
label_middle2 = Label(mainWindow, text="     >>>     ")
label_middle2.grid(row=4, column=1)
label_second_currency = Label(mainWindow, text="สกุลเงินปลายทาง", font=("Helvetica", 16))
label_second_currency.grid(row=2, column=2, padx=5, pady=5)

# Dropdown Menu to pick Currency
first_currency = StringVar(mainWindow)
first_currency.set(currency_list[0])  # default value
second_currency = StringVar(mainWindow)
second_currency.set(currency_list[0])  # default value
dropdown_first_currency = OptionMenu(mainWindow, first_currency, *currency_list)
dropdown_first_currency.grid(row=3, column=0, padx=5, pady=10)
dropdown_second_currency = OptionMenu(mainWindow, second_currency, *currency_list)
dropdown_second_currency.grid(row=3, column=2, padx=5, pady=10)

# Receive Input from User
get_amount = Entry(mainWindow, justify='center')
get_amount.grid(row=4, column=0, padx=5, pady=5, ipadx=1, ipady=2)

# Result
label_result_amount = Label(mainWindow, text="จำนวนเงิน")
label_result_amount.grid(row=4, column=2, padx=5, pady=5, ipadx=2, ipady=5)
label_currency_rate = Label(mainWindow, text="")
label_currency_rate.grid(row=5, columnspan=3, padx=15, pady=15)

# Calculate Button
calculateButton = Button(mainWindow, text="คำนวณ", height=2, width=20)
calculateButton.grid(row=6, columnspan=3, padx=15, pady=15)
calculateButton.bind('<Button-1>', leftClickButton)

mainWindow.mainloop()