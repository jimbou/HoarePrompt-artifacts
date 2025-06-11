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
        
    #State: `i` is the number of test cases, `n` is an integer, `k` is an integer, `l` is an empty list, `c` is 0, `maxi` is 0, stdin contains 0 inputs, and the result of the expression `(2

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case consists of two lines. The first line contains two integers, n and k, and the second line contains n integers. The function calculates a result for each test case by iterating through the integers, keeping track of the maximum sum of consecutive non-negative integers and the sum of all integers. It then prints the result of an expression involving the maximum sum, the sum of all integers, and the values of k and n, modulo 1000000007. After processing all test cases, the function leaves the input stream empty and returns no value.

