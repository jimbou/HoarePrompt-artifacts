#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines: the first line contains one integer n (1 ≤ n ≤ 3 * 10^5), and the second line contains n integers a_1, a_2, ..., a_n (0 ≤ a_i ≤ n).
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        
        idx += 1
        
        v = [0] * (n + 1)
        
        for _ in range(n):
            x = int(data[idx])
            idx += 1
            v[x] += 1
        
        cnt = 0
        
        ans = 0
        
        for i in range(n + 1):
            if v[i] >= 2:
                ans += cnt * v[i] * (v[i] - 1) // 2
            if v[i] >= 3:
                ans += v[i] * (v[i] - 1) * (v[i] - 2) // 6
            cnt += v[i]
        
        results.append(str(ans))
        
    #State: `t` is 0, `idx` is the length of `data`, `results` is a list containing the string representation of the sum of `cnt * v[i] * (v[i] - 1) // 2` for all `i` where `v[i]` is greater than or equal to 2, plus `v[i] * (v[i] - 1) * (v[i] - 2) // 6` for all `i` where `v[i]` is greater than or equal to 3, for each test case, `data` is empty, `_` is the last value of `n`, `n` is the last value of `n`, `v` is a list of zeros with a length equal to the last value of `n` + 1, `i` is the last value of `n`, `cnt` is the sum of all elements in the last `v`, and `ans` is the sum of `cnt * v[i] * (v[i] - 1) // 2` for all `i` where `v[i]` is greater than or equal to 2, plus `v[i] * (v[i] - 1) * (v[i] - 2) // 6` for all `i` where `v[i]` is greater than or equal to 3, for the last test case.
    print('\n'.join(results))
    #This is printed: the string representation of the sum of cnt * v[i] * (v[i] - 1) // 2 for all i where v[i] is greater than or equal to 2, plus v[i] * (v[i] - 1) * (v[i] - 2) // 6 for all i where v[i] is greater than or equal to 3, for each test case, separated by newline characters

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by n integers. It calculates the sum of combinations for each test case, specifically the sum of cnt * v[i] * (v[i] - 1) // 2 for all i where v[i] is greater than or equal to 2, plus v[i] * (v[i] - 1) * (v[i] - 2) // 6 for all i where v[i] is greater than or equal to 3. The results for each test case are stored in a list and then printed, separated by newline characters.

