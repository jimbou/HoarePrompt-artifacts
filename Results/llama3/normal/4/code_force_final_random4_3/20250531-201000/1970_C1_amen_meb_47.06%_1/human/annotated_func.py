#State of the program right berfore the function call: stdin contains three inputs: first two integers n and t (2 <= n <= 2*10^5, t=1), then n-1 lines each containing two integers u and v (1 <= u, v <= n), and finally one integer u_1 (1 <= u_1 <= n).
    numbers = []
    while True:
        nums = input().split()
        
        if len(nums) != 2:
            break
        
        num1 = int(nums[0])
        
        num2 = int(nums[1])
        
        numbers.append([num1, num2])
        
    #State: numbers is a list containing n-1 lists with two integers each, num1 is an integer equal to the first integer in the last line of stdin, num2 is an integer equal to the second integer in the last line of stdin, nums is a list containing two integers that are the last two integers in stdin, stdin is empty.
    return numbers
    #The program returns a list of n-1 lists, each containing two integers, where the last two integers in the list are num1 and num2, and the list nums contains these two integers.

#Overall this is what the function does:The function reads input from stdin, expecting a specific format: two integers, followed by n-1 lines of two integers each, and finally one integer. It then returns a list of n-1 lists, each containing two integers, where the last two integers in the list are the last two integers read from stdin.

