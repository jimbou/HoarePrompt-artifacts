#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing three integers n, a, and b (1 <= n <= 100, 1 <= a, b <= 30).
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        
        d = c / 2
        
        if a * b < a * d:
            print(a * b)
        else:
            print(round(a * d))
        
    #State: n is an integer greater than or equal to 0, i is n-1, a is an integer between 1 and 100, b is an integer between 1 and 30, c is an integer between 1 and 30, d is a float equal to half of c, stdin contains t-n lines, each containing three integers n, a, and b (1 <= n <= 100, 1 <= a, b <= 30). If the product of a and b is less than the product of a and d, the product of a and b is printed. Otherwise, the rounded value of the product of a and d is printed.

#Overall this is what the function does:This function reads a series of input lines from standard input, where each line contains three integers: n, a, and b. It then calculates the product of a and b, and the product of a and half of c. If the product of a and b is less than the product of a and half of c, it prints the product of a and b; otherwise, it prints the rounded value of the product of a and half of c. This process is repeated for a number of times specified by the initial input integer t.

