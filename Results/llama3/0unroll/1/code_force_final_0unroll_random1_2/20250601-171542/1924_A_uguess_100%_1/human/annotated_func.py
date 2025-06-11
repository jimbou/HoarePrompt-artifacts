#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^5), followed by t test cases. Each test case consists of two lines. The first line contains three integers n (1 <= n <= 26), k (1 <= k <= 26), and m (1 <= m <= 1000). The second line contains a string s of length m, comprising only of the first k lowercase English alphabets.
    t = int(input())
    for i in range(t):
        n, k, m = map(int, input().split())
        
        s = input()
        
        cnt = 0
        
        cur = 0
        
        ans = ''
        
        for ss in s:
            cur_ss = ord(ss) - ord('a')
            if cur & 1 << cur_ss == 0:
                cur += 1 << cur_ss
            if cur == (1 << k) - 1:
                cnt += 1
                cur = 0
                ans += ss
        
        if cnt >= n:
            print('YES')
        else:
            print('NO')
            tmp = ''
            for i in range(k):
                if cur & 1 << i == 0:
                    tmp = chr(ord('a') + i)
                    break
            ans += tmp
            ans += 'a' * (n - cnt - 1)
            print(ans)
        
    #State: The output state is a string of length `n` consisting of the first `k` lowercase English alphabets, where each character appears at least once, and the remaining characters are filled with 'a's. If the input string `s` contains all `k` characters at least `n` times, the output is 'YES', otherwise, it is 'NO' followed by the constructed string.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of three integers (n, k, m) and a string s. It checks if the string s contains all k lowercase English alphabets at least n times. If it does, the function outputs 'YES'. Otherwise, it outputs 'NO' followed by a constructed string of length n, where each of the first k alphabets appears at least once, and the remaining characters are filled with 'a's.

