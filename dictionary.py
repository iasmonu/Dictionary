import json
from difflib import get_close_matches
data = json.load(open("dictionary_data.json"))

#building translate function
def translate(word):
    word = word.lower()#90% pwrds are in lowercase
    if word in data :
        return(data[word])
    elif word.title() in data: #for the case of Tamil and tamil
        return(data[word.title()])
    elif word.upper() in data: #for the case of usa and USA
        return(data[word.upper()])
    elif len(get_close_matches(word , data.keys())) > 0 : #when we have closely matched words
        print("did you mean %s instead" %get_close_matches(word, data.keys())[0])
        decide = input("press y for yes or n for no")
        if decide == "y":
            return data[get_close_matches(word , data.keys())[0]]
        elif decide == "n":
            return("pugger your paw steps on wrong keys ")
        else:
            return("You have entered wrong input please enter just y or n")
    else:
        print("sorry! we dont have the answer")
#main loic or driver code
word = input("enter the word to be searched: ")

output = translate(word)
#for a better interface
#check if no of output is more than 1
if type(output) == list:
    #print line by line
    for item in output:
        print(item)
else:
    print(output)
