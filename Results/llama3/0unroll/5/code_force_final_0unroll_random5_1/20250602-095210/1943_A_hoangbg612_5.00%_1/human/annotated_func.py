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
        
        for i in range(cur):
            if M[i] <= i:
                cur = i
                break
        
        print(cur)
        
    #State: The output state is the maximum number of elements that can be selected from the input list such that the selected elements are in non-decreasing order and the number of selected elements is equal to the number of elements in the input list. The output is calculated for each test case and printed separately.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a list of integers. It then determines the maximum number of elements that can be selected from the list such that the selected elements are in non-decreasing order and the number of selected elements is equal to the number of elements in the list. The function prints the maximum number of elements that can be selected for each test case.

