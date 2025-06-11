#State of the program right berfore the function call: stdin contains t+1 lines, where t is an integer (1 <= t <= 10^4). The first line contains the integer t. Each of the following t lines contains three integers n, a, and b (1 <= n <= 100, 1 <= a, b <= 30).
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        
        d = c / 2
        
        if a * b < a * d:
            print(a * b)
        else:
            print(round(a * d))
        
    #State: The program will print n lines, each containing the minimum value between the product of a and b, and the product of a and half of c, rounded to the nearest integer. The value of n remains unchanged.

#Overall this is what the function does:The function reads an integer t from standard input, representing the number of test cases. For each test case, it reads three integers a, b, and c, and prints the minimum value between the product of a and b, and the product of a and half of c, rounded to the nearest integer. The function performs this calculation for t test cases and prints the results, leaving the value of t unchanged.

