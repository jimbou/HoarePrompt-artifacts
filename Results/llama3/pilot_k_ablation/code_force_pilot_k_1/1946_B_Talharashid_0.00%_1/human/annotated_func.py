#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains two integers n and k (1 <= n, k <= 2 * 10^5). The second line contains n integers a_1, a_2, ..., a_n (-10^9 <= a_i <= 10^9).
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
        
        print((2 ** k * maxi - maxi + sum(l)) % 1000000007)
        
    #State: `i` is equal to the number of test cases, `n` is an integer, `k` is an integer, `l` is an empty list, `c` is 0, `maxi` is 0, `ele` does not exist (since the loop has finished), and the output of the expression `(2

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case consists of two lines. The first line contains two integers n and k, and the second line contains n integers. The function calculates a value based on these inputs, using a cumulative sum and maximum value, and prints the result modulo 1000000007 for each test case. The function does not modify the input values or store any results, and its final state is the same as the initial state, with all variables reset to their default values.

