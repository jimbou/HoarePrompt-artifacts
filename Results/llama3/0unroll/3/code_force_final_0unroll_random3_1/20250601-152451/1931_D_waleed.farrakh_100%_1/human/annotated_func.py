#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains four elements: n, x, y, and arr. n is a positive integer, x and y are positive integers, and arr is a list of positive integers.
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
        
    #State: Output State: The `results` list contains the count of pairs of elements in each array that satisfy the given conditions. The `test_cases` list remains unchanged.
    return results
    #The program returns the list 'results' which contains the count of pairs of elements in each array that satisfy the given conditions. The list 'test_cases' remains unchanged.

#Overall this is what the function does:This function takes a list of test cases as input, where each test case is a tuple containing a positive integer n, two positive integers x and y, and a list of positive integers arr. It processes each test case by iterating over the list of integers, calculating the remainder of each integer modulo x and y, and counting the number of pairs that satisfy the given conditions. The function returns a list of counts, where each count represents the number of pairs in the corresponding test case that satisfy the conditions. The input list of test cases remains unchanged.

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
        
    #State: Output State: The variable t will be 0, the variable idx will be 2*t + 1 = 2*initial value of t + 1, the variable test_cases will be a list of tuples, where each tuple contains four elements: n, x, y, and arr. n is a positive integer, x and y are positive integers, and arr is a list of positive integers. The variable data will be the same as the initial state.
    results = func_1(test_cases)
    for result in results:
        print(result)
        
    #State: Output State: The variable t is 0, the variable idx is 2*t + 1 = 1, the variable test_cases is a list of tuples, where each tuple contains four elements: n, x, y, and arr. n is a positive integer, x and y are positive integers, and arr is a list of positive integers. The variable data is the same as the initial state. The variable results is returned by the function func_1 with test_cases as its argument.

#Overall this is what the function does:The function accepts a list of test cases as input, where each test case is a tuple containing four elements: a positive integer n, two positive integers x and y, and a list of positive integers arr. The function processes each test case and returns a list of results. The function does not modify the input test cases or any external state. The purpose of the function is to perform some computation on each test case and produce a corresponding output. The final state of the program after the function concludes is that the input test cases remain unchanged, and the function returns a list of results, one for each test case.

