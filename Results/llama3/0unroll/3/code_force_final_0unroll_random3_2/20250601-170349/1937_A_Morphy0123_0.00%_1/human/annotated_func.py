#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains an integer t (1 <= t <= 10^4) representing the number of test cases. Each of the following t lines contains one integer n (1 <= n <= 10^9) representing the length of the array a.
    n_cases = int(input())
    for i in range(n_cases):
        n = int(input())
        
        if n == 1:
            print(1)
        else:
            power = 1
            while power < log2(n):
                power += 1
            if power == n:
                print(2 ** power)
            else:
                power -= 1
                print(2 ** power)
        
    #State: Output State: The program will print the largest power of 2 that is less than or equal to the given number n for each test case. If n is a power of 2, it will print n. If n is 1, it will print 1. The number of test cases t will be processed, and the program will terminate after printing the results for all test cases.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case is an integer representing the length of an array. For each test case, it calculates and prints the largest power of 2 that is less than or equal to the given number. If the number is a power of 2, it prints the number itself. If the number is 1, it prints 1. The function processes all test cases and terminates after printing the results.

