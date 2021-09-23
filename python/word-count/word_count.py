import string

def word_count(phrase):
    dict = {}

    punct = string.punctuation.replace("'","").replace(",","").replace("_","")
    replace_punctuation = string.maketrans(punct, ' '*len(punct))
    replace_whitespace = string.maketrans(string.whitespace, ' '*len(string.whitespace))
    
    words = phrase.expandtabs().replace("_"," ").replace(","," ").split(" ")

    for i in range(0,len(words)):

        word = words[i].translate(replace_punctuation).translate(replace_whitespace).strip().strip("'")
        if word != " " and word != "":

            word = word.lower()
            if dict.has_key(word):
                dict[word] = dict[word] + 1
            else:
                dict[word] = 1

    return dict
