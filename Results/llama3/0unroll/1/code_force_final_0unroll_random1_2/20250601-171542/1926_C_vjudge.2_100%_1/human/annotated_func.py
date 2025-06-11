#State of the program right berfore the function call: stdin contains two inputs: first an integer (between 1 and 10^4) and then a list of integers (between 1 and 2 * 10^5).
    N = int(2 * 100000.0) + 1
    t = int(input())
    pd = [(0) for _ in range(N)]
    for i in range(1, N):
        pd[i] += pd[i - 1]
        
        for j in str(i):
            pd[i] += int(j)
        
    #State: Output State: N is 200001, t is an integer between 1 and 10^4, pd is a list of 200001 integers where each element at index i (1 <= i <= 200000) is the sum of all the digits of all the numbers from 1 to i, stdin contains no input.
    for _ in range(t):
        n = int(input())
        
        print(pd[n])
        
    #State: Output State: N is 200001, t is 0, pd is a list of 200001 integers where each element at index i (1 <= i <= 200000) is the sum of all the digits of all the numbers from 1 to i, stdin contains no input.

#Overall this is what the function does:The function reads an integer t from standard input, representing the number of test cases, and then reads t integers. For each integer n, it calculates and prints the sum of all digits of all numbers from 1 to n. The function uses a precomputed list pd to efficiently calculate this sum, where pd[i] is the sum of all digits of all numbers from 1 to i. After processing all test cases, the function concludes, leaving the input stream empty.

