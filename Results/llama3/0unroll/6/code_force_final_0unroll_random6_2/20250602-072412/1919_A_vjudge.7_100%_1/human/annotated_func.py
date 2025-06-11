#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 ≤ t ≤ 1000). Each of the following t lines contains two integers a and b (1 ≤ a, b ≤ 10^9).
    test = int(input())
    for t in range(test):
        a, b = map(int, input().split())
        
        if a + b & 1 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: The output will be a series of 'Bob' and 'Alice' printed to the console, where 'Bob' is printed when the sum of a and b is even, and 'Alice' is printed when the sum of a and b is odd. The number of lines printed will be equal to the value of `test`. The value of `test` remains unchanged. The stdin will be empty after the loop finishes execution.

#Overall this is what the function does:This function reads a series of input lines from the standard input, where the first line contains a single integer 'test' representing the number of test cases, and each subsequent line contains two integers 'a' and 'b'. It then prints 'Bob' to the console if the sum of 'a' and 'b' is even, and 'Alice' if the sum is odd, repeating this process for each test case. The function does not return any value, and its only effect is printing the results to the console.

