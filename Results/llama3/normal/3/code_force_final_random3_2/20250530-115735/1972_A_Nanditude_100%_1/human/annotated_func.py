#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three lines: the first line contains a positive integer n (1 ≤ n ≤ 100), the second line contains a list of n non-decreasing integers a (1 ≤ a1 ≤ a2 ≤ ⋯ ≤ an ≤ 10^9), and the third line contains a list of n non-decreasing integers b (1 ≤ b1 ≤ b2 ≤ ⋯ ≤ bn ≤ 10^9).
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
        
    #State: _ is t, t is a positive integer, n is a positive integer between 1 and 100, a is a list of n non-decreasing integers between 1 and 10^9, b is a list of n non-decreasing integers between 1 and 10^9, cnt is a non-negative integer less than or equal to n, i is a non-negative integer less than or equal to n, j is 0, and stdin contains no more test cases.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a positive integer n and two lists of n non-decreasing integers a and b. It then calculates the number of elements in list b that are less than the corresponding elements in list a and prints this count for each test case. The function does not modify the input lists or any other external state, and it does not return any value.

