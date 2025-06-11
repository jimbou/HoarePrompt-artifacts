#State of the program right berfore the function call: stdin contains two inputs: two positive integers n and k such that 1 <= n <= 26 and 1 <= k <= 26.
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        print('abcdefghijklmnopqrstuvwxyz'[:k] * n)
        
    #State: The loop has executed t iterations, printing the first k letters of the alphabet n times in each iteration. The value of t remains unchanged, but the values of n and k have been updated to the last input values. The output is a string of length n*k*t, consisting of the first k letters of the alphabet repeated n times in each iteration.

#Overall this is what the function does:The function reads a series of pairs of positive integers (n, k) from standard input, where 1 <= n <= 26 and 1 <= k <= 26, and prints the first k letters of the alphabet repeated n times for each pair. The function repeats this process for a number of iterations specified by an initial input t, resulting in a total output string of length n*k*t.

