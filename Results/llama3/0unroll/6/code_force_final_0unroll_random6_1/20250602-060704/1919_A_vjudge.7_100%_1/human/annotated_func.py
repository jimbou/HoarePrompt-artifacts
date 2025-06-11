#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 ≤ t ≤ 1000). Each of the following t lines contains two integers a and b (1 ≤ a, b ≤ 10^9).
    test = int(input())
    for t in range(test):
        a, b = map(int, input().split())
        
        if a + b & 1 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: The output will be a series of lines, each containing either 'Alice' or 'Bob', depending on whether the sum of the two integers in the corresponding line of input is odd or even. The number of lines in the output will be equal to the value of 'test'. The value of 'test' and the contents of stdin will remain unchanged.

#Overall this is what the function does:This function reads a series of lines from standard input, where the first line contains a single integer 'test' and each subsequent line contains two integers 'a' and 'b'. It then prints 'Alice' or 'Bob' for each pair of integers, depending on whether their sum is odd or even, respectively. The function prints 'test' number of lines and leaves the input unchanged.

