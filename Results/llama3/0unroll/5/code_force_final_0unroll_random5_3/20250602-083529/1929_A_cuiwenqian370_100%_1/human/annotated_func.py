#State of the program right berfore the function call: array is a list of integers, all integers in the list are greater than or equal to 1 and less than or equal to 10^9.
    array.sort()
    beauty = 0
    for i in range(1, len(array)):
        beauty += abs(array[i] - array[i - 1])
        
    #State: Output State: The array remains unchanged, beauty is the sum of the absolute differences between consecutive elements in the array.
    return beauty
    #The program returns the sum of the absolute differences between consecutive elements in the array.

#Overall this is what the function does:This function calculates and returns the sum of the absolute differences between consecutive elements in a given list of integers, without modifying the original list.

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
        
    #State: Output State: The loop will execute 't' times, and after each execution, the 'index' will be incremented by 'n+1' where 'n' is the number of elements in the array. The 'results' list will be populated with the results of 'func_1' applied to each array. The 'array' will be overwritten in each iteration with a new list of 'n' integers. The 'stdin' will remain empty as it is not used in the loop.
    for result in results:
        print(result)
        
    #State: Output State: The loop will execute 't' times, and after each execution, the 'index' will be incremented by 'n+1' where 'n' is the number of elements in the array. The 'results' list will be populated with the results of 'func_1' applied to each array. The 'array' will be overwritten in each iteration with a new list of 'n' integers. The 'stdin' will remain empty as it is not used in the loop.

#Overall this is what the function does:The function reads input from standard input, processes it, and prints the results. It expects the input to be in a specific format, where the first line contains the number of test cases 't', followed by 't' lines, each containing the size of an array 'n' and 'n' non-negative integers. The function applies another function 'func_1' to each array and stores the results in a list. Finally, it prints each result on a new line.

