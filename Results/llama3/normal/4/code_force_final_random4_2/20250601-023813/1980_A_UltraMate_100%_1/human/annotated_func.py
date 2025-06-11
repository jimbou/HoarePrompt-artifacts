#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case consists of two lines. The first line contains two integers n and m (1 <= n <= 50, 1 <= m <= 5). The second line contains a string a of n characters from 'A' to 'G'.
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        
        s = input()
        
        ans = 0
        
        p = 'ABCDEFG'
        
        hmp = Counter(s)
        
        for i in p:
            if i not in hmp:
                ans += m
        
        for i in hmp:
            if hmp[i] < m:
                ans += m - hmp[i]
        
        print(ans)
        
    #State: t is an integer that must be at least 1, _ is t-1, stdin contains 0 test cases, n is an integer between 1 and 50 inclusive, m is an integer between 1 and 5 inclusive, s is a string of n characters from 'A' to 'G', p is 'ABCDEFG', hmp is a dictionary where keys are characters from 'A' to 'G' and values are their respective counts in string s, i is the last key in the dictionary hmp, and ans is the total number of characters in string s that appear less than m times, and ans is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two lines: the first line contains two integers n and m, and the second line contains a string s of n characters. The function then calculates the total number of characters in the string that appear less than m times and prints this count for each test case. The function processes all test cases and does not return any value.

