#State of the program right berfore the function call: stdin contains two inputs: first an integer (1 <= t <= 50) and then t integers (2 <= n <= 10^3).
    t = int(input())
    while t:
        t -= 1
        
        n = int(input())
        
        for i in range(1, n + 1):
            print('1', end=' ')
            print(i)
        
        print(' ')
        
    #State: t is 0, n is an integer between 2 and 10^3 inclusive, i is n+1, stdin is empty, and the number 1 is printed, and this is printed: 1, and '1' is printed followed by a space, and the value of i which is 2 is printed, and '1' is printed followed by a space, and the value of i which is 3 is printed, and ... , and '1' is printed followed by a space, and the value of i which is n is printed, and a space is printed, and this sequence is repeated t times.

#Overall this is what the function does:This function reads a series of integers from standard input, where the first integer represents the number of test cases (t), and each subsequent integer represents the number of times (n) to print a sequence of numbers. The function then prints a sequence of numbers, starting with 1, followed by a space, and then the value of the current iteration (i), for each value of n. This process is repeated t times. The function does not return any value, but instead prints the sequences of numbers directly to the console.

