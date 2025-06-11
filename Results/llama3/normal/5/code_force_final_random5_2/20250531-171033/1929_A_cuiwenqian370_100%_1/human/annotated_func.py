#State of the program right berfore the function call: array is a list of integers of length n, where n is a positive integer greater than or equal to 2, and all elements in the array are non-negative integers less than or equal to 10^9.
    array.sort()
    beauty = 0
    for i in range(1, len(array)):
        beauty += abs(array[i] - array[i - 1])
        
    #State: `array` is a sorted list of integers of length n, `i` is n-1, `beauty` is the sum of the absolute differences between consecutive elements of `array`
    return beauty
    #The program returns the sum of the absolute differences between consecutive elements of a sorted list of integers of length n.

#Overall this is what the function does:This function calculates and returns the sum of the absolute differences between consecutive elements in a sorted list of non-negative integers. It takes a list of integers as input, sorts it in ascending order, and then computes the sum of the absolute differences between adjacent elements. The function returns this sum as its output, effectively measuring the total "beauty" or variation in the sorted list.

#State of the program right berfore the function call: array is a list of integers
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
        
    #State: array is a list of integers, t is 0, index is 1 plus t*n, results is a list containing the result of func_1(array) t times, stdin is empty
    for result in results:
        print(result)
        
    #State: array is a list of integers, t is at least 1, index is 1 plus t*n, results is a list containing the result of func_1(array) t times, stdin is empty, and the result is printed t times.

#Overall this is what the function does:Reads input from standard input, processes it into a list of integers, applies the func_1 function to each list, stores the results, and prints each result.

