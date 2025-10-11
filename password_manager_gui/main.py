import tkinter
import customtkinter


# ----------------------------- NEW WINDOW -------------------------------- #
window = tkinter.Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)


# ----------------------------- LOGO -------------------------------- #
canvas = tkinter.Canvas(width=200, height=200)
lock_image = tkinter.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)


# ----------------------------- URL LABEL/INPUT -------------------------------- #
url_label = tkinter.Label(text='Website: ')
url_label.grid(row=1, column=0)
url_input = tkinter.Entry(width=35)
url_input.grid(row=1, column=1, columnspan=2, sticky='EW')



# ----------------------------- USERNAME LABEL/INPUT -------------------------------- #
username_label = tkinter.Label(text='Username: ')
username_label.grid(row=2, column=0)

username_input = tkinter.Entry(width=35)
username_input.grid(row=2, column=1, columnspan=2, sticky='EW')
2

# ----------------------------- PASSWORD LABEL/INPUT/BUTTON -------------------------------- #
password_label = tkinter.Label(text='Password: ')
password_label.grid(row=3, column=0)

password_input = tkinter.Entry(width=21)
password_input.grid(row=3, column=1, sticky='W')

generate_button = tkinter.Button(text='Generate Password')
generate_button.grid(row=3, column=2)


# ----------------------------- ADD BUTTON -------------------------------- #
add_button = tkinter.Button(text='Add', width=36)
add_button.grid(row=4, column=1, columnspan=2, sticky='WE')





window.mainloop()