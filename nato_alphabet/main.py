import pandas

df = pandas.read_csv('./nato_phonetic_alphabet.csv')
code = {row.letter:row.code for (index, row) in df.iterrows()}


# SOLUTION 

def generate_phonetic(code):
    user_name = input('Enter your name: ').upper()

    try:
        answer = [code[letter] for letter in user_name]
    except KeyError:
        print('Sorry, only letters in the alphabet please.')
    else:
        print(answer)

if __name__ == '__main__':
    generate_phonetic(code)