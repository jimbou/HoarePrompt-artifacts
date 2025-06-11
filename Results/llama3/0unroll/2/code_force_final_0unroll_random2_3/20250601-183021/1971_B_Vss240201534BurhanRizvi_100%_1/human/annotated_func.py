#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t strings, each consisting of lowercase English letters and having a length of at most 10.
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
        
    #State: stdin is empty, and stdout contains t lines, each of which is either 'No' or 'Yes' followed by a rearranged string.

#Overall this is what the function does:This function reads a series of strings from standard input, checks each string to see if it can be rearranged into a different string, and prints 'Yes' followed by the rearranged string if possible, or 'No' if not. The function processes multiple strings, as specified by an initial integer input, and prints the results for each string.

