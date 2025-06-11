#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines: the first line contains an integer n (1 ≤ n ≤ 3 * 10^5), and the second line contains n integers a_1, a_2, ..., a_n (0 ≤ a_i ≤ n). The sum of n over all test cases does not exceed 3 * 10^5.
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
        
    #State: t is 0, n is an integer (1 ≤ n ≤ 3 * 10^5), num_of_lens is a dictionary with all elements of nums as keys and their counts as the values, where the count of each element is increased by the number of times it appears in the list, nums is an empty list, x is the last element in the list, _ is t, res is the sum of the number of ways to choose 3 elements from cnt elements plus the product of the number of ways to choose 2 elements from cnt elements and the total sum of the values in num_of_lens excluding cnt for all cnt in num_of_lens, stdin contains no test cases, and the sum of all combinations of counts of elements in num_of_lens which is res is being printed

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and a list of n integers. It calculates the sum of combinations of counts of elements in the list, specifically the number of ways to choose 3 elements from each count and the product of the number of ways to choose 2 elements from each count and the total sum of other counts. The function then prints the calculated sum for each test case.

