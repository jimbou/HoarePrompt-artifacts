#State of the program right berfore the function call: stdin contains multiple test cases. The first line of each test case contains a single integer n (1 <= n <= 2 * 10^5). The second line of each test case contains n integers a_1, a_2, ..., a_n (0 <= a_i < n).
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
        
    #State: T is an integer and must be at least T, _ is T-1, S is an integer, N is an empty list, M is a dictionary where each key is an integer and its corresponding value is the number of times that integer appears in the original list N, and the sum of the values in dictionary M equals S. If the value of M[i] is less than or equal to the current value of i, then cur is the value of i. Otherwise, no changes are made to cur, and the value of cur is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a single integer n followed by n integers. It then processes each test case by sorting the integers, counting the occurrences of each integer, and determining the maximum value that can be represented by the given integers. The function prints the maximum representable value for each test case.

