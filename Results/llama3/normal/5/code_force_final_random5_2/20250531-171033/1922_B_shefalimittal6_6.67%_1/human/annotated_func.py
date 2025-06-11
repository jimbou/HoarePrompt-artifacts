#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines: the first line contains one integer n (1 <= n <= 3 * 10^5), and the second line contains n integers a_1, a_2, ..., a_n (0 <= a_i <= n). The sum of n over all test cases does not exceed 3 * 10^5.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        num_of_lens = {}
        
        nums = list(map(int, input().split()))
        
        for x in nums:
            num_of_lens[x] = num_of_lens.get(x, 0) + 1
        
        res = 0
        
        for cnt in num_of_lens.values():
            if cnt >= 3:
                res += math.comb(cnt, 3)
            if cnt >= 2:
                total_sum = sum(i for i in num_of_lens.values() if i != cnt)
                res += math.comb(cnt, 2) * total_sum
        
        print(res)
        
    #State: `t` is 0, `_` is `t`, `n` is an integer between 1 and 3 * 10^5, `num_of_lens` is an empty dictionary, `nums` is an empty list, `x` is not defined, `cnt` is not defined, and `res` is not defined.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by n integers. It calculates the number of combinations of these integers that can form pairs or triplets, and prints the total count for each test case. The function does not modify the input data and does not return any value, only printing the results to standard output.

