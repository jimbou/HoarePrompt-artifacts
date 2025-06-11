#State of the program right berfore the function call: arr is a list of integers.
    if all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)) :
        return 'Yes'
        #The program returns the string 'Yes'
    #State: arr is a list of integers, and the list is not sorted in ascending order, meaning there exists at least one pair of adjacent elements where the first element is greater than the second element.
    return 'No' if any(arr[i] > arr[i + 1] for i in range(len(arr) - 1)) else 'Yes'
    #The program returns 'No' because the list 'arr' is not sorted in ascending order, meaning there exists at least one pair of adjacent elements where the first element is greater than the second element.

#Overall this is what the function does:Functionality: This function checks if a given list of integers is sorted in ascending order. It returns 'Yes' if the list is sorted, and 'No' if the list is not sorted, indicating that there exists at least one pair of adjacent elements where the first element is greater than the second element.

#State of the program right berfore the function call: data is a list of strings where each string represents an integer, index is a non-negative integer such that index < len(data), t is a positive integer, n is a positive integer such that n <= len(data) - index - 1, and arr is a list of integers of length n.
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
        
    #State: Output State: The final state after the loop executes all the iterations is: data remains the same list of strings, index is incremented by t + n * t (where n is the length of arr), t remains the same positive integer, results is a list of t elements where each element is the result of func_1(arr) for each iteration, and arr is the last list of integers of length n processed in the loop.
    print('\n'.join(results))
    #This is printed: The results of func_1(arr) for each iteration of the loop, where each result is separated by a newline character

#Overall this is what the function does:Reads input from standard input, processes it in iterations, and prints the results.

