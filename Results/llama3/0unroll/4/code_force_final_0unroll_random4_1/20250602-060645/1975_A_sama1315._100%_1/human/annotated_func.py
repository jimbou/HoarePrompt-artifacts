#State of the program right berfore the function call: a is a list of positive integers.
    n = len(a)
    sorted_a = sorted(a)
    concatenated_a = a + a
    for i in range(n):
        if concatenated_a[i:i + len(sorted_a)] == sorted_a:
            return 'Yes'
        
    #State: Output State: The loop will return 'Yes' if a sub-list of concatenated_a is equal to sorted_a, otherwise, it will return None. The values of a, n, and sorted_a remain unchanged.
    return 'No'
    #The program returns 'No'

#Overall this is what the function does:This function checks if a sublist of the concatenated version of the input list 'a' is equal to the sorted version of 'a'. It returns 'Yes' if such a sublist exists, otherwise, it returns 'No'. The original list 'a' remains unchanged.

#State of the program right berfore the function call: data is a list of strings where the first element is a positive integer t, followed by t sets of input data. Each set of input data consists of a positive integer n followed by n positive integers.
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
        
        result = func_1(a)
        
        results.append(result)
        
    #State: data is a list of strings where the first element is a positive integer t, followed by t sets of input data. Each set of input data consists of a positive integer n followed by n positive integers, idx is t * (n + 1) + 1, t is a positive integer, results is a list of t elements where each element is the result of func_1(a) for each set of input data.
    print('\n'.join(results))
    #This is printed: [result of func_1(a) for each set of input data], where each result is on a new line, and there are t results in total

#Overall this is what the function does:This function reads input data from standard input, processes it, and prints the results. It expects the input data to be a list of strings where the first element is a positive integer t, followed by t sets of input data. Each set of input data consists of a positive integer n followed by n positive integers. The function then applies the func_1 function to each set of input data and stores the results in a list. Finally, it prints each result on a new line, with a total of t results.

