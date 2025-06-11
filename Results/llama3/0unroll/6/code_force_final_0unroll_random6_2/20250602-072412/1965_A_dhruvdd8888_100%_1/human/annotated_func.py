#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer and then a space-separated list of integers. The first integer is a positive integer and represents the number of piles. The list of integers represents the number of stones in each pile and contains the same number of elements as the first integer. All integers in the list are positive and do not exceed 10^9.
    N = int(input())
    nums = set(input().split())
    nums.add('0')
    nums = sorted(map(int, nums))
    ls = 0
    for i in range(len(nums)):
        nums[i] -= ls
        
        ls += nums[i]
        
    #State: Output State: N is a positive integer, nums is a sorted list of positive integers containing the number of stones in each pile and 0, ls is the sum of all the numbers in the nums list.
    nw = True
    cw = True
    for i in range(len(nums) - 2, 0, -1):
        if nums[i] == 1:
            cw = not nw
        else:
            cw = True
        
        nw = cw
        
    #State: Output State: N is a positive integer, nums is a sorted list of positive integers containing the number of stones in each pile and 0, ls is the sum of all the numbers in the nums list, nw is True, cw is True
    if cw :
        print('Alice')
        #This is printed: Alice
    else :
        print('Bob')
        #This is printed: Bob
    #State: *N is a positive integer, nums is a sorted list of positive integers containing the number of stones in each pile and 0, ls is the sum of all the numbers in the nums list, nw is True. If cw is True, 'Alice' is being printed. If cw is False, 'Bob' is being printed.

#Overall this is what the function does:This function determines the winner of a game involving stone piles. It takes as input the number of piles and the number of stones in each pile, and outputs either 'Alice' or 'Bob' based on a specific winning condition. The function processes the input by sorting the stone counts, calculating a cumulative sum, and then evaluating a boolean flag based on the sorted stone counts. The final output is the name of the winner, either 'Alice' or 'Bob', depending on the value of the boolean flag.

