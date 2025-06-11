#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t strings, each consisting of lowercase English letters and having a length of at most 10.
    for _ in range(int(input())):
        s = input()
        
        s2 = ''.join(random.sample(s, len(s)))
        
        if s != s2:
            print('Yes')
            print(s2)
        else:
            print('No')
        
    #State: s is a string consisting of lowercase English letters and having a length of at most 10, s2 is a string consisting of the same characters as s but in a random order, _ is t-1, t is greater than or equal to 0, stdin contains 0 strings. If s is not equal to s2, 'Yes' is printed and s2 is printed. If s is equal to s2, 'No' is printed.

#Overall this is what the function does:This function reads a series of strings from standard input, randomizes the characters in each string, and prints 'Yes' followed by the randomized string if it is different from the original, or 'No' if it is the same. The function processes multiple strings, with the number of strings specified by an initial integer input.

