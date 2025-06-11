#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing three integers n, a, and b (1 <= n <= 100, 1 <= a, b <= 30).
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        
        d = c / 2
        
        if a * b < a * d:
            print(a * b)
        else:
            print(round(a * d))
        
    #State: n is an integer between 1 and 10^4 (inclusive), a is an integer between 1 and 30 (inclusive), b is an integer between 1 and 30 (inclusive), c is an integer between 1 and 30 (inclusive), d is a float equal to half of c, i is n-1, stdin is empty. If the product of a and b is less than the product of a and d, then the product of a and b is printed. Otherwise, the rounded value of a times d is printed.

#Overall this is what the function does:This function reads a series of input lines from standard input, where each line contains three integers. For each line, it calculates the product of the first two integers and compares it to the product of the first integer and half of the third integer. Depending on the comparison result, it prints either the product of the first two integers or the rounded value of the product of the first integer and half of the third integer. The function processes a specified number of input lines, as indicated by the first integer read from standard input.

