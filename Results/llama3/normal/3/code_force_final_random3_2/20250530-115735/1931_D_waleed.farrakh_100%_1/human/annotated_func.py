#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains four values: n, x, y, and arr. n is a positive integer, x and y are positive integers, and arr is a list of positive integers.
    results = []
    for (n, x, y, arr) in test_cases:
        freq = {}
        
        count = 0
        
        for a in arr:
            rx = (-a % x + x) % x
            ry = a % y
            if (rx, ry) in freq:
                count += freq[rx, ry]
            current_pair = a % x, a % y
            if current_pair in freq:
                freq[current_pair] += 1
            else:
                freq[current_pair] = 1
        
        results.append(count)
        
    #State: The final state of the loop is reached when all tuples in the `test_cases` list have been processed. The `results` list contains the count of pairs for each tuple in `test_cases`. The `freq` dictionary is reset for each tuple in `test_cases`, and the `count` variable is updated accordingly. The `a` variable takes on the value of the last element in the `arr` list for each tuple in `test_cases`. The `rx` and `ry` variables are calculated based on the last element in the `arr` list for each tuple in `test_cases`. The `current_pair` variable is a tuple containing the remainder of the last element in the `arr` list divided by `x` and `y`, respectively.
    return results
    #The program returns the list 'results' which contains the count of pairs for each tuple in 'test_cases'.

#Overall this is what the function does:This function takes a list of test cases as input, where each test case is a tuple containing four values: a positive integer n, two positive integers x and y, and a list of positive integers arr. It processes each test case by iterating over the list of integers, calculating the remainder of each integer divided by x and y, and counting the number of pairs that have the same remainder. The function returns a list of counts, where each count corresponds to the number of pairs found in each test case.

#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains four values: n, x, y, and arr. n is a positive integer, x and y are positive integers, and arr is a list of positive integers.
    input = sys.stdin.read
    data = input().splitlines()
    t = int(data[0])
    test_cases = []
    idx = 1
    for _ in range(t):
        n, x, y = map(int, data[idx].split())
        
        arr = list(map(int, data[idx + 1].split()))
        
        test_cases.append((n, x, y, arr))
        
        idx += 2
        
    #State: test_cases is a list of tuples, where each tuple contains four values: n, x, y, and arr. n is a positive integer, x and y are positive integers, and arr is a list of positive integers. t is an integer greater than or equal to 0, data is a list of strings, idx is 2*t + 1, _ is t - 1
    results = func_1(test_cases)
    for result in results:
        print(result)
        
    #State: `results` is returned and is equal to the return value of `func_1(test_cases)`, `test_cases` is a list of tuples, where each tuple contains four values: n, x, y, and arr. `t` is an integer greater than or equal to 0, `data` is a list of strings, `idx` is 2*t + 1, `_` is t - 1, `results` is a list of results that must have at least as many results as the length of `results`, and all results in the list are printed.

#Overall this is what the function does:The function accepts a list of test cases, where each test case is a tuple containing four values: a positive integer n, two positive integers x and y, and a list of positive integers arr. The function processes each test case and returns a list of results, where each result corresponds to a test case. The function does not modify the input test cases. The purpose of the function is to perform some operation on each test case and return the results. The final state of the program is that the results are printed to the console.

