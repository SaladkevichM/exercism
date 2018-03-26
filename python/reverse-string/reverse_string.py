def reverse(input=''):
    if len(input) == 0:
        return input

    output = ""
    for i in range(0,len(input)):        
        output = output + input[-1]
        input = input[:-1]
    return output
