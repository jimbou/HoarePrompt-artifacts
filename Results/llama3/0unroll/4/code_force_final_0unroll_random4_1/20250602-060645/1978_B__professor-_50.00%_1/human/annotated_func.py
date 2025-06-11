#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three integers n, a, and b (1 <= n, a, b <= 10^9).
    t = int(input())
    for _ in range(t):
        n, a, b = map(int, input().split())
        
        if b <= a:
            print(n * a)
        elif b - a >= n:
            print(int((2 * b - n + 1) * n / 2))
        else:
            print(int((b - a) / 2 * (b - a + 1) + a * n))
        
    #State: The loop has executed 't' number of times, and for each iteration, it has printed the calculated value based on the conditions provided. The value of 't' has been decremented to 0, and the stdin has been exhausted of all test cases. The values of 'n', 'a', and 'b' have been updated for each iteration but are no longer relevant after the loop finishes.

#Overall this is what the function does:Calculates and prints the maximum sum of 'n' consecutive integers within the range [a, b] for multiple test cases, where 'n', 'a', and 'b' are provided as input.

