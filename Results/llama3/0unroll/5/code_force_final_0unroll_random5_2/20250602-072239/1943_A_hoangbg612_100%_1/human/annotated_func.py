#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains a single integer t (1 <= t <= 2 * 10^4). Each test case contains two lines. The first line contains a single integer n (1 <= n <= 2 * 10^5). The second line contains n integers a_1, a_2, ..., a_n (0 <= a_i < n).
    T = int(input())
    for _ in range(T):
        S = int(input())
        
        N = list(map(int, input().split()))
        
        N.sort()
        
        cur = -1
        
        M = {}
        
        for num in N:
            if num > cur:
                if num > cur + 1:
                    cur += 1
                    break
                cur = num
                M[cur] = 1
            else:
                M[cur] += 1
        
        if sum([M[k] for k in M.keys()]) == S:
            cur += 1
        
        cnt = []
        
        for k in M.keys():
            if M[k] == 1:
                cnt.append(k)
        
        if len(cnt) >= 2:
            cur = cnt[1]
        
        print(cur)
        
    #State: The output state is a list of integers, where each integer is the value of `cur` after the loop executes for each test case. The value of `cur` is determined by the maximum value in the sorted list `N` that is not greater than `cur + 1`, or the second smallest value in `N` if there are at least two values with a count of 1 in the dictionary `M`. The output state will contain `T` integers, where `T` is the number of test cases.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains a list of integers. It sorts the list, identifies the maximum value that is not greater than the current value plus one, and updates the current value accordingly. If there are at least two values with a count of 1 in the list, it updates the current value to the second smallest value. The function then prints the final current value for each test case.

