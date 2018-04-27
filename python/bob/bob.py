import string

bobDict = {
        "ask": "Sure.",
        "yell": "Whoa, chill out!",
        "ask_yell": "Calm down, I know what I'm doing!",
        "empty": "Fine. Be that way!",
        "other": "Whatever.",
    }

redundant = string.whitespace + string.punctuation.replace("?","")

def hey(phrase):
    phrase = strip(phrase,redundant).strip()

    if phrase.strip() == "":
        return bobDict["empty"]

    if isQuestion(phrase) and isYell(phrase):
        return bobDict["ask_yell"]

    if isYell(phrase):
        return bobDict["yell"]

    if isQuestion(phrase):
        return bobDict["ask"]

    return bobDict["other"]

def isQuestion(phrase):
    if phrase[len(phrase)-1] == "?":
        return True
    return False

def isYell(phrase):
    return (isUpper(phrase) and len(phrase) > 2 and (phrase.isdigit() == False))

def isUpper(phrase):
    for i in range(0,len(phrase)-1):
        if str(phrase[i]).isalpha() == False:
            continue
        if string.lowercase.find(phrase[i]) != -1:
            return False
    return True

def strip(input, chars):
    for i in range(0,len(chars)-1):
        input = input.replace(chars[i],"")
    return input