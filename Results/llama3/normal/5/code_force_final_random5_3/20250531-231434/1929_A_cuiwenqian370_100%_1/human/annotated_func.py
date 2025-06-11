#State of the program right berfore the function call: array is a list of integers.
    array.sort()
    beauty = 0
    for i in range(1, len(array)):
        beauty += abs(array[i] - array[i - 1])
        
    #State: array is a sorted list of integers, i is len(array) - 1, beauty is the sum of the absolute differences between consecutive elements in array
    return beauty
    #The program returns the sum of the absolute differences between consecutive elements in the sorted list of integers 'array'.

#Overall this is what the function does:This function calculates and returns the sum of the absolute differences between consecutive elements in a sorted list of integers. It sorts the input list in ascending order and then computes the sum of the absolute differences between adjacent elements. The function does not modify the original list, but rather returns the calculated sum.

#State of the program right berfore the function call: array is a list of non-negative integers
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index])
        
        index += 1
        
        array = list(map(int, data[index:index + n]))
        
        index += n
        
        result = func_1(array)
        
        results.append(result)
        
    #State: array is a list of n non-negative integers, t is 0, index is 1 plus the sum of all n values, results is a list containing t elements which are the results of func_1(array) applied to all values of array, stdin is empty
    for result in results:
        print(result)
        
    #State: `array` is a list of n non-negative integers, `t` must be greater than 0, `index` is 1 plus the sum of all n values, `results` is a list containing t elements which are the results of func_1(array) applied to all values of array, `result` is the last element of results, `stdin` is empty, and the last element of results which is the result of func_1(array) applied to the last value of array is being printed.

#Overall this is what the function does:The function reads input from standard input, processes it into a list of non-negative integers, applies the func_1 function to each list, and prints the results. The function does not modify the input list or the func_1 function, and it does not perform any other actions beyond reading input, processing it, and printing the results.

