#State of the program right berfore the function call: stdin contains three inputs: first two integers n and t (2 <= n <= 2*10^5 and t=1), then n-1 lines each containing two integers 1 <= u, v <= n, and finally one line containing one integer 1 <= u_1 <= n.
    numbers = []
    while True:
        nums = input().split()
        
        if len(nums) != 2:
            break
        
        num1 = int(nums[0])
        
        num2 = int(nums[1])
        
        numbers.append([num1, num2])
        
    #State: numbers is a list containing n-1 lists [[n, 1], [num1, num2], ..., [num1, num2]], nums is a list containing two strings, stdin contains one line containing one integer 1 <= u_1 <= n, num1 is an integer, num2 is an integer.
    return numbers
    #The program returns a list of n-1 lists, where the first list contains two integers n and 1, and the remaining lists contain two integers num1 and num2, and n is an integer between 1 and the value of u_1 read from stdin.

#Overall this is what the function does:The function reads input from stdin, expecting a series of lines containing two integers each, until a line with a single integer is encountered. It then returns a list of n-1 lists, where each sublist contains two integers. The first sublist contains the total number of nodes (n) and 1, while the remaining sublists contain pairs of integers representing edges in a graph. The function does not perform any validation or processing on the input data beyond parsing it into the desired format.

