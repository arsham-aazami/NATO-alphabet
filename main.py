import pandas
alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dic = {
    row["letter"]: row["code"]
    for (index, row) in alphabet_df.iterrows()
}
input_word = input("Enter a word: ").upper()
input_word_letter_list = [letter for letter in input_word]
output_list = []

for letter in input_word_letter_list:
    output_list.append(alphabet_dic[letter])
print(output_list)


def arsha():
    print("arsj")
