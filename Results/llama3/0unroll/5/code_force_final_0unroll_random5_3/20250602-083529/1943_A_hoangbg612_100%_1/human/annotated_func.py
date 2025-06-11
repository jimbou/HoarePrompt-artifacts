#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 2 * 10^4) — the number of test cases. Each test case contains two lines. The first line of each test case contains a single integer n (1 ≤ n ≤ 2 * 10^5). The second line of each test case contains n integers a_1, a_2, …, a_n (0 ≤ a_i < n).
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
        
    #State: The loop will print the maximum possible value of 'cur' for each test case, which is the maximum number that can be formed using the given numbers, considering the constraints that the numbers must be in increasing order and each number can be used only once. The output will be the maximum possible value of 'cur' for each test case, separated by a newline character.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a list of integers. It then processes each list to find the maximum possible value that can be formed using the given numbers, considering the constraints that the numbers must be in increasing order and each number can be used only once. The function prints the maximum possible value for each test case, separated by a newline character.

