#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 10^4) and then t lines each containing an integer n (1 <= n <= 2 * 10^5).
    N = int(2 * 100000.0) + 1
    t = int(input())
    pd = [(0) for _ in range(N)]
    for i in range(1, N):
        pd[i] += pd[i - 1]
        
        for j in str(i):
            pd[i] += int(j)
        
    #State: N is 200001, t is an integer between 1 and 10^4 (inclusive), pd is a list of 200001 integers where each element at index i is the sum of all digits of all numbers from 1 to i, stdin contains t-1 lines each containing an integer n (1 <= n <= 2 * 10^5).
    for _ in range(t):
        n = int(input())
        
        print(pd[n])
        
    #State: Output State: The loop has executed t times, and for each iteration, it has printed the sum of all digits of all numbers from 1 to n, where n is the integer read from the standard input. The value of N remains unchanged at 200001, and the list pd remains unchanged. The variable t has been decremented by 1 in each iteration, so its final value is 0. The standard input has been consumed, and its contents are no longer available.

#Overall this is what the function does:This function reads a series of integers from standard input, calculates the sum of all digits of all numbers from 1 to each input integer, and prints the results. It consumes all input integers and leaves the input stream empty. The function does not modify any input values or store them; it only uses them to compute and print the sum of digits. The function's output is a series of sums, one for each input integer, and it does not return any value.

