import pandas
is_right = False
nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in nato_data_frame.iterrows()}
while not is_right:
    user_input = input("Type in your name: ").upper()
    try:
        user_nato = [nato_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry only alphabets are allowed")
    else:
        is_right = True
print(user_nato)
