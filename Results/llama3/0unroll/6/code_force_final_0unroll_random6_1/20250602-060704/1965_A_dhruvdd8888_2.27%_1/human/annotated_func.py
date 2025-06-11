#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer and then a list of integers. The first integer is a non-negative integer and represents the number of piles in the game. The list of integers represents the initial number of stones in each pile and contains at least one integer.
    N = int(input())
    nums = set(input().split())
    nums = sorted(map(int, nums))
    if (len(nums) == 1) :
        return print('Alice')
        #The program prints 'Alice' and returns None.
    #State: *N is a non-negative integer, nums is a sorted list of unique integers, stdin contains multiple test cases - 1. The length of nums is more than 1
    if (len(nums) == 2) :
        return print('Bob')
        #The program prints 'Bob' and returns None.
    #State: *N is a non-negative integer, nums is a sorted list of unique integers, stdin contains multiple test cases - 1. The length of nums is more than 2
    nums.insert(0, 0)
    cd = 0
    for i in range(len(nums) - 2):
        if nums[i + 1] - nums[i] == 1:
            cd += 1
        else:
            break
        
    #State: cd is the number of consecutive integers in the sorted list nums starting from the first element, N remains unchanged, nums remains unchanged, stdin remains unchanged.
    if (cd & 1) :
        return print('Bob')
        #The program returns the string 'Bob' and the value of cd remains an odd number.
    else :
        return print('Alice')
        #The program prints 'Alice' and returns None

#Overall this is what the function does:Determines the winner of a game based on the number of piles and stones in each pile, printing 'Alice' or 'Bob' depending on the game's state and returning None.

