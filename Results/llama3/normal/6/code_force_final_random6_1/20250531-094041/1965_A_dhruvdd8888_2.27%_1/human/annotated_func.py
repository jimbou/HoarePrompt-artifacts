#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two lines. The first line contains an integer n. The second line contains n integers. t, n and all the integers are positive integers.
    N = int(input())
    nums = set(input().split())
    nums = sorted(map(int, nums))
    if (len(nums) == 1) :
        return print('Alice')
        #The program returns and prints the string 'Alice'.
    #State: *t is a positive integer decreased by 1, N is a positive integer, nums is a sorted list of n positive integers, stdin contains t-1 test cases. Each test case contains two lines. The first line contains an integer n. The second line contains n integers. The length of nums is more than 1
    if (len(nums) == 2) :
        return print('Bob')
        #The program returns the string 'Bob' and prints it.
    #State: *t is a positive integer decreased by 1, N is a positive integer, nums is a sorted list of n positive integers, stdin contains t-1 test cases. Each test case contains two lines. The first line contains an integer n. The second line contains n integers. The length of nums is more than 2
    nums.insert(0, 0)
    cd = 0
    for i in range(len(nums) - 2):
        if nums[i + 1] - nums[i] == 1:
            cd += 1
        else:
            break
        
    #State: t is a positive integer decreased by 1, N is a positive integer, nums is a sorted list of n+1 positive integers that must have at least n+1 elements, stdin contains t-1 test cases. Each test case contains two lines. The first line contains an integer n. The second line contains n integers. If the difference between the (i+1)th element and the ith element of nums is 1 for all i from 0 to n-2, then cd is n-1 and i is n-2. Otherwise, cd is the number of consecutive differences of 1 between the elements of nums and i is the index of the last element of the sequence of consecutive differences of 1.
    if (cd & 1) :
        return print('Bob')
        #The program returns and prints the string 'Bob'
    else :
        return print('Alice')
        #The program prints 'Alice' and returns None.

#Overall this is what the function does:Determines the winner of a game based on a sequence of numbers. The function reads a test case from standard input, where the first line contains the number of integers and the second line contains the integers themselves. It then checks the sequence of numbers and prints 'Alice' or 'Bob' depending on the sequence's properties, specifically the length of the sequence and the presence of consecutive differences of 1. The function handles four cases: a sequence of one number, a sequence of two numbers, a sequence with an odd number of consecutive differences of 1, and a sequence with an even number of consecutive differences of 1.

