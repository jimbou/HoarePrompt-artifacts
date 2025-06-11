#State of the program right berfore the function call: stdin contains two inputs: first an integer (1 ≤ t ≤ 50) and then t lines each containing a single integer n (2 ≤ n ≤ 10^3).
    t = int(input())
    for i in range(t):
        n = int(input())
        
        print('1 1')
        
        print('1 2')
        
        if n == 3:
            print('2 3')
        elif n >= 4:
            print('2 4')
            for j in range(4, n + 1):
                print(str(j) + ' ' + str(j))
        
    #State: The output state will contain 2t + 2 lines. The first two lines will always be '1 1' and '1 2'. For each input n, if n is 3, the next line will be '2 3'. If n is 4 or more, the next line will be '2 4', followed by n - 3 lines of the form 'j j', where j ranges from 4 to n.

#Overall this is what the function does:The function reads a series of integers from standard input, where the first integer represents the number of test cases (t) and each subsequent integer (n) represents the number of lines to be printed in a specific pattern. For each test case, the function prints a fixed pattern of lines, starting with '1 1' and '1 2', followed by either '2 3' if n is 3, or '2 4' and then n-3 lines of the form 'j j' if n is 4 or more. The function generates a total of 2t + 2 lines of output, where t is the number of test cases.

