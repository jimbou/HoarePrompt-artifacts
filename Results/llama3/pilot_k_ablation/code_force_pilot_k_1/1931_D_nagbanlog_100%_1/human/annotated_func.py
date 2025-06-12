#State of the program right berfore the function call: t is a positive integer, test_cases is a list of test cases where each test case is a list of three elements: n, x, y, and a list of n integers a_1, a_2, ..., a_n. n is an integer such that 2 <= n <= 2 * 10^5, x and y are integers such that 1 <= x, y <= 10^9, and a_i is an integer such that 1 <= a_i <= 10^9 for all i. The sum of n over all test cases does not exceed 2 * 10^5.
    results = []
    for case in test_cases:
        n, x, y = case['params']
        
        a = case['array']
        
        freq = defaultdict(int)
        
        beautiful_count = 0
        
        for num in a:
            mod_x = num % x
            mod_y = num % y
            required_mod_x = (x - mod_x) % x
            required_mod_y = mod_y
            if (required_mod_x, required_mod_y) in freq:
                beautiful_count += freq[required_mod_x, required_mod_y]
            freq[mod_x, mod_y] += 1
        
        results.append(beautiful_count)
        
    #State: `t` is a positive integer, `test_cases` is a list of test cases, `results` is a list containing the beautiful count of each test case in `test_cases`.
    return results
    #The program returns a list of beautiful counts, where each beautiful count corresponds to a test case in the list `test_cases`, and the list has the same length as `test_cases`.

#Overall this is what the function does:This function calculates the beautiful count for each test case in the provided list of test cases. It takes a list of test cases as input, where each test case contains a list of integers and two integers x and y. The function returns a list of beautiful counts, where each count corresponds to a test case in the input list. The beautiful count is calculated by counting the number of pairs of integers in the test case that satisfy a certain modular arithmetic condition with respect to x and y. The function processes each test case independently and returns a list of beautiful counts with the same length as the input list of test cases.

