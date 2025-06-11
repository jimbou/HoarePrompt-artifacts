#State of the program right berfore the function call: stdin contains multiple test cases. The first line of stdin contains a single integer t (1 <= t <= 2 * 10^4), representing the number of test cases. Each test case consists of two lines. The first line of each test case contains a single integer n (1 <= n <= 2 * 10^5). The second line of each test case contains n integers a_1, a_2, ..., a_n (0 <= a_i < n).
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
        
    #State: The output state will be the largest integer `cur` such that the number of elements in the sorted list `N` that are less than or equal to `cur` is greater than `cur`. This value will be printed for each test case. The value of `T` will remain unchanged, as it is not modified within the loop. The input state of `stdin` will also remain unchanged, as the loop only reads from it and does not modify it.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a list of integers. It then processes each list by sorting it, counting the occurrences of each integer, and finding the largest integer 'cur' such that the number of elements less than or equal to 'cur' is greater than 'cur'. The function prints the value of 'cur' for each test case, effectively determining the maximum value that satisfies the given condition for each input list.

