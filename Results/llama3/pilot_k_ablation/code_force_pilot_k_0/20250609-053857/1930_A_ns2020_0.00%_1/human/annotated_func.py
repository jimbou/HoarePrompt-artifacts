#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains an integer n (1 ≤ n ≤ 50). The second line contains 2n integers a_1,a_2,…,a_{2n} (1 ≤ a_i ≤ 10^7).
    t = int(input())
    while t:
        n = int(input())
        
        A = list(map(int, input().split()))
        
        print(sum(A[::2]))
        
        t = t - 1
        
    #State: t = 0, n = None, A = None

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by 2n integers. It then calculates and prints the sum of every other integer (starting from the first) from the 2n integers for each test case, effectively processing all test cases until there are none left.

