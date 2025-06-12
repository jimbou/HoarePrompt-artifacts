#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t lines, each containing two integers n and k (1 <= n <= 100, 0 <= k <= n*(n-1)/2).
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        print(n if n - k > 1 else 1)
        
    #State: stdin is empty, _ is t-1, int(input()) is 0, n and k are the last two integers in the input, and the value of n if n - k > 1 else 1 has been printed t times.

#Overall this is what the function does:Reads a series of integer pairs from standard input, where each pair represents the number of nodes (n) and the number of edges (k) in a graph, and prints the number of nodes if the difference between the number of nodes and edges is greater than 1, otherwise prints 1, repeating this process for a number of times specified by the first integer read from standard input.

