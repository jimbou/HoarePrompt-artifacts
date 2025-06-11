#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 10^3). Each of the following t lines contains a single integer n (3 <= n <= 10^5).
    for i in range(int(input())):
        a = [int(i) for i in input().split()][0]
        
        p = []
        
        for i in range(2, a + 1, 2):
            p += [i]
        
        for i in range(1, a + 1, 2):
            p += [i]
        
        print(*p)
        
    #State: `i` is `t`, `a` is an integer between 3 and 10^5 (inclusive), `p` is a list containing all integers from 1 to `a` (inclusive), stdin is empty, and the list `p` containing all integers from 1 to `a` is being printed.

#Overall this is what the function does:The function reads a series of integers from standard input, where the first integer represents the number of test cases, and each subsequent integer represents the size of a list. For each list size, the function generates a list of integers from 1 to the list size, alternating between even and odd numbers, and prints the list. The function repeats this process for the specified number of test cases, until standard input is empty.

