#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two inputs: first an integer n and then a list of n integers. n is a positive integer and each integer in the list is a positive integer.
    N = int(input())
    nums = set(input().split())
    nums.add('0')
    nums = sorted(map(int, nums))
    ls = 0
    for i in range(len(nums)):
        nums[i] -= ls
        
        ls += nums[i]
        
    #State: Output State: N is a positive integer, nums is a sorted list of n+1 positive integers where each element is equal to its original value minus the sum of all the previous elements, ls is equal to the sum of all the original elements in nums.
    nw = True
    cw = True
    for i in range(len(nums) - 2, 0, -1):
        if nums[i] == 1:
            cw = not nw
        else:
            cw = True
        
        nw = cw
        
    #State: Output State: N is a positive integer, nums is a sorted list of n+1 positive integers where each element is equal to its original value minus the sum of all the previous elements, ls is equal to the sum of all the original elements in nums, nw is True, cw is True.
    if cw :
        print('Alice')
        #This is printed: Alice
    else :
        print('Bob')
        #This is printed: Bob
    #State: *N is a positive integer, nums is a sorted list of n+1 positive integers where each element is equal to its original value minus the sum of all the previous elements, ls is equal to the sum of all the original elements in nums, nw is True. If cw is True, then 'Alice' is printed. Otherwise, cw is False and 'Bob' is printed.

#Overall this is what the function does:This function determines the winner of a game based on a list of integers. It takes a positive integer N and a list of N positive integers as input, modifies the list by subtracting the sum of all previous elements from each element, and then checks the modified list from right to left. If the second last element is 1, the function prints 'Alice', otherwise it prints 'Bob'. The function does not return any value, it only prints the winner's name.

