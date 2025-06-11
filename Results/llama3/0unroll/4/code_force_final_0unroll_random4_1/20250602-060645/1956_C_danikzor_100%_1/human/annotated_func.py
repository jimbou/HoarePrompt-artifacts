#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains one input: a positive integer (n) representing the size of the matrix.
    n = int(input())
    print(n * (n + 1) * (4 * n - 1) // 6, 2 * n)
    #This is printed: the sum of squares of the first n natural numbers, 2 times the value of n (where n is a positive integer)
    for i in range(1, n + 1):
        print(1, i, *range(n, 0, -1))
        
        print(2, i, *range(n, 0, -1))
        
    #State: The output state after the loop executes all the iterations is a sequence of lines, where each line contains a sequence of numbers. The first number in each line is either 1 or 2, the second number is a value from 1 to n (inclusive), and the remaining numbers are a sequence of numbers from n to 1 (inclusive) in reverse order. The total number of lines is 2n.

#Overall this is what the function does:The function generates and prints a sequence of lines based on a given positive integer n, representing the size of a matrix. It first prints the sum of squares of the first n natural numbers and 2 times the value of n. Then, it prints 2n lines, where each line contains a sequence of numbers. The first number in each line is either 1 or 2, the second number is a value from 1 to n (inclusive), and the remaining numbers are a sequence of numbers from n to 1 (inclusive) in reverse order.

