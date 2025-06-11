#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case consists of two integers n and m (1 <= n <= 50, 1 <= m <= 5) followed by a string a of n characters from 'A' to 'G'.
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
        
    #State: t is an integer between 0 and 1000, n is an integer, m is an integer, s is a string that must have at least 1 character, p is 'ABCDEFG', hmp is a Counter object containing the frequency of each character in s, stdin contains 0 test cases, _ is t-1, i is the last key in hmp, ans is the sum of m for each character in 'ABCDEFG' that is not in hmp plus m - hmp[i] for each character i in hmp where the frequency of character i in s is less than m, and ans is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers (n and m) and a string (s) of n characters. It calculates the total number of characters needed to make the frequency of each character in the string 's' at least 'm', considering the characters 'A' to 'G'. The function then prints the calculated total for each test case.

