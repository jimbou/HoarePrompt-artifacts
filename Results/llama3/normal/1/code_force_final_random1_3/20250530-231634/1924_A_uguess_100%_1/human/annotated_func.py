#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^5) followed by t test cases. Each test case consists of two lines. The first line contains three integers n (1 <= n <= 26), k (1 <= k <= 26), and m (1 <= m <= 1000). The second line contains a string s of length m, comprising only of the first k lowercase English alphabets.
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
        
    #State: t is an integer between 1 and 10^5, i is equal to t, stdin contains 0 test cases, n is an integer between 1 and 26, k is an integer between 1 and 26, m is an integer between 1 and 1000, s is an empty string, cnt is an integer between 0 and the length of s divided by k, cur is 0, and ans is a string containing every kth character of the original string s plus tmp plus (n - cnt - 1) 'a's, where tmp is a string containing the kth letter of the alphabet. If cnt is greater than or equal to n, 'YES' is printed. Otherwise, 'NO' is printed, and the string ans is printed.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints output for each case. It takes no parameters and returns no value. For each test case, it reads three integers (n, k, m) and a string s of length m, then checks if the string contains at least n sequences of k distinct characters. If it does, it prints 'YES'. Otherwise, it prints 'NO' and appends a string to the last sequence found, making it a complete sequence of k distinct characters, and prints the resulting string.

