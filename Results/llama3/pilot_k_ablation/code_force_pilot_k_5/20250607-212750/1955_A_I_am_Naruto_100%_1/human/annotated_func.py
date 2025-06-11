#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing three integers n, a, and b (1 <= n <= 100, 1 <= a, b <= 30).
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        s1 = n * a
        
        s2 = b * (n // 2) + n % 2 * a
        
        print(min(s1, s2))
        
    #State: _ is t-1, stdin is empty, and the minimum value between s1 and s2 is printed for each of the t input lines.

#Overall this is what the function does:This function reads a series of input lines from standard input, where each line contains three integers representing the number of items, the cost of item A, and the cost of item B. For each input line, it calculates the minimum total cost between buying all items at the cost of A and buying as many items as possible at the cost of B and the remaining items at the cost of A, then prints this minimum cost. The function continues this process until all input lines have been processed, at which point standard input is empty.

