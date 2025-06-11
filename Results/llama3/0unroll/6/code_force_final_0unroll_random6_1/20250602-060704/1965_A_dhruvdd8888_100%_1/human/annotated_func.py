#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (1 <= n <= 2*10^5) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
    N = int(input())
    nums = set(input().split())
    nums.add('0')
    nums = sorted(map(int, nums))
    ls = 0
    for i in range(len(nums)):
        nums[i] -= ls
        
        ls += nums[i]
        
    #State: nums is a sorted list of integers containing the integers from the input test cases and the integer 0, each decreased by the sum of the previous integers in the list, ls is the sum of all integers in nums.
    nw = True
    cw = True
    for i in range(len(nums) - 2, 0, -1):
        if nums[i] == 1:
            cw = not nw
        else:
            cw = True
        
        nw = cw
        
    #State: nums is a sorted list of integers containing the integers from the input test cases and the integer 0, each decreased by the sum of the previous integers in the list, ls is the sum of all integers in nums, nw is True, cw is True.
    if cw :
        print('Alice')
        #This is printed: Alice
    else :
        print('Bob')
        #This is printed: Bob
    #State: *nums is a sorted list of integers containing the integers from the input test cases and the integer 0, each decreased by the sum of the previous integers in the list, ls is the sum of all integers in nums, nw is True. If cw is True, 'Alice' is printed. If cw is False, 'Bob' is printed.

#Overall this is what the function does:This function determines the winner of a game based on a set of input integers. It takes a set of integers as input, sorts them, and then applies a series of transformations to the integers. The function then uses these transformed integers to determine the winner of the game, either 'Alice' or 'Bob', and prints the result.

