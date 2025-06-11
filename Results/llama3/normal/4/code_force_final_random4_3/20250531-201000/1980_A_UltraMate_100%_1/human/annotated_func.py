#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case contains two integers n and m (1 <= n <= 50, 1 <= m <= 5) followed by a string a of n characters from 'A' to 'G'.
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
        
    #State: t is an integer equal to 0, stdin contains 0 test cases, n is an integer between 1 and 50 inclusive, m is an integer between 1 and 5 inclusive, s is a string of n characters from 'A' to 'G', p is 'ABCDEFG', hmp is a dictionary containing the frequency of each character in s that is not empty and has at least 2 keys, i is the last key in hmp, ans is either m, m+m, m+m+m, m+m+m+m, m+m+m+m+m, m+m+m+m+m+m, or m+m+m+m+m+m+m increased by m - hmp[i] for each key i in hmp where the frequency of character i in s is less than m, otherwise ans remains unchanged, _ is t-1, and the value of ans is being printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers (n and m) and a string (s) of n characters. It calculates the total number of characters that need to be added to the string to make the frequency of each character in the string at least m. The function then prints the calculated total for each test case.

