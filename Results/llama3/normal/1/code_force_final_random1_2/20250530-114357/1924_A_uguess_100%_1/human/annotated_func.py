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
        
    #State: t is 0, i is t, n is an integer, k is an integer, m is an integer, cnt is the number of times the string s contains a substring of length k consisting of distinct characters, ans is either the concatenation of all characters in s that are part of a substring of length k consisting of distinct characters or the concatenation of all characters in s that are part of a substring of length k consisting of distinct characters plus tmp plus 'a' repeated (n - cnt - 1) times, s is an empty string, ss is the last character in the original string, cur_ss is the position of the last character in the original string in the alphabet (0-25), cur is 0, tmp is either an empty string or a character from 'a' to 'z' (inclusive), and stdin contains 0 test cases. If cnt is greater than or equal to n, 'YES' is printed. Otherwise, ans is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of three integers (n, k, m) and a string s of length m. It then checks if the string s contains at least n substrings of length k consisting of distinct characters. If it does, the function prints 'YES'. Otherwise, it prints a string that is the concatenation of all characters in s that are part of a substring of length k consisting of distinct characters, followed by a character that is not in the current substring, and then 'a' repeated (n - cnt - 1) times, where cnt is the number of times the string s contains a substring of length k consisting of distinct characters.

