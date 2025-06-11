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
        
    #State: Output State: The `results` list contains the total count of pairs of elements in each array that satisfy the given conditions, and the `test_cases` list remains unchanged.
    return results
    #The program returns the list 'results' which contains the total count of pairs of elements in each array that satisfy the given conditions, and the list 'test_cases' remains unchanged.

#Overall this is what the function does:This function takes a list of test cases as input, where each test case is a tuple containing a positive integer n, two positive integers x and y, and a list of positive integers arr. It processes each test case by iterating through the list of integers, calculating the remainder of each integer modulo x and y, and counting the number of pairs that satisfy a certain condition. The function returns a list of counts, where each count represents the total number of pairs in the corresponding test case that satisfy the condition. The original list of test cases remains unchanged.

#State of the program right berfore the function call: test_cases is a list of tuples, each tuple contains four elements: n, x, y and arr. n is a positive integer, x and y are positive integers, and arr is a list of positive integers.
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
        
    #State: Output State: test_cases is a list of tuples, each tuple contains four elements: n, x, y and arr. n is a positive integer, x and y are positive integers, and arr is a list of positive integers, t is 0, data is a list of strings, idx is an integer greater than or equal to 2*t.
    results = func_1(test_cases)
    for result in results:
        print(result)
        
    #State: Output State: The variable `result` has been iterated over the list `results` and printed each element in `results`. The other variables in the initial state remain unchanged.

#Overall this is what the function does:This function takes a list of test cases as input, where each test case is a tuple containing four elements: a positive integer n, two positive integers x and y, and a list of positive integers arr. The function processes each test case and returns a list of results. The results are then printed to the console. The function does not modify the input variables or have any side effects beyond printing the results.

