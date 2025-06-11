#State of the program right berfore the function call: stdin contains t+1 lines of input. The first line contains one integer t (1 <= t <= 10^4). Each of the remaining t lines contains three integers n, a, and b (1 <= n <= 100, 1 <= a, b <= 30).
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        
        d = c / 2
        
        if a * b < a * d:
            print(a * b)
        else:
            print(round(a * d))
        
    #State: The loop will print the minimum value between the product of a and b, and the product of a and half of c, rounded to the nearest integer, for each line of input. The value of n will remain unchanged.

#Overall this is what the function does:This function reads a series of input lines from standard input, where the first line contains an integer t, and each subsequent line contains three integers n, a, and b. It then calculates and prints the minimum value between the product of a and b, and the product of a and half of c, rounded to the nearest integer, for each line of input. The function does not return any value, but instead prints the calculated values directly to the console.

