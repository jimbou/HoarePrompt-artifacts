#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 10^3). Each of the following t lines contains a single integer n (3 <= n <= 10^5).
    for i in range(int(input())):
        a = [int(i) for i in input().split()][0]
        
        p = []
        
        for i in range(2, a + 1, 2):
            p += [i]
        
        for i in range(1, a + 1, 2):
            p += [i]
        
        print(*p)
        
    #State: The output state contains t lines, each containing the numbers from 1 to n, where n is the number on the corresponding line in the initial state. The numbers are arranged in a specific pattern: first, all even numbers from 2 to n are printed, followed by all odd numbers from 1 to n.

#Overall this is what the function does:The function reads a series of integers from standard input, where the first integer t represents the number of test cases, and each subsequent integer n represents the number of elements in a sequence. For each sequence, the function rearranges the numbers from 1 to n in a specific pattern, printing all even numbers from 2 to n followed by all odd numbers from 1 to n, and outputs the rearranged sequences for all test cases.

