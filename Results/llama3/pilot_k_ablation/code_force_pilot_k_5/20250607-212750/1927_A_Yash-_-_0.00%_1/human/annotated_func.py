#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case contains an integer n (1 <= n <= 10) followed by a string s of length n consisting of 'W' and 'B' characters, with at least one 'B' character.
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
        
    #State: n is an integer between 1 and 10^4 inclusive, i is equal to n, t is an integer equal to the input value, x is a list of characters equal to the input string, stdin is empty. If 'B' is in the list x of characters, the difference between the index of the last 'B' and the index of the first 'B' in the list x of characters is printed. Otherwise, 0 is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer followed by a string of 'W' and 'B' characters. It then calculates and prints the distance between the first and last occurrence of 'B' in each string, or 0 if no 'B' is found. The function processes multiple test cases and outputs the results for each case.

