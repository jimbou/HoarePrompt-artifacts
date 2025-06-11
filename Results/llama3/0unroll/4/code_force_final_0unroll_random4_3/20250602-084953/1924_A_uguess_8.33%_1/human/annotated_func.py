#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^5) followed by t test cases. Each test case consists of two lines. The first line contains three integers n (1 <= n <= 26), k (1 <= k <= 26), and m (1 <= m <= 1000). The second line contains a string s of length m, comprising only of the first k lowercase English alphabets.
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
        
    #State: The output state after the loop executes all the iterations is a series of 'YES' or 'NO' followed by a string. The 'YES' or 'NO' indicates whether the string s contains at least n substrings of length k that contain all k lowercase English alphabets. If 'NO', the string is the lexicographically smallest string of length n that contains all k lowercase English alphabets and is consistent with the given string s.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of three integers (n, k, m) and a string s. It checks if the string s contains at least n substrings of length k that contain all k lowercase English alphabets. If it does, the function prints 'YES'. If not, it prints 'NO' followed by the lexicographically smallest string of length n that contains all k lowercase English alphabets and is consistent with the given string s. The function repeats this process for all test cases provided in the input.

