#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains three integers n, k, and m. The second line contains a string s of length m. n, k, and m are integers such that 1 <= n <= 26, 1 <= k <= 26, and 1 <= m <= 1000. s consists only of the first k lowercase English alphabets.
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
        
    #State: The loop has executed all the iterations and has printed the output for each test case. The value of t is now 0, and the stdin is empty. The variables n, k, m, s, cnt, and cur are no longer in scope. The output of the program is a series of 'YES' or 'NO' followed by a string for each test case. The string is either empty (if the answer is 'YES') or a string of length n consisting of the first k lowercase English alphabets (if the answer is 'NO').

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three integers (n, k, m) and a string s of length m. It checks if the string s contains at least n substrings of length k, where each substring consists of distinct characters from the first k lowercase English alphabets. If such substrings are found, it prints 'YES'. Otherwise, it prints 'NO' followed by a string of length n, which is a combination of the longest substring found and additional characters to fill the length n. The function processes all test cases and prints the output for each case.

