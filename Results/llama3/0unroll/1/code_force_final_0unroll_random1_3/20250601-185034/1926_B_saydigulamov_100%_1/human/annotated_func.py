#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains an integer n (2 <= n <= 10) followed by n lines each containing n characters '0' or '1'. The grid contains exactly one triangle or exactly one square that contains all the '1's in the grid. The size of the triangle or square is greater than 1.
    a = int(input())
    for i in range(a):
        k = []
        
        for _ in range(int(input())):
            b = input()
            if '1' in b:
                k.append(b.count('1'))
        
        if k[0] == k[1]:
            print('SQUARE')
        else:
            print('TRIANGLE')
        
    #State: Output State: The loop has executed 'a' number of times, where 'a' is an integer between 2 and 10 inclusive. For each execution, it has read 'a' lines from the standard input, where each line contains a string of '0's and '1's. It has then checked if the number of '1's in the first two lines are equal. If they are equal, it has printed 'SQUARE', otherwise it has printed 'TRIANGLE'. The output state is the same as the initial state, with the addition of 'a' number of lines printed to the standard output, each containing either 'SQUARE' or 'TRIANGLE'.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains a grid of '0's and '1's. It determines whether the grid contains a square or a triangle based on the number of '1's in the first two lines and prints 'SQUARE' or 'TRIANGLE' accordingly. The function repeats this process for a specified number of test cases, ranging from 2 to 10, and outputs the results to standard output.

