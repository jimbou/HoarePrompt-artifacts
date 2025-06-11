#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing three integers n, a, and b (1 <= n <= 100, 1 <= a, b <= 30).
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
        
    #State: The output state will contain t lines, each containing a single integer, which is the result of the calculation for the corresponding input line. The calculation is based on the values of n, a, and b, and the conditions specified in the loop.

#Overall this is what the function does:Calculates and prints the minimum cost for t scenarios, each involving n items with costs a and b, based on conditions specified in the loop, and outputs the results in t lines, one integer per line.

