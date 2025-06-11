#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t strings, each consisting of lowercase English letters of length at most 10.
    for _ in range(int(input())):
        s = input()
        
        s2 = ''.join(random.sample(s, len(s)))
        
        if s != s2:
            print('Yes')
            print(s2)
        else:
            print('No')
        
    #State: The output state will contain a series of 'Yes' or 'No' statements, followed by a shuffled version of the input string if 'Yes' is printed. The number of 'Yes' or 'No' statements will be equal to the value of t. The stdin will be empty after the loop finishes executing.

#Overall this is what the function does:This function reads a series of strings from standard input, shuffles each string randomly, and prints 'Yes' followed by the shuffled string if the shuffled string is different from the original, or 'No' if they are the same. The function processes a number of strings specified by an initial integer input, and it empties the standard input after processing all strings.

