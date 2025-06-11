#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t strings, each consisting of lowercase English letters of length at most 10.
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
        
    #State: stdin is empty.

#Overall this is what the function does:This function reads a series of strings from standard input, checks each string for uniqueness of characters and length, and if the string has more than one unique character, it generates a new string by either shuffling the characters or rotating the string, and prints the result. If the string has only one unique character or is a single character, it prints 'No'. The function continues this process until all input strings have been processed, leaving the standard input empty.

