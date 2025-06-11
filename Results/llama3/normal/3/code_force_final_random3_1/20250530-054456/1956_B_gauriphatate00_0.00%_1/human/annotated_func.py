#State of the program right berfore the function call: n is a positive integer, a is a list of integers such that 1 <= a_i <= n for all i, and each integer from 1 through n appears in the sequence a at most 2 times.
    counter = Counter(a)
    pairs = sum(1 for count in counter.values() if count == 2)
    return min(pairs, n // 2)
    #The program returns the minimum value between the number of integers that appear exactly twice in list 'a' and half of the positive integer 'n'.

#Overall this is what the function does:This function calculates and returns the minimum value between the number of integers that appear exactly twice in the input list 'a' and half of the input positive integer 'n'. It accepts two parameters: a list of integers 'a' and a positive integer 'n', and returns an integer value representing the calculated minimum. The function does not modify the input list 'a' or the integer 'n'.

#State of the program right berfore the function call: n is a positive integer and a is a list of integers such that 1 <= a_i <= n for all i and each integer from 1 through n appears in the sequence a at most 2 times.
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
        
    #State: n is a positive integer equal to the value at data[idx], idx is equal to its original value plus the sum of all n values plus t, a is a list of n integers from data[idx:idx + n], results is a list containing the result of func_1(n, a) for each iteration, data remains unchanged, t is 0, _ is t-1, stdin is empty
    for result in results:
        print(result)
        
    #State: n is a positive integer equal to the value at data[idx], idx is equal to its original value plus the sum of all n values plus t, a is a list of n integers from data[idx:idx + n], results is a list containing all results of func_1(n, a), result is the last result in the results list, data remains unchanged, t is 0, _ is t-1, stdin is empty, and the last result of func_1(n, a) is being printed.

#Overall this is what the function does:The function reads input from standard input, processes it, and prints the results. It reads a sequence of positive integers and lists of integers, where each list represents a sequence of integers from 1 to n, with each integer appearing at most twice. The function then calls another function, func_1, with each list and its corresponding n, and stores the results in a list. Finally, it prints each result in the list. The function does not modify the input data and leaves the standard input empty after processing.

