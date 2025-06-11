#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t strings, each consisting of lowercase English letters and having a length of at most 10.
    for _ in range(int(input())):
        s = input()
        
        s2 = ''.join(random.sample(s, len(s)))
        
        if s != s2:
            print('Yes')
            print(s2)
        else:
            print('No')
        
    #State: The output state will contain a series of strings, each representing the shuffled version of the input strings, along with a 'Yes' indicator, or a 'No' indicator if the shuffled string is the same as the original string. The number of output strings will be equal to the number of input strings.

#Overall this is what the function does:This function reads a series of strings from standard input, shuffles each string randomly, and prints the shuffled string along with 'Yes' if it is different from the original string, or 'No' if it is the same. The function processes multiple strings, with the number of strings specified by an initial integer input.

