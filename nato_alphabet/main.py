import pandas

df = pandas.read_csv('./nato_phonetic_alphabet.csv')
user_name = input('Enter your name: ').upper()


#  SOLUTION 1
code = []

for letter in user_name:
    for (index, row) in df.iterrows():
        if letter == row.letter:
            code.append(row.code)


print(code)

# SOLUTION 2
code = {row.letter:row.code for (index, row) in df.iterrows()}
answer = [code[letter] for letter in user_name]
print(answer)
