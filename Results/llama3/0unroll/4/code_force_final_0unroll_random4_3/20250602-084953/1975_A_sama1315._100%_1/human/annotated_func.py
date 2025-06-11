#State of the program right berfore the function call: a is a list of positive integers
    n = len(a)
    sorted_a = sorted(a)
    concatenated_a = a + a
    for i in range(n):
        if concatenated_a[i:i + len(sorted_a)] == sorted_a:
            return 'Yes'
        
    #State: Output State: The loop will return 'Yes' if any sub-list of 'concatenated_a' of length 'n' is equal to 'sorted_a', otherwise, it will return None. The value of 'a' remains unchanged, 'n' remains the same, 'sorted_a' remains sorted, and 'concatenated_a' remains twice as long as 'a'.
    return 'No'
    #The program returns 'No'

#Overall this is what the function does:This function checks if any sub-list of a concatenated version of the input list 'a' (duplicated once) is equal to the sorted version of 'a'. If such a sub-list is found, it returns 'Yes'. If no such sub-list is found after checking all possible sub-lists, it returns 'No'. The input list 'a' remains unchanged throughout the function's execution.

#State of the program right berfore the function call: data is a list of strings where each string represents an integer, idx is a non-negative integer such that idx < len(data), t is a positive integer, n is a positive integer such that n < len(data) - idx.
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
        
    #State: Output State: The loop has executed t iterations, and the results list now contains t elements, each of which is the result of calling func_1 on a slice of the data list. The idx variable has been incremented by t times the value of n (which is the length of the slice of data passed to func_1), plus t (the number of iterations). The data list and the variable n remain unchanged.
    print('\n'.join(results))
    #This is printed: the results of calling func_1 on t slices of the data list, each of length n, separated by newline characters

#Overall this is what the function does:Reads input from standard input, extracts a list of integers, and then iterates over the list to extract slices of integers. For each slice, it calls a function `func_1` and appends the result to a list of results. Finally, it prints the results, separated by newline characters.

