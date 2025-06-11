#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains two integers n and k (1 <= n <= 2 * 10^5, 0 <= k <= 10^12). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^12).
    ans_list = []
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        ans = a[0]
        
        res = n - 1
        
        for i in range(n - 1):
            dif = a[i + 1] - a[i]
            if dif == 0:
                res -= 1
            if dif != 0:
                if k >= dif * (i + 1):
                    ans += dif
                    k -= dif * (i + 1)
                    res -= 1
                else:
                    ans += k // (i + 1)
                    if i != 0:
                        res += k % (i + 1)
                    k = 0
                    break
                if k == 0:
                    break
        
        if k != 0:
            ans += k // n
            res += k % n
        
        ans += (ans - 1) * (n - 1)
        
        ans += res
        
        ans_list.append(ans)
        
    #State: ans_list contains the values of ans for all test cases, _ is the number of test cases minus 1, n is a positive integer, a is a sorted list of positive integers, stdin is empty, i is n - 1, dif is a[n - 1] - a[n - 2], ans is the smallest integer in a plus the sum of dif if k is greater than or equal to dif times the current value of i, otherwise ans is the smallest integer in a plus the sum of k // (i + 1), res is 0 if k is greater than or equal to dif times the current value of i, otherwise res is n - 1 plus the sum of k modulo i + 1 if i is not 0, otherwise res is n - 1, and k is either increased by k // n and res is increased by k % n, or k remains 0.
    for a in ans_list:
        print(a)
        
    #State: `ans_list` contains the values of `ans` for all test cases, `a` is the last value in the list, _ is the number of test cases minus 1, `n` is a positive integer, `a` is a sorted list of positive integers, `stdin` is empty, `i` is `n` - 1, `dif` is `a[n - 1]` - `a[n - 2]`, `ans` is the smallest integer in `a` plus the sum of `dif` if `k` is greater than or equal to `dif` times the current value of `i`, otherwise `ans` is the smallest integer in `a` plus the sum of `k` // (`i` + 1), `res` is 0 if `k` is greater than or equal to `dif` times the current value of `i`, otherwise `res` is `n` - 1 plus the sum of `k` modulo `i` + 1 if `i` is not 0, otherwise `res` is `n` - 1, and `k` is either increased by `k` // `n` and `res` is increased by `k` % `n`, or `k` remains 0, and the sorted list of positive integers `a` is being printed

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines: the first line contains two integers n and k, and the second line contains n integers. The function sorts the integers, calculates a value 'ans' based on the sorted integers and the value of k, and appends this value to a list. After processing all test cases, the function prints the calculated values for each test case. The calculated value 'ans' represents the smallest integer in the sorted list plus the sum of differences between consecutive integers if k is sufficient, otherwise it's the smallest integer plus the sum of k divided by the current index.

