#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^5) followed by t test cases. Each test case contains three integers n (1 <= n <= 26), k (1 <= k <= 26), and m (1 <= m <= 1000) followed by a string s of length m, comprising only of the first k lowercase English alphabets.
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
        
    #State: t is an integer between 0 and 10^5 (inclusive), i is t, stdin is empty, n is an integer, k is an integer, m is an integer, cnt is an integer, s is a string of length m, ss is the last character in the string s, cur_ss is the ASCII value of the last character in the string s minus the ASCII value of 'a', which is a value between 0 and 25 (inclusive), cur is either 0 or a value between 1 and (1 << k) - 1.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of three integers (n, k, m) and a string s. It then checks if the string s contains at least n substrings of length k, where each substring consists of distinct characters from the first k lowercase English alphabets. If such substrings are found, it prints 'YES'. Otherwise, it prints 'NO' followed by a string that represents the shortest possible completion of s to meet the condition. The function processes all test cases and prints the results accordingly.

