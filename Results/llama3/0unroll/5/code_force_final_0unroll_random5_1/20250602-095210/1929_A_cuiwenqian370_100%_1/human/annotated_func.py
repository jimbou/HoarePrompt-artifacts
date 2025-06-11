#State of the program right berfore the function call: array is a list of integers of length n, where n is a positive integer greater than or equal to 2 and each integer is between 1 and 10^9 (inclusive).
    array.sort()
    beauty = 0
    for i in range(1, len(array)):
        beauty += abs(array[i] - array[i - 1])
        
    #State: Output State: array is a sorted list of integers of length n, where n is a positive integer greater than or equal to 2 and each integer is between 1 and 10^9 (inclusive), beauty is the sum of the absolute differences between consecutive elements in the array.
    return beauty
    #The program returns the sum of the absolute differences between consecutive elements in the sorted list of integers.

#Overall this is what the function does:This function calculates the sum of the absolute differences between consecutive elements in a sorted list of integers. It takes a list of integers as input, sorts the list in ascending order, and then computes the sum of the absolute differences between each pair of adjacent elements. The function returns this sum, which represents a measure of the "beauty" of the sorted list.

#State of the program right berfore the function call: array is a list of integers of length n, where n is a positive integer and 1 <= a_i <= 10^9 for all i.
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
        
    #State: The loop iterates t times, and in each iteration, it reads an integer n from the data list at the current index, increments the index by 1, reads n integers from the data list starting from the current index, increments the index by n, applies the function func_1 to the read integers, and appends the result to the results list. After the loop finishes, the index is incremented by t + n*t, and the results list contains t elements, each being the result of applying func_1 to the corresponding set of n integers from the data list. The array list is updated to the last set of n integers read from the data list. The stdin remains empty.
    for result in results:
        print(result)
        
    #State: Output State: The loop has executed t iterations, and the results list contains t elements, each being the result of applying func_1 to the corresponding set of n integers from the data list. The index has been incremented by t + n*t, and the array list has been updated to the last set of n integers read from the data list. The stdin remains empty.

#Overall this is what the function does:The function reads input from standard input, processes it in batches of n integers, applies the func_1 function to each batch, and prints the results. It iterates this process t times, where t and n are integers read from the input. The function does not modify the input data or have any side effects beyond printing the results.

