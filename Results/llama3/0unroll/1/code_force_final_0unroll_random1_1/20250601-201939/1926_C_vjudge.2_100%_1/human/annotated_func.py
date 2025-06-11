#State of the program right berfore the function call: stdin contains two inputs: first an integer (the number of test cases) and then a list of integers (the largest number Vladislav writes for each test case). The first integer is a positive integer and each integer in the list is a positive integer less than or equal to 2*10^5.
    N = int(2 * 100000.0) + 1
    t = int(input())
    pd = [(0) for _ in range(N)]
    for i in range(1, N):
        pd[i] += pd[i - 1]
        
        for j in str(i):
            pd[i] += int(j)
        
    #State: Output State: N is 200001, t is a positive integer, pd is a list of 200001 integers where each element at index i is the sum of all digits of all numbers from 1 to i, stdin contains 1 input: a list of integers.
    for _ in range(t):
        n = int(input())
        
        print(pd[n])
        
    #State: Output State: N is 200001, t is 0, pd is a list of 200001 integers where each element at index i is the sum of all digits of all numbers from 1 to i, stdin contains 0 input.

#Overall this is what the function does:This function reads a positive integer (the number of test cases) and a list of integers from standard input, calculates the sum of all digits of all numbers from 1 to each integer in the list, and prints the results. The function does not modify the input values and does not have any side effects other than printing the results. After execution, the function leaves the input stream empty.

