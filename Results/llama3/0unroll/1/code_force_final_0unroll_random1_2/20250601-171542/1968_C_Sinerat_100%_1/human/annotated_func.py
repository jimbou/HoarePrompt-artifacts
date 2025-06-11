#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines of input. The first line contains a single integer n (2 <= n <= 500). The second line contains n-1 integers x_2,...,x_n (1 <= x_i <= 500). The number of test cases is a single integer t (1 <= t <= 10^4) which is given in the first line of the input.
    for _ in range(int(input())):
        n = int(input())
        
        x = list(map(int, input().split()))
        
        a = [0] * n
        
        a[0] = 1000
        
        for i in range(1, n):
            a[i] = a[i - 1] + x[i - 1]
        
        print(*a)
        
    #State: The output state will contain the same number of test cases as the initial state. Each test case will contain a list of n integers, where n is the same as in the initial state. The first integer in each list will be 1000, and each subsequent integer will be the sum of the previous integer and the corresponding integer from the initial state. For example, if the initial state contains a test case with n=3 and x=[2, 3], the output state will contain a test case with the list [1000, 1002, 1005].

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of a single integer n and a list of n-1 integers. It then generates a new list of n integers, where the first integer is 1000, and each subsequent integer is the sum of the previous integer and the corresponding integer from the input list. The function prints each generated list as output, with the same number of test cases as the input.

