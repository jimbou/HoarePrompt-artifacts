#State of the program right berfore the function call: arr is a list of integers.
    if all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)) :
        return 'Yes'
        #The program returns the string 'Yes'. The list 'arr' remains unchanged and is still sorted in ascending order, with each element being less than or equal to the next element in the list.
    #State: arr is a list of integers. The list is not sorted in ascending order, meaning there exists at least one pair of adjacent elements where the first element is greater than the second element.
    return 'No' if any(arr[i] > arr[i + 1] for i in range(len(arr) - 1)) else 'Yes'
    #The program returns 'No' because the list 'arr' is not sorted in ascending order, meaning there exists at least one pair of adjacent elements where the first element is greater than the second element.

#Overall this is what the function does:This function checks if a given list of integers is sorted in ascending order. It returns 'Yes' if the list is sorted, meaning each element is less than or equal to the next element, and 'No' otherwise, indicating the presence of at least one pair of adjacent elements where the first is greater than the second. The function does not modify the input list.

#State of the program right berfore the function call: data is a list of strings where the first element is a positive integer t, followed by a sequence of test cases. Each test case starts with a positive integer n, followed by n positive integers. The list is 1-indexed and the index is a non-negative integer.
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
        
    #State: data is a list of strings where the first element is a positive integer t, followed by a sequence of test cases. Each test case starts with a positive integer n, followed by n positive integers. The list is 1-indexed and the index is 1 + n + 1 + n + ... + n, t is a positive integer equal to the first element of data and greater than or equal to 0, results is a list containing the result of func_1(arr) for each test case, _ is t-1, n is a positive integer equal to the second element of data, arr is a list of n positive integers, result is the result of func_1(arr), index is 1 + n + 1 + n + ... + n
    print('\n'.join(results))
    #This is printed: the results of func_1(arr) for each test case, separated by newline characters, where each result is the output of func_1(arr) for the corresponding test case

#Overall this is what the function does:The function reads input from standard input, processes it into a list of test cases, and then applies the func_1 function to each test case. It then prints the results of func_1 for each test case, separated by newline characters.

