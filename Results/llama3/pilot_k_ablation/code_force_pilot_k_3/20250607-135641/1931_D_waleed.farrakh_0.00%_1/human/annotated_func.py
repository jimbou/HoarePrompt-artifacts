#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains four values: n, x, y, and arr. n is a positive integer, x and y are positive integers, and arr is a list of positive integers.
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
        
    #State: `test_cases` is an empty list, `n` is undefined, `x` is undefined, `y` is undefined, `arr` is undefined, `num` is undefined, `rem_x` is undefined, `rem_y` is undefined, `mod_x` is an empty dictionary, `mod_y` is an empty dictionary, `count` is undefined, and `results` is a list containing the counts of pairs of numbers in each tuple of `test_cases` that satisfy the given conditions.
    return results
    #The program returns a list containing the counts of pairs of numbers in each tuple of `test_cases` that satisfy the given conditions.

#Overall this is what the function does:This function accepts a list of test cases, where each test case is a tuple containing a positive integer n, two positive integers x and y, and a list of positive integers arr. It returns a list of counts, where each count represents the number of pairs of numbers in the corresponding test case that satisfy the condition: the remainder of the product of the two numbers when divided by x is non-zero and the remainder of the sum of the two numbers when divided by y is zero. The function iterates over each test case, processes the list of numbers, and appends the count of satisfying pairs to the results list. The function returns the list of counts, effectively providing the number of pairs in each test case that meet the specified conditions.

#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains four elements: n, x, y, and arr. n is a positive integer, x and y are positive integers, and arr is a list of positive integers.
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
        
    #State: t is greater than or equal to 0, data is a list of strings split from the lines of stdin, test_cases contains t tuples (n, x, y, arr), idx is 2t + 2, stdin is empty except for the first line that has been read, n, x, and y are integers, arr is a list of integers.
    results = func_1(test_cases)
    for result in results:
        print(result)
        
    #State: `t` is greater than or equal to 0, `data` is a list of strings split from the lines of stdin, `idx` is 2t + 2, `n`, `x`, and `y` are integers, `arr` is a list of integers, `results` is a list that has `t` elements and is returned by `func_1(test_cases)`, `test_cases` contains `t` tuples (n, x, y, arr), and all elements of the results list which is returned by `func_1(test_cases)` have been printed.

#Overall this is what the function does:The function accepts a list of test cases, where each test case is a tuple containing four elements: a positive integer n, two positive integers x and y, and a list of positive integers arr. It processes each test case and returns a list of results, one for each test case. The function then prints each result. The final state of the program is that all results have been printed, and the input variables remain unchanged.

