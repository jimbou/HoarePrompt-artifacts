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
        
    #State: `test_cases` is a list of tuples, `results` is a list of integers where each integer is the sum of the products of the values of `mod_x` and `mod_y` for each element in `arr` for each test case, `n`, `x`, `y` are the elements of the last test case, `arr` is an empty list, `count` is the sum of the products of the values of `mod_x` and `mod_y` for each element in `arr` for the last test case, `mod_x` is a dictionary where the keys are the remainders of the elements of `arr` when divided by `x` and the values are the counts of each remainder for the last test case, `mod_y` is a dictionary where the keys are the remainders of the elements of `arr` when divided by `y` and the values are the counts of each remainder for the last test case. If `test_cases` is an empty list, `results` is an empty list.
    return results
    #The program returns a list of integers where each integer is the sum of the products of the values of `mod_x` and `mod_y` for each element in `arr` for each test case. If `test_cases` is an empty list, the program returns an empty list.

#Overall this is what the function does:This function processes a list of test cases, where each test case contains a positive integer n, two positive integers x and y, and a list of positive integers arr. For each test case, it calculates the sum of the products of the counts of remainders when the elements of arr are divided by x and y. The function returns a list of these sums, one for each test case. If the input list of test cases is empty, the function returns an empty list.

#State of the program right berfore the function call: test_cases is a list of tuples, each tuple contains four elements: n, x, y, and arr. n is a positive integer, x and y are positive integers, and arr is a list of positive integers.
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
        
    #State: test_cases is a list of t tuples, each tuple contains four elements: n, x, y, and arr. n is a positive integer, x and y are positive integers, and arr is a list of positive integers. t is a non-negative integer, data is a list of strings, idx is 2*t + 1, input is a function that reads from sys.stdin.
    results = func_1(test_cases)
    for result in results:
        print(result)
        
    #State: `results` is a list of values returned by `func_1` for each tuple in `test_cases`, `test_cases` is a list of t tuples, each tuple contains four elements: n, x, y, and arr. n is a positive integer, x and y are positive integers, and arr is a list of positive integers. t is a non-negative integer, data is a list of strings, idx is 2*t + 1, input is a function that reads from sys.stdin, and all results have been printed. If `results` is empty, no results have been printed.

#Overall this is what the function does:The function accepts a list of test cases, where each test case is a tuple containing four elements: a positive integer n, two positive integers x and y, and a list of positive integers arr. It processes each test case and returns a list of results. The function prints each result in the list, or does not print anything if the list is empty.

