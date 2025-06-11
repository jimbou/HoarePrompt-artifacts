#State of the program right berfore the function call: stdin contains t+1 lines, where t is an integer (1 <= t <= 10^4). The first line contains t. Each of the following t lines contains three integers n, a, and b (1 <= n <= 100, 1 <= a, b <= 30).
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        if n % 2:
            if 2 * a < b:
                print(a * n)
            else:
                print(n // 2 * b + a)
        elif 2 * a < b:
            print(a * n)
        else:
            print(n // 2 * b)
        
    #State: The output state will contain t lines, each representing the result of the calculation for the corresponding input line. The result will be the maximum of a*n and n//2*b, depending on the values of a, b, and n.

#Overall this is what the function does:Calculates and prints the maximum of two possible values for each input line, where the values are determined by the number of items (n), the cost of item A (a), and the cost of item B (b). For each input line, the function prints the maximum of a*n and n//2*b, taking into account whether n is odd or even. The function processes multiple input lines and prints the result for each line separately.

