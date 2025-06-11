#State of the program right berfore the function call: stdin contains t+1 lines of input. The first line contains one integer t (1 <= t <= 10^4). Each of the next t lines contains three integers n, a, and b (1 <= n <= 100, 1 <= a, b <= 30).
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        
        d = c / 2
        
        if a * b < a * d:
            print(a * b)
        else:
            print(round(a * d))
        
    #State: The output will be n lines, each containing a single integer. This integer will be the minimum of a*b and a*d, where d is half of c. If a*b is less than a*d, the output will be a*b; otherwise, it will be a*d rounded to the nearest integer.

#Overall this is what the function does:This function reads input from stdin, expecting t+1 lines, where t is an integer on the first line, and each subsequent line contains three integers n, a, and b. It then calculates and prints the minimum of a*b and a*d for each set of inputs, where d is half of c, rounding a*d to the nearest integer if it's greater than or equal to a*b. The function outputs n lines, each containing the calculated minimum value.

