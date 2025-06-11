#State of the program right berfore the function call: arr is a list of integers
    if all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)) :
        return 'Yes'
        #The program returns the string 'Yes'
    #State: *arr is a list of integers. The list is not sorted in ascending order
    return 'No' if any(arr[i] > arr[i + 1] for i in range(len(arr) - 1)) else 'Yes'
    #The program returns 'No' if the list 'arr' is not sorted in ascending order, otherwise it returns 'Yes'

#Overall this is what the function does:Determines if a list of integers is sorted in ascending order and returns 'Yes' if it is, otherwise returns 'No'.

#State of the program right berfore the function call: data is a list of strings where each string is either a positive integer or a space-separated list of positive integers. The first element of data is a positive integer t, and the rest of the elements are alternating pairs of a positive integer n and a list of n positive integers.
    input = sys.stdin.read
    data = input().split()
    index = 0
    t = int(data[index])
    index += 1
    results = []
    for _ in range(t):
        n = int(data[index])
        
        index += 1
        
        arr = list(map(int, data[index:index + n]))
        
        index += n
        
        result = func_1(arr)
        
        results.append(result)
        
    #State: data is a list of strings where each string is either a positive integer or a space-separated list of positive integers, index is n + 2 + ... + 2n, t is 0, results is a list containing the result of func_1(arr) where arr is a list of n positive integers, and the result of func_1(arr) where arr is a list of n positive integers, and ... and the result of func_1(arr) where arr is a list of n positive integers.
    print('\n'.join(results))
    #This is printed: a string containing the results of func_1(arr) where arr is a list of n positive integers, separated by newline characters, repeated n + 2 + ... + 2n times

#Overall this is what the function does:Reads input data from standard input, processes it in batches, and prints the results. The input data consists of a series of alternating pairs of a positive integer n and a list of n positive integers. For each pair, the function applies the func_1 function to the list of integers and appends the result to a list of results. Finally, it prints the results, one per line, with each result repeated a number of times equal to the sum of the batch sizes.

