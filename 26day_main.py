import pandas
data = pandas.read_csv("26day_nato_phonetic_alphabet.csv")
# print(data)

alphabet_dict = {row.letter:row.code for (index,row) in data.iterrows()}
name = input("Enter a word: ")
# print(alphabet_dict)
name_dict = [alphabet_dict[letter] for letter in name.upper()]
print(name_dict)