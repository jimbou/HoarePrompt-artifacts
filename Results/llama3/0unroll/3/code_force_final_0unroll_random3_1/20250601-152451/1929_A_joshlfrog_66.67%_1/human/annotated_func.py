#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (the number of elements in the list) and then a list of integers. The integers in the list are between 1 and 10^9 (inclusive).
    t = int(input())
    for e in range(t):
        l = int(input())
        
        nums = [int(x) for x in input().split()]
        
        x = 0
        
        y = 100000000
        
        for i in range(l):
            if nums[i] > x:
                x = nums[i]
            if nums[i] < y:
                y = nums[i]
        
        print(x - y)
        
    #State: Output State: The loop will execute `t` times, where `t` is the number of test cases. In each iteration, it will read a list of integers from stdin, find the maximum and minimum values in the list, and print their difference. After all iterations, the loop will finish, and the program will terminate. The output will be the differences between the maximum and minimum values for each test case, printed on separate lines.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer (the number of elements in the list) followed by a list of integers. It then finds the maximum and minimum values in each list and prints their difference. The function repeats this process for each test case, producing a separate output for each case.

