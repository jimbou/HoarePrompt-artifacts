#State of the program right berfore the function call: a is a list of n positive integers where n is a positive integer greater than or equal to 2 and less than or equal to 50.
    n = len(a)
    sorted_a = sorted(a)
    concatenated_a = a + a
    for i in range(n):
        if concatenated_a[i:i + len(sorted_a)] == sorted_a:
            return 'Yes'
        
    #State: `a` is a list of n positive integers, `n` is the number of elements in list a, `sorted_a` is a sorted list of the elements in a, `concatenated_a` is a list containing all elements in a twice, `i` is n. If any sublist of `concatenated_a` of length n is equal to `sorted_a`, the program returns the string 'Yes'. Otherwise, the program returns None.
    return 'No'
    #The program returns the string 'No'.

#Overall this is what the function does:This function checks if a sorted version of the input list can be found as a contiguous sublist within the list concatenated with itself. It returns 'Yes' if such a sublist exists, and 'No' otherwise. The function accepts a list of positive integers as input and returns a string indicating the presence or absence of the sorted sublist.

#State of the program right berfore the function call: data is a list of strings where each string represents either an integer or a space-separated list of integers, and idx is a non-negative integer such that idx < len(data).
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
        
    #State: data is an empty list, idx is 1 + t*n + t, t is 0, results is a list containing the result of func_1(a) for each iteration of the loop, stdin is empty, _ is t-1
    print('\n'.join(results))
    #This is printed: the results of func_1(a) for each iteration of the loop, separated by newline characters

#Overall this is what the function does:Reads input from standard input, parses it into a list of integers and space-separated lists of integers, applies the func_1 function to each list of integers, and prints the results separated by newline characters.

