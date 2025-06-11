#State of the program right berfore the function call: stdin contains one or more inputs: an integer (greater than 0).
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        sum = 1
        
        for i in range(2, n + 1):
            sum += (i * i - (i - 1) * (i - 1)) * i
        
        print(sum, n + n)
        
        for j in range(1, n + 1):
            print(1, n - j + 1, *range(1, n + 1))
            print(2, n - j + 1, *range(1, n + 1))
        
    #State: t is 0, stdin contains no more inputs, n is the last input integer, i is n+1, j is n+1, and sum is 1 + ∑[(i * i - (i - 1) * (i - 1)) * i] from i=2 to n.

#Overall this is what the function does:The function reads a series of integers from standard input, where the first integer t represents the number of subsequent integers. For each integer n, it calculates a sum using a formula involving squares and cubes of numbers from 2 to n, then prints the sum and the value 2n. It then prints a series of lines, each containing the numbers 1 and 2, followed by a range of numbers from 1 to n, repeated n times. After processing all integers, the function leaves the input stream empty and the variables t, n, i, and j with values 0, the last input integer, n+1, and n+1, respectively, and the sum variable with the calculated value.

