#State of the program right berfore the function call: a is a list of n positive integers, where n is a positive integer greater than or equal to 2 and less than or equal to 50.
    n = len(a)
    sorted_a = sorted(a)
    concatenated_a = a + a
    for i in range(n):
        if concatenated_a[i:i + len(sorted_a)] == sorted_a:
            return 'Yes'
        
    #State: The program returns 'Yes' if the sublist of `concatenated_a` from index `i` to `i + len(sorted_a)` is equal to `sorted_a` for any `i` in the range of `n`, otherwise it returns None.
    return 'No'
    #The program returns 'No'.

#Overall this is what the function does:This function checks if a sorted version of a given list of positive integers is present as a contiguous sublist in the concatenation of the original list with itself. It returns 'Yes' if such a sublist is found, and 'No' otherwise.

#State of the program right berfore the function call: data is a list of strings where the first element is a positive integer t, followed by a sequence of test cases. Each test case consists of a positive integer n followed by n positive integers. The integers are separated by spaces.
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
        
    #State: data is a list of strings where the first element is a positive integer t, followed by a sequence of test cases. Each test case consists of a positive integer n followed by n positive integers. The integers are separated by spaces, idx is t + t*n + t, t is 0, results is a list containing the results of func_1(a) for t test cases, where a is a list of n positive integers, _ is t-1
    print('\n'.join(results))
    #This is printed: (empty string)

#Overall this is what the function does:This function reads input from standard input, processes it into a list of test cases, applies the func_1 function to each test case, and prints the results. The input is expected to be a list of strings where the first element is a positive integer t, followed by a sequence of test cases. Each test case consists of a positive integer n followed by n positive integers. The function returns no value but prints the results of func_1(a) for each test case, where a is a list of n positive integers.

