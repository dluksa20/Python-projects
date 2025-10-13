import tkinter
from tkinter import messagebox
import string
import random
import pyperclip
import json



# ----------------------------- FIND PASSWORD -------------------------------- #
def find_password():
    search_keyword = url_input.get().capitalize()
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
            try:
                match = data[search_keyword]
                username = match['username']
                pasword = match['password']
                messagebox.showinfo(title='Match Found', message=f'Username: {username} \nPassword: {pasword}')
            except KeyError:
                messagebox.showerror(title='Error', message='No match found.')
    except FileNotFoundError:
        messagebox.showerror(title='Error', message='File not found.')


# ----------------------------- GENERATE PASSWORD -------------------------------- #
def generate_password():


    password_list = []
    # 
    letters = string.ascii_letters
    numbers_list = string.digits
    special_symbols = string.punctuation[0:17]
    # 
    password_letters = [random.choice(letters) for _ in range(random.randint(8,10))]
    password_numbers = [random.choice(numbers_list) for _ in range(random.randint(8,10))]
    password_symbols = [random.choice(special_symbols) for _ in range(random.randint(2,4))]
    # 
    
    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = ''.join(password_list)
    pyperclip.copy(password)
    if len(password_input.get()) != 0 :
        password_input.delete(0, tkinter.END)
    password_input.insert(0, password)

    


# ----------------------------- SAVE DATA -------------------------------- #
def save_data():

    # get entries
    website = url_input.get()
    user = username_input.get()
    pasword = password_input.get()
    
    data_json = {
        website:{
            'username':user,
            'password':pasword
        }
    }


    # show warning for empty fields
    if len(user) == 0 or len(website) == 0 or len(pasword) == 0:
        is_empty = messagebox.showwarning(title='Warning', message='Invalid input, fields can not be empty!')
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered:' 
 
                                                  f'\nEmail: {user} \nPassword: {pasword} \nIs it ok to save?')
        if is_ok:
            # read/write data
                try:
                    with open('data.json', 'r') as f:
                        data = json.load(f)
                except (ValueError, FileNotFoundError):
                    with open('data.json', 'w') as f:
                        json.dump(data_json, f, indent=4)
                else:
                    data.update(data_json)
                    with open('data.json', 'w') as f:
                        json.dump(data, f, indent=4)

                finally:
                    # clear the entries
                    url_input.delete(0, tkinter.END)
                    password_input.delete(0, tkinter.END)



# ----------------------------- NEW WINDOW -------------------------------- #
window = tkinter.Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)


# ----------------------------- LOGO -------------------------------- #
canvas = tkinter.Canvas(width=200, height=200)
lock_image = tkinter.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=0, columnspan=3)


# ----------------------------- URL LABEL/INPUT -------------------------------- #
url_label = tkinter.Label(text='Website: ')
url_label.grid(row=1, column=0, sticky='E')

url_input = tkinter.Entry(width=25)
url_input.grid(row=1, column=1)
url_input.focus()

search_button = tkinter.Button(text='Search', width=15, command=find_password)
search_button.grid(row=1, column=2, padx=(5,0), pady=(3, 0))



# ----------------------------- USERNAME LABEL/INPUT -------------------------------- #
username_label = tkinter.Label(text='Username: ')
username_label.grid(row=2, column=0, sticky='E')

username_input = tkinter.Entry(width=45)
username_input.grid(row=2, column=1, columnspan=2, pady=(3, 0))
username_input.insert(0, 'name@gmail.com')


# ----------------------------- PASSWORD LABEL/INPUT/BUTTON -------------------------------- #
password_label = tkinter.Label(text='Password: ')
password_label.grid(row=3, column=0, sticky='E')

password_input = tkinter.Entry(width=25)
password_input.grid(row=3, column=1, sticky='E', pady=(3, 0))

generate_button = tkinter.Button(text='Generate Password',width=15, command=generate_password)
generate_button.grid(row=3, column=2, sticky='W', padx=(5,0), pady=(3, 0))


# ----------------------------- ADD BUTTON -------------------------------- #
add_button = tkinter.Button(text='Add', width=38, command=save_data)
add_button.grid(row=4, column=1, columnspan=2, pady=(5, 0))





window.mainloop()