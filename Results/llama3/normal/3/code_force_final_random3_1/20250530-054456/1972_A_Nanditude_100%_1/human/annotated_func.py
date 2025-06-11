#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three lines. The first line contains a positive integer n (1 ≤ n ≤ 100). The second line contains a list of n non-decreasing integers a_1, a_2, …, a_n (1 ≤ a_i ≤ 10^9). The third line contains a list of n non-decreasing integers b_1, b_2, …, b_n (1 ≤ b_i ≤ 10^9).
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        b = list(map(int, input().split()))
        
        cnt = 0
        
        i = 0
        
        for j in range(n):
            if b[j] < a[i]:
                cnt += 1
            else:
                i += 1
        
        print(cnt)
        
    #State: t is 0, _ is t, stdin is empty, n is a positive integer that must be at least 1, a is a list of n non-decreasing integers, b is a list of n non-decreasing integers, cnt is a non-negative integer, i is n, and j is n.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a positive integer n and two lists of n non-decreasing integers, a and b. It then counts the number of elements in b that are less than the current element in a, and prints this count for each test case. The function does not return any value, but rather prints the results directly to standard output.

