#State of the program right berfore the function call: stdin contains t test cases. Each test case consists of two lines: the first line contains one integer n, and the second line contains n integers a_1, a_2, ..., a_n. 1 <= t <= 10^4, 1 <= n <= 3 * 10^5, 0 <= a_i <= n. The sum of n over all test cases does not exceed 3 * 10^5.
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
        
    #State: The loop will have executed t times, with the value of t being an integer between 1 and 10^4. The stdin will be empty, as all test cases will have been processed. The output will be a series of integers, each representing the result of the calculation for a test case. The number of integers in the output will be equal to t-1. The value of n will be the last value read from stdin, and the value of num_of_lens will be a dictionary containing the count of each number in the last test case. The value of nums will be a list of integers representing the last test case. The value of res will be the result of the calculation for the last test case.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of a list of integers. It calculates the number of triplets and pairs that can be formed from the integers in each test case, taking into account the frequency of each integer. The function then prints the total count of triplets and pairs for each test case. After processing all test cases, the function leaves the standard input empty and produces a series of output integers, each representing the result of the calculation for a test case.

