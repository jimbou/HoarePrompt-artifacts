#State of the program right berfore the function call: stdin contains t test cases. Each test case contains an integer n (2 <= n <= 10) followed by n lines each containing n characters 0 or 1. The grid contains exactly one triangle or exactly one square that contains all the 1s in the grid. The size of the triangle or square is greater than 1.
    a = int(input())
    for i in range(a):
        k = []
        
        for _ in range(int(input())):
            b = input()
            if '1' in b:
                k.append(b.count('1'))
        
        if k[0] == k[1]:
            print(k)
        
    #State: Output State: The loop will execute 'a' number of times. In each iteration, it will read 'n' lines from the standard input, where 'n' is the integer provided in the first line of each test case. It will then count the number of '1's in each line and store them in the list 'k'. If the first two elements of 'k' are equal, it will print the list 'k'. The value of 'a' remains unchanged after the loop execution.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of an integer n followed by n lines of n characters (0s and 1s). It then counts the number of 1s in each line and stores them in a list. If the first two elements of the list are equal, it prints the list. The function repeats this process for the specified number of test cases, leaving the input variable unchanged.

