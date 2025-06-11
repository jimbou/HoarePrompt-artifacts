#State of the program right berfore the function call: stdin contains three inputs: first two integers n and t, where n is an integer greater than or equal to 2 and t is 1, then n-1 lines each containing two integers u and v, where u and v are integers between 1 and n, and finally one integer u_1, where u_1 is an integer between 1 and n.
    numbers = []
    while True:
        nums = input().split()
        
        if len(nums) != 2:
            break
        
        num1 = int(nums[0])
        
        num2 = int(nums[1])
        
        numbers.append([num1, num2])
        
    #State: numbers is a list containing n-1 sublists [[n, 1], [u_1, u_2], ..., [u_(n-2), u_(n-1)]], num1 is an integer u_(n-1), num2 is an integer u_n, nums is a list containing two strings u_(n-1) and u_n, stdin contains one integer u_n, where u_n is an integer between 1 and n.
    return numbers
    #The program returns a list of n-1 sublists, where the first sublist contains two integers n and 1, and the remaining sublists contain integers u_1 to u_(n-1), and the last sublist contains an integer u_(n-1) which is also the value of num1, and the last integer u_n which is also the value of num2 and is also present in the stdin and is a string in the list nums.

#Overall this is what the function does:The function reads input from stdin, expecting a sequence of integers in a specific format, and returns a list of sublists containing these integers. The input sequence starts with two integers, n and t, followed by n-1 lines of two integers each, and finally one integer. The function reads this input, constructs a list of sublists from the integers, and returns this list. The returned list contains n-1 sublists, where the first sublist contains the first two integers n and 1, and the remaining sublists contain the subsequent integers. The last sublist contains the last two integers read from the input.

