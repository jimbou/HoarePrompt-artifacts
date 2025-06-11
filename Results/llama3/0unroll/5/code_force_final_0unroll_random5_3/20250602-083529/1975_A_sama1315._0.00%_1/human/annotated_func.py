#State of the program right berfore the function call: arr is a list of integers.
    if all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)) :
        return 'Yes'
        #The program returns the string 'Yes'. The list 'arr' remains unchanged, still containing integers in ascending order.
    #State: arr is a list of integers. The list is not sorted in ascending order, meaning there exists at least one pair of adjacent elements where the first element is greater than the second element.
    return 'No' if any(arr[i] > arr[i + 1] for i in range(len(arr) - 1)) else 'Yes'
    #The program returns 'No' because there exists at least one pair of adjacent elements in the list 'arr' where the first element is greater than the second element.

#Overall this is what the function does:This function checks if a given list of integers is sorted in ascending order and returns 'Yes' if it is, or 'No' if it's not. The function does not modify the original list.

#State of the program right berfore the function call: data is a list of strings where the first element is a positive integer t, and the rest of the elements are alternating positive integers n and lists of n positive integers.
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
        
    #State: Output State: data is a list of strings where the first element is a positive integer t, and the rest of the elements are alternating positive integers n and lists of n positive integers, index is t * 2 + 1, t is a positive integer, results is a list of t elements where each element is the result of func_1(arr) for each iteration of the loop.
    print('\n'.join(results))
    #This is printed: the results of func_1(arr) for each iteration of the loop, separated by newline characters (where arr is a list of n positive integers and n is a positive integer)

#Overall this is what the function does:This function reads input from standard input, processes it, and prints the results. It expects the input to be a list of strings where the first element is a positive integer t, and the rest of the elements are alternating positive integers n and lists of n positive integers. The function then iterates t times, each time processing a list of n positive integers using the func_1 function and storing the result. Finally, it prints the results of all iterations, separated by newline characters.

