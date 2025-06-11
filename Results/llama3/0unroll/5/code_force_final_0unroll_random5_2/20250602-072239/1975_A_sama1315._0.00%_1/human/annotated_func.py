#State of the program right berfore the function call: arr is a list of integers
    if all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)) :
        return 'Yes'
        #The program returns the string 'Yes'.
    #State: arr is a list of integers. The list is not sorted in ascending order, meaning there exists at least one pair of adjacent elements where the first element is greater than the second element.
    return 'No' if any(arr[i] > arr[i + 1] for i in range(len(arr) - 1)) else 'Yes'
    #The program returns 'No'

#Overall this is what the function does:This function checks if a given list of integers is sorted in ascending order. It returns 'Yes' if the list is sorted and 'No' otherwise. The function does not modify the input list. It only performs a check and returns a string indicating whether the list is sorted or not.

#State of the program right berfore the function call: data is a list of strings where each string represents an integer, index is a non-negative integer, t is a non-negative integer, n is a non-negative integer, and arr is a list of integers.
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
        
    #State: Output State: The loop has executed t times, and the results list now contains t results. The index has moved t * (n + 1) positions forward in the data list. The arr list has been updated t times with different slices of the data list. The value of n has been updated t times with different values from the data list. The value of result has been updated t times with the result of func_1(arr) for each iteration.
    print('\n'.join(results))
    #This is printed: a multi-line string containing t results, each result being the output of func_1(arr) for a different slice of the data list, separated by newline characters

#Overall this is what the function does:This function reads input from standard input, processes it in batches, and prints the results. It takes no arguments and returns no value. The input is expected to be a list of strings where each string represents an integer, followed by a series of batches, each batch consisting of a non-negative integer (n) and a list of n integers. The function processes each batch by calling another function (func_1) with the list of integers as an argument, and appends the result to a list of results. After processing all batches, the function prints the list of results, one result per line.

