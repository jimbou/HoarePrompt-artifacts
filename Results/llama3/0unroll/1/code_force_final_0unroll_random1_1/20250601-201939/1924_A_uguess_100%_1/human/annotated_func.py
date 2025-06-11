#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^5) followed by t test cases. Each test case consists of a line with three integers n (1 <= n <= 26), k (1 <= k <= 26), and m (1 <= m <= 1000), followed by a line with a string s of length m consisting only of the first k lowercase English alphabets.
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
        
    #State: The loop has executed t times, and for each execution, it has processed a test case from the input. The output will be either 'YES' or 'NO' for each test case, followed by a string if the answer is 'NO'. The string will be the original string s with additional characters appended to it to make its length equal to n. The additional characters will be the first character of the alphabet that is not present in the current substring of s, followed by 'a's. The state of the other variables remains unchanged.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and outputs the result for each case. It checks if a given string can be extended to a certain length by appending specific characters, and if so, prints 'YES'. If not, it prints 'NO' followed by the extended string. The function iterates through the input test cases, processing each one independently, and outputs the results in the specified format.

