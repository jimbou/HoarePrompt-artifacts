#State of the program right berfore the function call: stdin contains three inputs: first two integers n and t (n >= 2, t = 1), then n-1 lines each containing two integers u and v (1 <= u, v <= n), and finally one integer u (1 <= u <= n).
    numbers = []
    while True:
        nums = input().split()
        
        if len(nums) != 2:
            break
        
        num1 = int(nums[0])
        
        num2 = int(nums[1])
        
        numbers.append([num1, num2])
        
    #State: numbers = [[1, 2], [2, 3], [3, 4]]
    return numbers
    #The program returns a list of lists, where each sublist contains two integers. The list is [[1, 2], [2, 3], [3, 4]].

#Overall this is what the function does:The function reads input from stdin, expecting pairs of integers until a single integer is encountered, and returns a list of these integer pairs. The function does not perform any validation or processing on the input data beyond parsing it into a list of lists, where each sublist contains two integers. The returned list contains all the integer pairs read from stdin, in the order they were encountered.

