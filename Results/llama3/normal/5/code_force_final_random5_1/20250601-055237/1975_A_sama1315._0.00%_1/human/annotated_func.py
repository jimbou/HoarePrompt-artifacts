#State of the program right berfore the function call: arr is a list of integers.
    if all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)) :
        return 'Yes'
        #The program returns the string 'Yes'.
    #State: arr is a list of integers, and the list is not sorted in ascending order, meaning there exists at least one pair of adjacent elements where the first element is greater than the second element.
    return 'No' if any(arr[i] > arr[i + 1] for i in range(len(arr) - 1)) else 'Yes'
    #The program returns 'No' because the list 'arr' is not sorted in ascending order, meaning there exists at least one pair of adjacent elements where the first element is greater than the second element.

#Overall this is what the function does:This function checks if a given list of integers is sorted in ascending order. It returns 'Yes' if the list is sorted, and 'No' if it's not, specifically when there exists at least one pair of adjacent elements where the first element is greater than the second element.

#State of the program right berfore the function call: data is a list of strings where each string represents an integer, index is a non-negative integer such that index < len(data), t is a positive integer, n is a positive integer, and arr is a list of integers.
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
        
    #State: data is a list of strings where each string represents an integer, index is 1 plus t times n, t is a positive integer equal to the integer value of the first string in data, results is a list containing the result of func_1(arr) for each iteration, arr is a list of n integers, n is the integer value of the string at index 1 in data, and _ is t-1
    print('\n'.join(results))
    #This is printed: A series of lines, where each line contains the result of func_1(arr) for a particular iteration, separated by newline characters

#Overall this is what the function does:This function reads input from standard input, processes it, and prints the results. It expects the input to be a list of strings representing integers, where the first string is the number of test cases (t), followed by t sets of data. Each set of data starts with the number of elements (n) in the set, followed by n integers. The function applies another function (func_1) to each set of data and appends the result to a list of results. Finally, it prints each result in the list on a separate line, separated by newline characters.

