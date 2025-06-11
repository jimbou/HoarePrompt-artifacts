#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains an integer n (2 <= n <= 10) followed by n lines each containing n characters 0 or 1.
    a = int(input())
    for i in range(a):
        k = []
        
        for _ in range(int(input())):
            b = input()
            if '1' in b:
                k.append(b.count('1'))
        
        if k[0] == k[1]:
            print('SQUARE')
        else:
            print('TRIANGLE')
        
    #State: `a` is greater than or equal to 2 and less than or equal to 10, `i` is equal to `a`, either 'SQUARE' or 'TRIANGLE' has been printed, `b` is a string that contains the last input string, `_` is equal to 0, stdin is empty, and `k` is a list that contains the count of '1' in each input string `b` that contains '1'. If the first element of `k` is equal to the second element of `k`, then 'SQUARE' is being printed. Otherwise, 'TRIANGLE' is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by n lines of n characters (0s and 1s). It then analyzes the input strings, counts the occurrences of '1' in each string, and prints 'SQUARE' if the counts in the first two strings are equal, and 'TRIANGLE' otherwise. The function processes all test cases and prints the corresponding shape for each case.

