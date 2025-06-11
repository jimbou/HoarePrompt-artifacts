#State of the program right berfore the function call: stdin contains t+1 inputs: the first input is an integer t (1 <= t <= 1000), and the remaining t inputs are strings of lowercase English letters of length at most 10.
    for _ in range(int(input())):
        s = input()
        
        if len(s) == 1:
            print('No')
        elif len(set(s)) == 1 and len(s) > 1:
            print('No')
        else:
            s2 = ''.join(random.sample(s, len(s)))
            if s == s2:
                s2 = s[1:] + s[0]
            print('Yes')
            print(s2)
        
    #State: The output state will contain 't' number of outputs, where 't' is the first input provided. Each output will be either 'No' or 'Yes' followed by a shuffled string. If the input string has a length of 1 or all characters are the same, the output will be 'No'. Otherwise, the output will be 'Yes' followed by a shuffled version of the input string. If the shuffled string is the same as the original string, the first character will be moved to the end of the string.

#Overall this is what the function does:This function takes a series of strings as input and outputs a shuffled version of each string. If a string has a length of 1 or contains only identical characters, it outputs 'No'. Otherwise, it outputs 'Yes' followed by a shuffled version of the string. If the shuffled string is identical to the original, it moves the first character to the end of the string. The function processes multiple strings, with the number of strings specified by the first input.

