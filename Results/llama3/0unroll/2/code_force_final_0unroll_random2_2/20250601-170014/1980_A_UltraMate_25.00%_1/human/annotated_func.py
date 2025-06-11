#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case consists of two integers n and m (1 <= n <= 50, 1 <= m <= 5) followed by a string a of n characters from 'A' to 'G'.
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        
        s = input()
        
        ans = 0
        
        p = 'ABCDEF'
        
        hmp = Counter(s)
        
        for i in p:
            if i not in hmp:
                ans += m
        
        for i in hmp:
            if hmp[i] < m:
                ans += m - hmp[i]
        
        print(ans)
        
    #State: The output state is the total number of characters that need to be added to the string `s` to make the frequency of each character from 'A' to 'G' at least `m`. This is calculated for each test case and printed as output. The initial state of `t` remains unchanged, as it is not affected by the loop.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers (n and m) and a string of characters (s). It calculates and prints the total number of characters that need to be added to the string s to make the frequency of each character from 'A' to 'G' at least m, for each test case. The function does not modify the input values and only produces output for each test case.

