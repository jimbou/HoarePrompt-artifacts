#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two inputs: first an integer n and then a space-separated list of n integers. n is a positive integer and each integer in the list is a positive integer.
    N = int(input())
    nums = set(input().split())
    nums.add('0')
    nums = sorted(map(int, nums))
    ls = 0
    for i in range(len(nums)):
        nums[i] -= ls
        
        ls += nums[i]
        
    #State: N is a positive integer, nums is a sorted list of n+1 positive integers with all elements reduced by the sum of the first i elements of the original list, ls is equal to the sum of all elements of the original list, i is n, stdin contains t-1 test cases
    nw = True
    cw = True
    for i in range(len(nums) - 2, 0, -1):
        if nums[i] == 1:
            cw = not nw
        else:
            cw = True
        
        nw = cw
        
    #State: N is a positive integer, nums is a sorted list of n+1 positive integers with all elements reduced by the sum of the first i elements of the original list and must have at least 3 elements, ls is equal to the sum of all elements of the original list, i is 1, nw is equal to cw, cw is False if nums[i] is 1, otherwise cw is True, stdin contains t-1 test cases.
    if cw :
        print('Alice')
        #This is printed: Alice
    else :
        print('Bob')
        #This is printed: Bob
    #State: *N is a positive integer, nums is a sorted list of n+1 positive integers with all elements reduced by the sum of the first i elements of the original list and must have at least 3 elements, ls is equal to the sum of all elements of the original list, i is 1, nw is equal to cw. If nums[i] is not 1, cw is True and 'Alice' is printed. If nums[i] is 1, cw is False and 'Bob' is printed.

#Overall this is what the function does:This function determines the winner of a game based on a list of integers. It takes a positive integer N and a list of N positive integers as input, modifies the list by subtracting the sum of the first i elements from each element, and then checks the modified list from right to left. If the second last element is 1, the function prints 'Bob', otherwise it prints 'Alice'. The function repeats this process for multiple test cases.

