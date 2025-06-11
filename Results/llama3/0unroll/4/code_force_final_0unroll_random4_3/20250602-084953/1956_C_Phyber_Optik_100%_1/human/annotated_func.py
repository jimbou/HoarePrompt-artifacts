#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains one integer n (1 <= n <= 500) on a line.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        sum = 1
        
        for i in range(2, n + 1):
            sum += (i * i - (i - 1) * (i - 1)) * i
        
        print(sum, n + n)
        
        for j in range(1, n + 1):
            print(1, n - j + 1, *range(1, n + 1))
            print(2, n - j + 1, *range(1, n + 1))
        
    #State: The loop has executed t times, and for each execution, it has printed the sum of the squares of the numbers from 1 to n, the value of n + n, and two sets of numbers from 1 to n, each preceded by the numbers 1 and 2, respectively. The value of t remains unchanged, as it is not modified within the loop. The input from stdin has been consumed, and the output has been printed to the console.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case contains an integer n. For each test case, it calculates the sum of squares of numbers from 1 to n, prints the sum along with the value of n + n, and then prints two sets of numbers from 1 to n, each preceded by the numbers 1 and 2, respectively. The function consumes all input from standard input and produces output to the console, without modifying any external state or returning any value.

