#State of the program right berfore the function call: stdin contains t+1 lines, where t is a positive integer. The first line contains one integer t. Each of the remaining t lines contains three positive integers n, a, and b, where n is less than or equal to 100, and a and b are less than or equal to 30.
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        s1 = n * a
        
        s2 = b * (n // 2) + n % 2 * a
        
        print(min(s1, s2))
        
    #State: The output state will contain t lines, each containing the minimum of two calculated values, s1 and s2, for each of the t test cases. The values of s1 and s2 are calculated based on the input values of n, a, and b for each test case.

#Overall this is what the function does:The function reads input from stdin, processes multiple test cases, and prints the minimum of two calculated values for each case. It takes no arguments and returns no values, instead, it outputs the results directly to the console. The function's purpose is to calculate and display the minimum cost for each test case based on the provided input values.

