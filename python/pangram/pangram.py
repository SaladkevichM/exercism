def is_pangram(sentence):

    alphabet = 'qwertyuioplkjhgfdsazxcvbnm'
    hits = {}

    for i in range(0,len(sentence)):

        if sentence[i] != " " and alphabet.__contains__(sentence[i].lower()):
            hits[sentence[i].lower()] = 1

    if len(alphabet) == len(hits.keys()):
        return True

    return False
