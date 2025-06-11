#State of the program right berfore the function call: stdin contains t+1 inputs: the first input is a positive integer t (1 <= t <= 10^4), and the remaining t inputs are lines each containing three positive integers n, a, and b (1 <= n <= 100, 1 <= a, b <= 30).
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        
        d = c / 2
        
        if a * b < a * d:
            print(a * b)
        else:
            print(round(a * d))
        
    #State: n is greater than or equal to 0, i is n-1, a is an integer, b is an integer, c is an integer, d is a float equal to half of c. If the product of a and b is less than the product of a and d, the product of a and b is printed. Otherwise, the rounded product of a and d is printed.

#Overall this is what the function does:This function reads a series of inputs from the standard input, where the first input is a positive integer t, and the remaining t inputs are lines each containing three positive integers n, a, and b. For each line of three integers, it calculates the product of a and b, and the product of a and half of c. It then prints the smaller of these two products, rounding the product of a and half of c to the nearest integer if necessary. The function does not return any value, but instead prints the results for each input line.

