#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains a single integer n (2 <= n <= 100). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
    ntest = int(input())
    for itest in range(0, ntest, 1):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        kq = 0
        
        for i in range(0, len(a) // 2, 1):
            kq = kq + a[len(a) - i - 1] - a[i]
        
        print(kq)
        
    #State: The loop has executed `ntest` times, and for each test case, it has printed the difference between the sum of the largest half of the numbers and the sum of the smallest half of the numbers. The value of `ntest` remains unchanged.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a list of integers. For each test case, it calculates and prints the difference between the sum of the largest half of the numbers and the sum of the smallest half of the numbers. The function does not return any value, but instead, prints the results for each test case.

