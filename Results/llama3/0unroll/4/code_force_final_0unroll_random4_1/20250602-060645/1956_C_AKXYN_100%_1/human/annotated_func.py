#State of the program right berfore the function call: stdin contains one input: an integer (1 <= t <= 500), followed by t inputs, each of which is an integer (1 <= n <= 500).
    for _ in range(int(input())):
        n = int(input())
        
        mat = [list(range(1, n + 1)) for i in range(n)]
        
        res = 0
        
        for i in range(n):
            res += (i + 1) * (2 * i + 1)
        
        print(res, n << 1)
        
        for i in range(n, 0, -1):
            print('1 %d' % i, *range(1, n + 1))
            print('2 %d' % i, *range(1, n + 1))
        
    #State: The output state is a series of lines, each containing a string of numbers. The first line contains two numbers, the second line contains a string of numbers from 1 to n, and the third line contains another string of numbers from 1 to n. This pattern repeats for each input value of n. The number of lines in the output state is 3 times the number of input values of n.

#Overall this is what the function does:The function reads a series of integers from standard input, where the first integer represents the number of test cases (t), followed by t integers (n), each representing the size of a matrix. For each test case, the function calculates a result (res) based on the size of the matrix (n) and prints the result along with the value of n shifted left by 1 bit. Then, for each test case, the function prints two lines of numbers from 1 to n, with the first line starting with '1' and the second line starting with '2', repeating this pattern for each input value of n. The function outputs a series of lines, with each line containing a string of numbers, where the first line contains two numbers, and the subsequent lines contain strings of numbers from 1 to n, repeating this pattern for each input value of n.

