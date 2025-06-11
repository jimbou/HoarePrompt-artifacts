#State of the program right berfore the function call: a is a list of positive integers.
    n = len(a)
    sorted_a = sorted(a)
    concatenated_a = a + a
    for i in range(n):
        if concatenated_a[i:i + len(sorted_a)] == sorted_a:
            return 'Yes'
        
    #State: `a` is a list of positive integers, `n` is the number of elements in `a`, `sorted_a` is a sorted list of positive integers containing the same elements as `a`, `concatenated_a` is a list of positive integers containing two copies of the elements in `a`, `i` is equal to `n`. If the sublist of `concatenated_a` from index `i - len(sorted_a)` to `i` is equal to `sorted_a`, the program returns the string 'Yes'. Otherwise, the program returns None.
    return 'No'
    #The program returns string 'No'

#Overall this is what the function does:This function checks if a sorted version of a given list of positive integers can be found as a contiguous sublist within a concatenated version of the original list. It returns 'Yes' if such a sublist is found, and 'No' otherwise.

#State of the program right berfore the function call: data is a list of strings where the first element is a positive integer t, followed by t blocks of input data. Each block consists of a positive integer n followed by n positive integers. The input is read from stdin.
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
        
    #State: data is a list of strings where the first element is a positive integer t, followed by t blocks of input data, idx is t*(n+1)+1, results is a list containing t elements which are the result of func_1(a) for t different values of a, a is a list of n positive integers, t is 0, stdin is empty, _ is t-1, n is a positive integer, result is the result of func_1(a)
    print('\n'.join(results))
    #This is printed: (empty string)

#Overall this is what the function does:Reads input from stdin, processes it into blocks of integers, applies the func_1 function to each block, and prints the results.

