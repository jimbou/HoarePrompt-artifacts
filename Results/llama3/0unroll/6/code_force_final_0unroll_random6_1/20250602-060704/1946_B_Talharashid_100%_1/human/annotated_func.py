#State of the program right berfore the function call: stdin contains several test cases. Each test case contains two lines. The first line contains two integers n and k (1 <= n, k <= 2 * 10^5). The second line contains n integers a_1, a_2, ..., a_n (-10^9 <= a_i <= 10^9).
    for i in range(int(input())):
        n, k = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        c = 0
        
        maxi = 0
        
        for ele in l:
            if ele < 0 and c <= abs(ele):
                maxi = max(c, maxi)
                c = 0
            else:
                c += ele
                maxi = max(c, maxi)
        
        maxi = max(c, maxi)
        
        print((2 ** k * maxi - maxi + sum(l)) % 1000000007)
        
    #State: The output state after the loop executes all the iterations is a list of integers, each representing the result of the calculation (2

#Overall this is what the function does:The function processes multiple test cases from standard input, where each test case consists of two lines. The first line contains two integers, n and k, and the second line contains n integers. The function calculates a result for each test case by iterating through the integers, maintaining a running sum and maximum value, and then applies a formula involving the maximum value, the sum of the integers, and the value of k. The result is then printed to the console, with the output being a list of integers representing the results of the calculations for each test case.

