#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains a single integer n (1 ≤ n ≤ 2 * 10^5). The second line contains n integers a_1, a_2, …, a_n (0 ≤ a_i < n).
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
        
    #State: T is 0, _ is T, S is an integer, N is an empty list, M is a dictionary where keys are integers from the original list N and values are their respective counts, cnt is a list containing all keys in M with a value of 1, stdin is empty. If the sum of the values in dictionary M equals S, then cur is 0. If the length of cnt is at least 2, then cur is the second element in the list cnt. Otherwise, no changes are made to cur, and cur is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a single integer n followed by n integers. It processes each test case by sorting the integers, counting their occurrences, and identifying the smallest missing integer. If the sum of the counts equals the original number of integers, it increments the smallest missing integer. If there are at least two integers with a count of 1, it updates the smallest missing integer to the second such integer. Finally, it prints the smallest missing integer for each test case.

