#State of the program right berfore the function call: stdin contains multiple inputs: the first line contains a single integer t (1 ≤ t ≤ 10^4), followed by t sets of input data. Each set of input data starts with a line containing two integers n and k (1 ≤ k < n ≤ 10^5), followed by n - 1 lines, each containing two integers v and u (1 ≤ v, u ≤ n).
    for _ in range(int(sys.stdin.readline())):
        solve()
        
    #State: stdin contains multiple inputs: the first line contains a single integer 0, and the function solve() has been executed and returned None.

#Overall this is what the function does:Reads input from stdin, processes it according to the solve() function, and returns None, leaving stdin in a state where the first line contains a single integer 0.

