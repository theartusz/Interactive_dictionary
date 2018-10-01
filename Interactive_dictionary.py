import json

data = json.load(open("data.json"))

def find_word(word):
    return data.get(word, "Doesn't exist")

word = input("Enter the word you are looking for: ")
print(find_word(word))
