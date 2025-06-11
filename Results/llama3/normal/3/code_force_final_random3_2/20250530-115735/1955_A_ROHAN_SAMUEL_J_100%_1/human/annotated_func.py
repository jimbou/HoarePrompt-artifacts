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
        
    #State: The loop has finished executing, and the program has terminated. The output state is the final state of the program after all iterations of the loop have completed. The values of `n`, `a`, and `b` are no longer relevant, as the loop has finished executing. The program has processed all input lines and printed the results according to the conditions specified in the loop body. The program has terminated, and no further input or output is expected.

#Overall this is what the function does:This function reads a series of input lines, each containing three integers, and for each line, it calculates and prints a result based on the values of the integers. The calculation depends on whether the first integer is odd or even and the relationship between the second and third integers. The function processes all input lines and prints the corresponding results, then terminates.

