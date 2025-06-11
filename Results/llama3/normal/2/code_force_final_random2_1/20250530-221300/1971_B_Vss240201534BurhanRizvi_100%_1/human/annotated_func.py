#State of the program right berfore the function call: stdin contains two inputs: first an integer (between 1 and 1000) and then a string of lowercase English letters of length at most 10.
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
        
    #State: The program has processed all the strings from the input and has printed 'Yes' or 'No' for each string based on the conditions specified in the loop. The input buffer is empty.

#Overall this is what the function does:This function reads a series of strings from the input, checks each string to see if it has more than one distinct character and is not a single character, and if so, generates a random permutation of the string (or a simple rotation if the random permutation happens to be the same as the original string), and prints 'Yes' followed by the permuted string. If the string does not meet these conditions, it prints 'No'. The function continues this process until all input strings have been processed, at which point the input buffer is empty.

