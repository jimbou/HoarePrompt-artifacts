#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains three integers n, k, and m, where n, k, and m are non-negative integers and 1 <= n <= 26 and 1 <= k <= 26 and 1 <= m <= 1000. The second line contains a string s of length m, comprising only of the first k lowercase English alphabets.
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
        
    #State: The program prints 'YES' if the number of times a substring of length k with different characters appears in the string s is greater than or equal to n, otherwise it prints 'NO' and a string "ans" of length n, comprising only of the character 'a' plus k minus 1.

#Overall this is what the function does:The function determines if a given string contains a specified number of substrings with distinct characters of a certain length. If the condition is met, it prints 'YES'. Otherwise, it prints 'NO' and generates a string of a specified length, consisting of a specific character repeated a certain number of times, followed by another character, and then the first character repeated again to fill the remaining length.

