#State of the program right berfore the function call: stdin contains two inputs: first an integer (1 <= t <= 10^3) and then t space-separated integers (3 <= n <= 10^5).
    for i in range(int(input())):
        a = [int(i) for i in input().split()][0]
        
        p = []
        
        for i in range(2, a + 1, 2):
            p += [i]
        
        for i in range(1, a + 1, 2):
            p += [i]
        
        print(*p)
        
    #State: stdin is empty, `i` is equal to `t`, `a` is the last integer in the input, `p` is a list of integers from 1 to `a` (inclusive), and the list of integers from 1 to `a` (inclusive) has been printed `t` times.

#Overall this is what the function does:The function reads a series of integers from standard input, where the first integer represents the number of test cases (t) and each subsequent integer (a) represents the size of a sequence. For each sequence, the function generates a list of integers from 1 to a (inclusive), with even numbers appearing before odd numbers, and prints this list. The function repeats this process t times, emptying the standard input buffer in the process.

