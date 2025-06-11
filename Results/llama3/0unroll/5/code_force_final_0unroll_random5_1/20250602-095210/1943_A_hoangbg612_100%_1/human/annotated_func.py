#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains a single integer n (1 <= n <= 2 * 10^5). The second line contains n integers a_1, a_2, ..., a_n (0 <= a_i < n).
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
        
    #State: The output state after the loop executes all the iterations is the number of test cases T, where each test case contains a single integer representing the maximum value that can be obtained by incrementing the elements in the array N, without exceeding the maximum value in N, and ensuring that the total count of elements in N is equal to the length of N. If there are multiple such maximum values, the second smallest one is chosen.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by n integers. It then processes each test case by sorting the integers, identifying the maximum value that can be obtained by incrementing elements without exceeding the maximum value, and ensuring the total count of elements equals the length of the input array. If multiple such maximum values exist, it selects the second smallest one. The function outputs the maximum value for each test case.

