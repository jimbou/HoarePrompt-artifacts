#State of the program right berfore the function call: stdin contains t+1 lines, where t is a positive integer. The first line contains t. Each of the following t lines contains a positive integer n. Each of the following t lines contains n positive integers.
    N = int(input())
    nums = set(input().split())
    nums = sorted(map(int, nums))
    if (len(nums) == 1) :
        return print('Alice')
        #The program prints and returns the string 'Alice'.
    #State: N is a positive integer, nums is a sorted list of positive integers, stdin contains t lines, where t is a positive integer. The length of nums is more than 1.
    if (len(nums) == 2) :
        return print('Bob')
        #The program prints 'Bob' and returns None
    #State: *N is a positive integer, nums is a sorted list of positive integers, stdin contains t lines, where t is a positive integer. The length of nums is more than 2
    nums.insert(0, 0)
    cd = 0
    for i in range(len(nums) - 2):
        if nums[i + 1] - nums[i] == 1:
            cd += 1
        else:
            break
        
    #State: Output State: N is a positive integer, nums is a sorted list of positive integers with a prepended 0, cd is the number of consecutive integers in the list starting from the second element, stdin contains t lines.
    if (cd & 1) :
        return print('Bob')
        #The program prints 'Bob' and returns None.
    else :
        return print('Alice')
        #The program prints 'Alice' and returns None

#Overall this is what the function does:This function determines the winner of a game based on a sequence of positive integers. It reads input from stdin, where the first line contains the number of test cases, and each subsequent line contains a sequence of positive integers. The function then analyzes the sequence to determine the winner, either 'Alice' or 'Bob', and prints the result. The function returns None in all cases except when the input sequence contains only one element, in which case it returns the string 'Alice'.

