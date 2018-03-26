def is_isogram(string):
    
    # fill dictionary
    dict = {}
    for i in range(0,len(string)):
        
        char = string[i].lower()
        if char == " " or char == "-":
            continue

        if char in dict: 
            dict[char] = dict[char] + 1
        else:
            dict[char] = 1

    # read dictionary
    for key in dict.keys():
        if dict[key] > 1:
            return False

    return True
