#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains three integers n, k, and m, where n, k, and m are non-negative integers. The second line contains a string s of length m, comprising only of the first k lowercase English alphabets.
    t = int(input())
    for i in range(t):
        n, k, m = map(int, input().split())
        
        s = input()
        
        cnt = 0
        
        cur = 0
        
        for ss in s:
            cur_ss = ord(ss) - ord('a')
            if cur & 1 << cur_ss == 0:
                cur += 1 << cur_ss
            if cur == (1 << k) - 1:
                cnt += 1
                cur = 0
        
        if cnt >= n:
            print('YES')
        else:
            print('NO')
            tmp = ''
            ans = chr(ord('a') + k - 1) * cnt
            for i in range(k):
                if cur & 1 << i == 0:
                    tmp = chr(ord('a') + i)
            ans += tmp
            ans += 'a' * (n - cnt - 1)
            print(ans)
        
    #State: The loop will execute t times, each time processing a test case. For each test case, it will read two lines of input, the first line containing two integers k and m, and the second line containing a string s of length m. The loop will then process the string s and calculate the number of substrings of length k that contain all k distinct characters. If the number of such substrings is greater than or equal to n, it will print 'YES'. Otherwise, it will print 'NO' and construct a string of length n that contains all k distinct characters and print it. After processing all t test cases, the loop will terminate.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines: the first line contains three integers n, k, and m, and the second line contains a string s of length m. It then processes the string s to count the number of substrings of length k that contain all k distinct characters. If the count is greater than or equal to n, it prints 'YES'. Otherwise, it prints 'NO' and constructs a string of length n that contains all k distinct characters, printing the constructed string. The function repeats this process for each test case.

