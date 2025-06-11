#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 10^3) and then t integers n (3 <= n <= 10^5).
    for i in range(int(input())):
        n = [int(i) for i in input().split()][0]
        
        p = [0] * n
        
        ind = n
        
        for i in range(0, n, 2):
            p[i] = ind
            ind -= 2
        
        ind = 1 + n % 2
        
        for i in range(1, n, 2):
            p[i] = ind
            ind += 2
        
        print(*p)
        
    #State: The output state is a list of integers, where each integer is the result of the loop execution for the corresponding input integer n. The list contains t integers, where each integer is the result of the loop execution for the corresponding input integer n. The integers in the list are in the same order as the input integers.

#Overall this is what the function does:The function takes a series of integers as input, where the first integer t represents the number of test cases, followed by t integers n. For each integer n, the function generates a list of n integers, where the list is constructed by alternating between two sequences: one starting from n and decreasing by 2, and the other starting from 1 + n % 2 and increasing by 2. The function then prints the generated list for each test case. The output is a series of lists, each corresponding to the input integer n, in the same order as the input.

