#State of the program right berfore the function call: a is a list of n positive integers where n is a positive integer greater than or equal to 2 and less than or equal to 50.
    n = len(a)
    sorted_a = sorted(a)
    concatenated_a = a + a
    for i in range(n):
        if concatenated_a[i:i + len(sorted_a)] == sorted_a:
            return 'Yes'
        
    #State: Output State: The loop will return 'Yes' if a is already sorted, otherwise it will return None.
    return 'No'
    #The program returns 'No'

#Overall this is what the function does:This function checks if a given list of positive integers is already sorted by comparing it with its sorted version. It returns 'Yes' if the list is sorted, 'No' if it's not, and 'None' if the list is empty or contains only one element.

#State of the program right berfore the function call: data is a list of strings where the first element is a positive integer t, followed by t pairs of positive integers n and n space-separated positive integers.
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        
        idx += 1
        
        a = list(map(int, data[idx:idx + n]))
        
        idx += n
        
        result = func_1(a)
        
        results.append(result)
        
    #State: Output State: The loop has executed all iterations, and the output state is as follows: data is unchanged, idx is t * (n + 1) + 1, t is unchanged, and results is a list of t elements, where each element is the result of func_1 applied to the corresponding list of n space-separated positive integers.
    print('\n'.join(results))
    #This is printed: the results of applying func_1 to each list of n space-separated positive integers

#Overall this is what the function does:The function reads input from standard input, processes it into a list of integers, applies the func_1 function to each list of integers, and prints the results. It does not modify the original input data. The function takes no arguments and returns no value, instead printing the results directly.

