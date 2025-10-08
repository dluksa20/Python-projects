from tkinter import *


window = Tk()
window.minsize(width=200, height=130)
window.config(padx=30, pady=30)
window.title('Kilometer to Miles Converter')



def km_to_miles():
    km = input_km.get()
    try:
        converted = int(km)*0.621371
        output.config(text=f'{km} km ≈ {converted} miles')
    except:
        output.config(text='Error enter a valid number!')
    



# Label
input_label = Label(window, text='Kilometers: ').grid(row=0, column=0)

# Input
input_km = Entry(window)
input_km.grid(column=1, row=0, sticky='NESW')

# Result
output = Label(window, text='')
output.grid(column=1, row=1, pady=0, sticky='W')

# Quit button
btn_quit = Button(window, text='Quit', command=window.quit)
btn_quit.grid(column=0, row=2, sticky='NESW', pady=5)

# Calculate button
btn_calculate = Button(window, text='Calculate', command=km_to_miles)
btn_calculate.grid(column=1, row=2, sticky='NESW', pady=5)


window.mainloop()