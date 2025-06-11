#State of the program right berfore the function call: array is a list of integers, all integers are greater or equal to 1 and less or equal to 10^9.
    array.sort()
    beauty = 0
    for i in range(1, len(array)):
        beauty += abs(array[i] - array[i - 1])
        
    #State: `array` is a sorted list of integers, all integers are greater or equal to 1 and less or equal to 10^9, `beauty` is equal to the sum of absolute differences between consecutive elements in `array`, `i` is equal to `len(array) - 1`, `len(array)` is greater than or equal to 1.
    return beauty
    #The program returns the sum of absolute differences between consecutive elements in the sorted list 'array' of integers, where all integers are greater or equal to 1 and less or equal to 10^9.

#Overall this is what the function does:This function calculates and returns the sum of absolute differences between consecutive elements in a sorted list of integers. The input list is expected to contain integers between 1 and 10^9. The function sorts the list in ascending order, then iterates through the sorted list to calculate the sum of absolute differences between adjacent elements. The final result is the total sum of these absolute differences.

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
        
    #State: array is a list of n non-negative integers, t is 0, index is incremented by tn + t, results is a list containing t elements which are the results of func_1(array) for t different arrays, stdin is empty
    for result in results:
        print(result)
        
    #State: array is a list of n non-negative integers, t is 0, index is incremented by tn + t, results is an empty list, stdin is empty, and all elements in the list results have been printed.

#Overall this is what the function does:The function reads input from standard input, processes it, and prints the results. It takes no arguments and returns no value. The input is expected to be in a specific format, where the first line contains an integer t, followed by t lines, each containing an integer n and n non-negative integers. The function processes each line of input, applies the func_1 function to the list of integers, and appends the result to a list. After processing all input, it prints each result in the list. The function modifies the state of the program by emptying the standard input buffer and printing the results to the console.

