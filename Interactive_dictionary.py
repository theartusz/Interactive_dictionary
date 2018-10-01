import json, difflib
from difflib import SequenceMatcher #solves issue of misspeled words
from difflib import get_close_matches

data = json.load(open("data.json"))

#check data.json for word and return definition 
def find_word(word):
    word = word.lower()

    if word in data:
        return data[word]

    elif word.title() in data:
        return data[word.title()]

    elif word.upper() in data:
        return data[word.upper()]

    elif get_close_matches(word, data.keys()) != []: 
        #options are ordered based on closnes
        option = get_close_matches(word, data.keys())[0]
        yn = input("Did you mean %s instead? Enter Y if yes or N if no." %option)
        
        if yn == 'Y':
            return data[option]
        
        else: 
            return "Word " + word + " is not in dictionary."

    else:
        print("Word " + word + " is not in dictionary.")

word = input("Enter the word you are looking for: ")

output = find_word(word)

if type(output) == list:
    for item in output:
        print(item)
else: 
    print(output)