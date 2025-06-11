#State of the program right berfore the function call: test_cases is a list of test cases. Each test case is a list of two elements: the first element is an integer n, and the second element is a list of n integers a_1, a_2, ..., a_n, where 0 <= a_i <= n.
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
        
    #State: Output State: The `results` list is populated with the calculated results for each test case. The length of the `results` list is equal to the number of test cases. Each element in the `results` list represents the total number of ways to choose three numbers from the corresponding test case that sum up to the length of the test case. The `test_cases` list remains unchanged.
    for result in results:
        print(result)
        
    #State: Output State: The `results` list is empty. The `test_cases` list remains unchanged.

#Overall this is what the function does:This function calculates and prints the total number of ways to choose three numbers from each test case that sum up to the length of the test case. It accepts a list of test cases as input, where each test case is a list of two elements: an integer n and a list of n integers. The function processes each test case, counts the occurrences of each number, and calculates the total number of ways to choose three numbers that sum up to n. The results are stored in a list and printed out. The original test cases remain unchanged.

