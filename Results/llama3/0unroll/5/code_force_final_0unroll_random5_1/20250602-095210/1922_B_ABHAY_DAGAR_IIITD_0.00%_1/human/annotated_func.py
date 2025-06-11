#State of the program right berfore the function call: test_cases is a list of lists of integers, where the first element of each sublist is an integer n (1 <= n <= 3 * 10^5) and the second element is a list of n integers a_1, a_2, ..., a_n (0 <= a_i <= n).
    results = []
    for _ in range(test_cases):
        n = int(input())
        
        num_list = list(map(int, input().split()))
        
        num_of_lens = {}
        
        for x in num_list:
            if x in num_of_lens:
                num_of_lens[x] += 1
            else:
                num_of_lens[x] = 1
        
        res = 0
        
        total_count = 0
        
        for cnt in num_of_lens.values():
            if cnt >= 3:
                res += cnt * (cnt - 1) * (cnt - 2) // 6
            if cnt >= 2:
                res += cnt * (cnt - 1) // 2 * total_count
            total_count += cnt
        
        results.append(res)
        
    #State: The `results` list contains the number of triplets that can be formed from the given list of integers for each test case. The `test_cases` list remains unchanged.
    for result in results:
        print(result)
        
    #State: Output State: The `results` list remains unchanged, and the `test_cases` list remains unchanged.

#Overall this is what the function does:This function calculates the number of triplets that can be formed from a given list of integers for each test case. It accepts a list of test cases, where each test case consists of a list of integers, and returns a list of results, where each result is the number of triplets that can be formed from the corresponding test case. The function does not modify the input test cases.

