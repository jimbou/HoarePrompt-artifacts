#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two lines: the first line contains one integer n, and the second line contains n integers a_1, a_2, ..., a_n. 1 <= t <= 10^4, 1 <= n <= 3 * 10^5, and 0 <= a_i <= n. The sum of n over all test cases does not exceed 3 * 10^5.
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
        
    #State: The loop has executed t times, and for each execution, it has printed the number of triplets that can be formed from the given array of integers. The value of t remains unchanged, and the stdin is empty after the loop finishes.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by n integers. It then calculates and prints the number of triplets that can be formed from the given array of integers, considering both triplets with distinct elements and triplets with repeated elements. The function processes all test cases and prints the result for each case, leaving the standard input empty after execution.

