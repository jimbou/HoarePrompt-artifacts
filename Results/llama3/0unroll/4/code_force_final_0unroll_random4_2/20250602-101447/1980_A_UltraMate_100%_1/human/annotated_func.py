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
        
    #State: The number of characters that need to be added to the string `a` to make the frequency of each character from 'A' to 'G' at least `m` is printed for each test case. The value of `t` remains unchanged.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints the number of characters that need to be added to a given string to make the frequency of each character from 'A' to 'G' at least a specified minimum value. The function does not modify the input values and leaves the value of `t` unchanged.

