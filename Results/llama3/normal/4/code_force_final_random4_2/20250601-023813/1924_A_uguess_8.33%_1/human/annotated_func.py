#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^5) followed by t test cases. Each test case consists of a line containing three integers n (1 <= n <= 26), k (1 <= k <= 26), and m (1 <= m <= 1000), followed by a line containing a string s of length m, comprising only of the first k lowercase English alphabets.
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
        
    #State: t is 0, i is t, stdin contains 0 test cases, n is an integer between 1 and 26 (inclusive), k is an integer between 1 and 26 (inclusive), m is an integer between 1 and 1000 (inclusive), s is an empty string, ss is undefined, cur_ss is undefined, cnt is the number of times the string s can be divided into substrings of length k where each substring contains all k distinct characters, cur is 0. If cnt is greater than or equal to n, 'YES' is printed. Otherwise, a string of length cnt + n - cnt - 1 consisting of the character that is k-1 positions after 'a' in the alphabet repeated cnt times followed by 'a' repeated n - cnt - 1 times is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of three integers (n, k, m) and a string s. It then checks if the string s can be divided into substrings of length k, where each substring contains all k distinct characters. If the number of such divisions is greater than or equal to n, it prints 'YES'. Otherwise, it prints a string of length n-1, consisting of the character that is k-1 positions after 'a' in the alphabet repeated cnt times (where cnt is the number of divisions), followed by 'a' repeated n-cnt-1 times. The function processes all test cases and prints the corresponding results.

