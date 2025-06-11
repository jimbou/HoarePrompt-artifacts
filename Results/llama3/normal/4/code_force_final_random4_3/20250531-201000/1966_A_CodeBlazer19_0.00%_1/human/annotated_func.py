#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t test cases. Each test case consists of two lines. The first line contains two integers n and k (1 <= n <= 100, 2 <= k <= 100). The second line contains n integers c_1, c_2, ..., c_n (1 <= c_i <= 100).
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        print(k - 1)
        
    #State: t is 0, n is an integer between 1 and 100, k is an integer between 2 and 100, l is a list of n integers between 1 and 100, i is t-1, stdin contains 0 test cases, and k-1 is printed t times, where k-1 is an integer between 1 and 99.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of two integers (n and k) and a list of n integers. It then prints k-1 for each test case, effectively ignoring the list of integers. The function does not modify the input variables or perform any calculations beyond reading and printing. Its purpose is to simply output k-1 for each test case, without altering the state of the program or the input variables.

