#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (2 <= n <= 10^5) and then a list of n integers a_1,a_2,...,a_n (1 <= a_i <= 10^9). The number of test cases t (1 <= t <= 500) is given in the first line.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        max = 0
        
        for i in range(1, n):
            if min(a[i], a[i - 1]) > max:
                max = min(a[i], a[i - 1])
        
        print(max)
        
    #State: The maximum of the minimum of adjacent pairs in each test case is printed to the console, and the value of `t` is unchanged.

#Overall this is what the function does:Reads multiple test cases from standard input, where each test case consists of an integer n and a list of n integers. For each test case, it finds the maximum of the minimum values of adjacent pairs in the list and prints this value to the console. The function does not modify the input values or return any values, only printing the results for each test case.

