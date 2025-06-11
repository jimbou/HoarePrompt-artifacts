#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^5), followed by t test cases. Each test case contains three integers n (1 <= n <= 26), k (1 <= k <= 26), and m (1 <= m <= 1000), followed by a string s of length m, comprising only of the first k lowercase English alphabets.
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
        
    #State: t is an integer between 0 and 10^5 (inclusive), i is an integer equal to t, n is an integer, k is an integer, m is an integer, s is an empty string, ss is an empty string, cur_ss is an integer between 0 and 25 (inclusive), cnt is an integer, ans is a string, tmp is an empty string, and cur is 0. If cnt is greater than or equal to n, 'YES' is printed. Otherwise, 'NO' is printed along with the string ans.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints output. It accepts no parameters and returns no value. It reads an integer t, representing the number of test cases, followed by t test cases. Each test case consists of three integers n, k, and m, and a string s of length m. The function then checks if a certain condition is met, and if so, prints 'YES'. Otherwise, it prints 'NO' along with a constructed string. The function processes all test cases and prints the corresponding output for each case.

