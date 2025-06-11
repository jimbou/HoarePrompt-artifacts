#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 2 * 10^4) — the number of test cases. For each test case, the first line contains a single integer n (1 ≤ n ≤ 2 * 10^5), and the second line contains n integers a_1, a_2, …, a_n (0 ≤ a_i < n).
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
        
    #State: T is 0, S is an integer equal to the input value, N is an empty list, num is not defined, M is a dictionary that must have at least as many keys as the number of iterations of the loop, k is the last key in the dictionary M. If the value of M[k] is 1 and cnt has at least two elements, then cnt is a list containing at least two elements, where the last key k of dictionary M has a value of 1, and cur is equal to the second element of cnt. Otherwise, cnt remains an empty list, and the value of cur is being printed, where cur is equal to the second element of cnt if cnt has at least two elements and the value of M[k] is 1, otherwise cur is undefined.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a list of integers. It processes each list by sorting it, identifying the longest contiguous subsequence, and then finding the smallest missing number in that subsequence. If the smallest missing number is not present in the original list, it is incremented by 1. If there are multiple single-element subsequences, the function returns the second smallest missing number. Otherwise, it returns the smallest missing number. The function prints the result for each test case.

