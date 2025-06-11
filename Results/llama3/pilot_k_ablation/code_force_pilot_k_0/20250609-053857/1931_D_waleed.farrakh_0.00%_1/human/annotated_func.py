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
        
    #State: Output State: The `results` list contains the count of pairs of numbers in each test case that satisfy the condition `num1 % x == -num2 % x` and `num1 % y == num2 % y`, where `num1` and `num2` are numbers in the `arr` list. The `test_cases` list remains unchanged.
    return results
    #The program returns the list 'results' which contains the count of pairs of numbers in each test case that satisfy the condition `num1 % x == -num2 % x` and `num1 % y == num2 % y`, where `num1` and `num2` are numbers in the `arr` list.

#Overall this is what the function does:This function takes a list of test cases as input, where each test case is a tuple containing a positive integer n, two positive integers x and y, and a list of positive integers arr. It processes each test case by iterating through the list of integers and counting the number of pairs that satisfy two conditions: `num1 % x == -num2 % x` and `num1 % y == num2 % y`. The function returns a list of counts, where each count corresponds to the number of pairs satisfying the conditions in each test case. The input list of test cases remains unchanged.

#State of the program right berfore the function call: test_cases is a list of tuples, each tuple contains four values: n, x, y, and arr. n is a positive integer, x and y are positive integers, and arr is a list of positive integers.
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
        
    #State: Output State: test_cases is a list of tuples, each tuple contains four values: n, x, y, and arr. n is a positive integer, x and y are positive integers, and arr is a list of positive integers, t is an integer equal to the first line of stdin, data is a list of strings split from stdin, idx is 2 * t + 1.
    results = func_1(test_cases)
    for result in results:
        print(result)
        
    #State: Output State: The loop has executed all iterations, printing each result in the `results` list. The `results` list remains unchanged, still containing the values returned by `func_1(test_cases)`. The `test_cases` list, `t` integer, `data` list, and `idx` integer remain unchanged as they were not affected by the loop.

#Overall this is what the function does:The function accepts a list of test cases, where each test case is a tuple containing four values: a positive integer n, two positive integers x and y, and a list of positive integers arr. The function processes these test cases and returns a list of results. The function does not modify the input test cases or any other external state. The purpose of the function is to compute and return a list of results based on the input test cases.

