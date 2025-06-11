#State of the program right berfore the function call: stdin contains multiple test cases. The first line of stdin contains a single integer t (1 ≤ t ≤ 2 * 10^4) — the number of test cases. Each test case contains two lines. The first line of each test case contains a single integer n (1 ≤ n ≤ 2 * 10^5). The second line of each test case contains n integers a_1, a_2, …, a_n (0 ≤ a_i < n).
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
        
    #State: T is 0, S is an integer, N is a list with at least one integer, _ is T-1, M is a dictionary with key-value pairs where the key is an integer from the original list N and the value is the count of consecutive occurrences of that integer, num is the last integer in the original list N, k is the last key in M. If there are at least two keys in M with a value of 1, cur is the second element in cnt, and cnt is a list containing all keys in M where the value equals 1 and has at least two elements. Otherwise, the state of the variables remains unchanged. The value of cur is being printed, where cur is the second element in cnt which is a list containing all keys in M where the value equals 1 and has at least two elements.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a list of integers. It processes each test case by sorting the integers, identifying consecutive sequences, and counting their occurrences. If there are at least two sequences with a single occurrence, it returns the second smallest integer from these sequences. Otherwise, it returns the next integer after the largest sequence. The function prints the result for each test case.

