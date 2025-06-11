#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three lines: the first line contains a positive integer n (1 ≤ n ≤ 100), the second line contains a list of n non-decreasing integers a_1 ≤ a_2 ≤ ⋯ ≤ a_n (1 ≤ a_i ≤ 10^9), and the third line contains a list of n non-decreasing integers b_1 ≤ b_2 ≤ ⋯ ≤ b_n (1 ≤ b_i ≤ 10^9).
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
        
    #State: The number of elements in b that are less than the corresponding elements in a, for each test case, is printed to the console. The input state remains unchanged, with stdin still containing the multiple test cases.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a positive integer n and two lists of n non-decreasing integers, a and b. For each test case, it counts the number of elements in list b that are less than the corresponding elements in list a and prints this count to the console. The function does not modify the input state, leaving the standard input unchanged.

