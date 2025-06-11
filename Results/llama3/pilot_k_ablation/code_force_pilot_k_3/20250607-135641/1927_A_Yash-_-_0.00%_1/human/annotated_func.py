#State of the program right berfore the function call: stdin contains an integer t (1 ≤ t ≤ 10^4) followed by t test cases. Each test case consists of an integer n (1 ≤ n ≤ 10) followed by a string s of length n containing only 'W' and 'B' characters, with at least one 'B' character.
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
        
    #State: n is an integer (1 ≤ n ≤ 10^4) and is equal to 0, i is (n-1), t is an integer, x is a list of characters, stdin contains 0 test cases. If 'B' is in the list x, the difference between the index of the last 'B' and the index of the first 'B' in the list x is printed. Otherwise, 0 is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer followed by a string of 'W' and 'B' characters. It then calculates and prints the distance between the first and last occurrence of 'B' in each string, or 0 if there are no 'B' characters. The function processes all test cases and does not return any value, only printing the results for each case.

