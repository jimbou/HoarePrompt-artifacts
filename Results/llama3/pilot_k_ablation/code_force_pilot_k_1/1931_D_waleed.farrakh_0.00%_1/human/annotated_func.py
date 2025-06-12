#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains four elements: n, x, y, and arr. n is a positive integer, x and y are positive integers, and arr is a list of positive integers.
    results = []
    for (n, x, y, arr) in test_cases:
        count = 0
        
        mod_x = {}
        
        mod_y = {}
        
        for num in arr:
            rem_x = -num % x
            rem_y = num % y
            count += mod_x.get(rem_x, 0) and mod_y.get(rem_y, 0)
            mod_x[num % x] = mod_x.get(num % x, 0) + 1
            mod_y[num % y] = mod_y.get(num % y, 0) + 1
        
        results.append(count)
        
    #State: `test_cases` is a list of tuples, `results` is a list with the sum of the products of the counts of each remainder modulo `x` and modulo `y` for each tuple in `test_cases`.
    return results
    #The program returns a list with the sum of the products of the counts of each remainder modulo `x` and modulo `y` for each tuple in `test_cases`.

#Overall this is what the function does:Functionality: This function takes a list of test cases as input, where each test case is a tuple containing a positive integer n, two positive integers x and y, and a list of positive integers arr. It processes each test case by iterating through the list of integers, calculating the remainder of each integer modulo x and modulo y, and counting the number of pairs that have the same remainder modulo x and modulo y. The function returns a list of counts, where each count represents the sum of the products of the counts of each remainder modulo x and modulo y for each test case.

#State of the program right berfore the function call: test_cases is a list of tuples, each tuple contains four values: n, x, y and arr. n is a positive integer, x and y are positive integers, and arr is a list of positive integers.
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
        
    #State: test_cases is a list of tuples, each tuple contains four values: n, x, y and arr. n is a positive integer, x and y are positive integers, and arr is a list of positive integers, t is an integer and must be greater than or equal to 0, data is a list of strings, idx is an integer equal to 1 + 2 * t
    results = func_1(test_cases)
    for result in results:
        print(result)
        
    #State: test_cases is a list of tuples, each tuple contains four values: n, x, y and arr. n is a positive integer, x and y are positive integers, and arr is a list of positive integers, t is an integer and must be greater than or equal to 0, data is a list of strings, idx is an integer equal to 1 + 2 * t, results is returned by func_1(test_cases) and must be empty, all elements of the results list which is returned by func_1(test_cases) have been printed

#Overall this is what the function does:The function accepts a list of test cases, where each test case is a tuple containing four values: a positive integer n, two positive integers x and y, and a list of positive integers arr. The function processes these test cases and returns a list of results. The function then prints each result from the returned list. The function does not modify the input test cases or any other external state. Its sole purpose is to process the input test cases and produce output based on the results.

