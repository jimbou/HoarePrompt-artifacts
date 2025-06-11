#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case consists of two lines. The first line contains two integers n and m (1 <= n <= 50, 1 <= m <= 5). The second line contains a string a of n characters from 'A' to 'G'.
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
        
    #State: The number of characters that need to be added to the string `a` to make all characters appear at least `m` times, for each test case.

#Overall this is what the function does:Calculates and prints the minimum number of characters that need to be added to a given string to make all characters appear at least a specified number of times, for multiple test cases.

