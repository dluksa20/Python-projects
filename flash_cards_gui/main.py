from tkinter import *
import pandas
import random



def click():

    df = pandas.read_csv('data/french_words.csv', header=0)
    df_dict = df.to_dict(orient='records')
    # 
    random_pair = random.choice(df_dict)
    french = random_pair['French']
    english = random_pair['English']
    card.itemconfigure(foreign_word, text=french)


# - COLORS/STYLES/FONTS

BACKGROUND_COLOR = "#B1DDC6"
font_1 = ("Ariel", 40, 'italic')
font_2 = ('Ariel', 60, 'bold')


# - MAIN WINDOW

window = Tk()
window.title('Flashy')
window.minsize(width=800, height=526)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


# - MAIN CANVAS

card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=False)
card_front = PhotoImage(file = 'images/card_front.png')
card.create_image(400, 263, image = card_front)
# 
language = card.create_text(400, 150, text='French', font=font_1)
foreign_word = card.create_text(400, 263, text='trouve', font=font_2)
# 
card.grid(row=0, column=0, columnspan=2)



# - BUTTONS


btn_wrong_image = PhotoImage(file='images/wrong.png')
btn_wrong = Button(height=90, width=90,image=btn_wrong_image, bd=0, command=click)
btn_wrong.grid(row=1, column=0)

btn_right_image = PhotoImage(file='images/right.png')
btn_right = Button(height=90, width=90, image=btn_right_image, bd=0, command=click)
btn_right.grid(row=1, column=1, pady=10)















window.mainloop()