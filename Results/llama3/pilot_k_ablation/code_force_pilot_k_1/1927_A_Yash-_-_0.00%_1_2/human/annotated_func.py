#State of the program right berfore the function call: stdin contains multiple inputs: first an integer t (1 <= t <= 10^4), then for each test case, first an integer n (1 <= n <= 10), then a string s of length n consisting of 'W' and 'B' characters.
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
        
    #State: n is an integer between 1 and 10, i is n-1, stdin contains no inputs. For each test case, if 'B' is present in the string, the difference between the index of the last 'B' and the index of the first 'B' in the string is printed. Otherwise, if the string consists only of 'W' characters, 0 is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer and a string of 'W' and 'B' characters. For each test case, it calculates and prints the distance between the first and last occurrence of 'B' in the string, or 0 if the string contains only 'W' characters. The function processes all test cases and then terminates, leaving the input stream empty.

