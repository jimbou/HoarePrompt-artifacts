#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (the length of the strip) and then a string of characters 'W' or 'B' (the strip) of the same length as the integer.
    n = int(input())
    for i in range(n):
        t = int(input())
        
        x = list(input())
        
        if 'B' in x:
            start = x.index('B')
            end = len(x) - x[::-1].index('B') - 1
            print(end - start)
        else:
            print(0)
        
    #State: The number of test cases have been processed, and for each test case, the length of the longest contiguous substring of 'B's in the input string has been printed. The input string and the integer `n` remain unchanged.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer (the length of a strip) and a string of characters 'W' or 'B' (the strip). It then calculates and prints the length of the longest contiguous substring of 'B's in each input string. If no 'B's are found in a string, it prints 0. The function processes all test cases and does not modify the input strings or the integer `n`.

