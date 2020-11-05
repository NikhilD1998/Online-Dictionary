import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0 :
        predictedWord = input("Did you mean %s ? If Yes press y or press n for No: " % get_close_matches(word, data.keys())[0])
        predictedWord = predictedWord.lower()
        if predictedWord == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif predictedWord == "n":
            exit()
        else: 
            return "We didn't understand your query. Please try again"
    else:
        return "This word is not available in the Dictionary"

word = input("Enter word: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)