#State of the program right berfore the function call: array is a list of integers, all integers in the list are greater or equal to 1 and less or equal to 10^9.
    array.sort()
    beauty = 0
    for i in range(1, len(array)):
        beauty += abs(array[i] - array[i - 1])
        
    #State: Output State: array is a sorted list of integers, all integers in the list are greater or equal to 1 and less or equal to 10^9, beauty is the sum of the absolute differences between consecutive elements in the array.
    return beauty
    #The program returns the sum of the absolute differences between consecutive elements in the array, where the array is a sorted list of integers, all integers in the list are greater or equal to 1 and less or equal to 10^9.

#Overall this is what the function does:This function calculates and returns the sum of the absolute differences between consecutive elements in a sorted list of integers, where all integers are between 1 and 10^9 (inclusive). The input list is sorted in ascending order, and the function returns the total beauty value, which is the sum of these absolute differences.

#State of the program right berfore the function call: array is a list of non-negative integers.
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
        
    #State: Output State: The loop has executed t times, and the results list now contains t elements, each of which is the result of applying func_1 to a sublist of n integers from the data list, where n is the value at index in the data list. The index variable has been incremented by t + sum of all n values. The array variable now holds the last sublist of n integers from the data list. The stdin remains empty.
    for result in results:
        print(result)
        
    #State: Output State: The loop has executed t times, and the results list now contains t elements, each of which is the result of applying func_1 to a sublist of n integers from the data list, where n is the value at index in the data list. The index variable has been incremented by t + sum of all n values. The array variable now holds the last sublist of n integers from the data list. The stdin remains empty.

#Overall this is what the function does:The function reads input from standard input, processes it in batches, applies the func_1 function to each batch, and prints the results. The input is expected to be a list of non-negative integers, where the first integer specifies the number of batches, and each batch is preceded by its size. The function consumes all input from standard input, leaving it empty. The output is a list of results, one for each batch, which are printed to the console.

