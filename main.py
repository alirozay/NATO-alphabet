import pandas
nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in nato_data_frame.iterrows()}
user_input = input("Type in your name: ").upper()
user_nato = [nato_dict[letter] for letter in user_input]
print(user_nato)
