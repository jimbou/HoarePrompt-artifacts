#State of the program right berfore the function call: t is a positive integer, test_cases is a list of test cases, each test case is a list of three elements: the first element is a positive integer n, the second and third elements are positive integers x and y, and a list of n positive integers.
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
        
    #State: Output State: `t` is a positive integer, `test_cases` is a list of test cases, each test case is a list of three elements: the first element is a positive integer `n`, the second and third elements are positive integers `x` and `y`, and a list of `n` positive integers, `results` is a list of integers, where each integer represents the count of beautiful pairs in the corresponding test case.
    return results
    #The program returns a list of integers, where each integer represents the count of beautiful pairs in the corresponding test case. The list has the same length as the number of test cases in the `test_cases` list. Each integer in the list is calculated based on the corresponding test case, which includes a positive integer `n`, two positive integers `x` and `y`, and a list of `n` positive integers.

#Overall this is what the function does:This function calculates the count of beautiful pairs in each test case and returns a list of these counts. A beautiful pair is defined as two numbers in the array that satisfy certain modular arithmetic conditions based on the given integers x and y. The function takes a list of test cases as input, where each test case includes a positive integer n, two positive integers x and y, and a list of n positive integers. It processes each test case, calculates the count of beautiful pairs, and returns a list of these counts, one for each test case.

