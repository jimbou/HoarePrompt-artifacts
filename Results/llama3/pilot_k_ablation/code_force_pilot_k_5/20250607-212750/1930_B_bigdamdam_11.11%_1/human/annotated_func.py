#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 10^3). Each of the following t lines contains a single integer n (3 <= n <= 10^5).
    for i in range(int(input())):
        a = [int(i) for i in input().split()][0]
        
        p = []
        
        for i in range(2, a + 1, 2):
            p += [i]
        
        for i in range(1, a + 1, 2):
            p += [i]
        
        print(*p)
        
    #State: The loop has finished executing, and the output state is the final state after the last iteration of the loop. The variable `a` is the last integer read from the input, `i` is equal to `a`, `p` is a list containing all even integers from 2 to `a` inclusive, followed by all odd integers from 1 to `a` inclusive, and the list `p` has been printed. The input has been fully consumed, and there are no more lines of input left.

#Overall this is what the function does:The function reads a series of integers from standard input, where the first integer represents the number of subsequent integers to process. For each integer, it generates a list of numbers from 2 to the integer (inclusive), alternating between even and odd numbers, and prints this list. The function continues this process until all input integers have been processed, consuming all input lines.

