#State of the program right berfore the function call: stdin contains one input: an integer (the number of test cases), followed by that many test cases. Each test case contains one input: a positive integer (the size of the matrix).
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
        
    #State: The output state after the loop executes all the iterations is a series of print statements for each test case. For each test case, the first line contains the value of 'res' (which is the sum of the products of the row number and the sum of the first '2*i + 1' odd numbers) and 'n << 1' (which is twice the size of the matrix). The following lines contain two types of print statements: '1 i' followed by the numbers from 1 to 'n', and '2 i' followed by the numbers from 1 to 'n', where 'i' ranges from 'n' to 1 in reverse order. The number of test cases and the size of the matrix 'n' remain unchanged.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of a positive integer representing the size of a matrix. For each test case, it calculates a value 'res' as the sum of the products of the row number and the sum of the first '2*i + 1' odd numbers, and prints this value along with twice the size of the matrix. It then prints a series of lines for each test case, containing two types of statements: '1 i' followed by numbers from 1 to 'n', and '2 i' followed by numbers from 1 to 'n', where 'i' ranges from 'n' to 1 in reverse order. The function does not modify the input values or the size of the matrix.

