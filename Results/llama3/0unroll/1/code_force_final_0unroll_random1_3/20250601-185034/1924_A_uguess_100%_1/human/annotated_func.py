#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^5), followed by t test cases. Each test case consists of a line containing three integers n (1 <= n <= 26), k (1 <= k <= 26), and m (1 <= m <= 1000), followed by a line containing a string s of length m, comprising only of the first k lowercase English alphabets.
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
        
    #State: The output state is a string of length n, where n is the number of test cases. Each character in the string is either 'YES' or 'NO', indicating whether the corresponding test case has a solution or not. If the test case has a solution, the string contains 'YES'. If the test case does not have a solution, the string contains 'NO' followed by a string of length n-1, which is a possible solution for the test case. The possible solution is constructed by appending the first missing character in the string s to the string ans, and then appending 'a' (the first lowercase English alphabet) repeatedly until the length of the string is n-1.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and outputs a string indicating whether each test case has a solution or not. For each test case, it checks if a given string contains all k lowercase English alphabets at least n times. If a solution exists, it outputs 'YES'. If not, it outputs 'NO' followed by a possible solution string of length n-1, constructed by appending the first missing character and then 'a's. The function processes all test cases and outputs the results accordingly.

