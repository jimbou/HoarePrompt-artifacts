#State of the program right berfore the function call: test_cases is a list of test cases, where each test case is a list containing an integer n and a list of n integers a_1, a_2, ..., a_n, where 1 <= n <= 3 * 10^5 and 0 <= a_i <= n.
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
        
    #State: Output State: The `results` list contains the number of triplets that can be formed from the given list of integers for each test case.
    for result in results:
        print(result)
        
    #State: Output State: The `results` list is empty, and the number of triplets that can be formed from the given list of integers for each test case has been printed to the console.

#Overall this is what the function does:This function calculates and prints the number of triplets that can be formed from a list of integers for each test case. It accepts a list of test cases as input, where each test case contains an integer n and a list of n integers. The function processes each test case, counts the occurrences of each integer, and calculates the number of triplets that can be formed using the counted integers. Finally, it prints the calculated number of triplets for each test case.

