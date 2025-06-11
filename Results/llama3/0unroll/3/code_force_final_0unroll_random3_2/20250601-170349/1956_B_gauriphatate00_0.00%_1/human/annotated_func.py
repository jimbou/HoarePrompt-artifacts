#State of the program right berfore the function call: n is a positive integer, a is a list of integers such that 1 <= a_i <= n for all i, and each integer from 1 through n appears in the sequence a at most 2 times.
    counter = Counter(a)
    pairs = sum(1 for count in counter.values() if count == 2)
    return min(pairs, n // 2)
    #The program returns the minimum value between the number of elements in list 'a' that appear exactly twice and half of the positive integer 'n'.

#Overall this is what the function does:This function determines the minimum value between the number of elements in list 'a' that appear exactly twice and half of the positive integer 'n'. It accepts a list of integers 'a' and a positive integer 'n' as input, and returns an integer representing the minimum value between these two counts. The function does not modify the input list 'a' or the integer 'n'.

#State of the program right berfore the function call: n is a positive integer and a is a list of n integers, each between 1 and n (inclusive), with each integer appearing at most twice in the list.
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        
        idx += 1
        
        a = list(map(int, data[idx:idx + n]))
        
        idx += n
        
        results.append(func_1(n, a))
        
    #State: Output State: idx is t * (n + 1) + 1, results is a list of t elements, each of which is the result of func_1(n, a) for the corresponding iteration, n is the value of n in the last iteration, a is the value of a in the last iteration, t is 0, data is the same as the initial state, stdin is the same as the initial state.
    for result in results:
        print(result)
        
    #State: Output State: idx is t * (n + 1) + 1, results is a list of t elements, each of which is the result of func_1(n, a) for the corresponding iteration, n is the value of n in the last iteration, a is the value of a in the last iteration, t is the number of iterations, data is the same as the initial state, stdin is the same as the initial state.

#Overall this is what the function does:This function reads input from standard input, processes it, and prints the results. It expects the input to be a series of test cases, where each test case consists of a positive integer n followed by a list of n integers between 1 and n (inclusive), with each integer appearing at most twice in the list. The function calls another function, func_1, for each test case and appends the result to a list. After processing all test cases, it prints each result in the list.

