#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t sets of three space-separated integers a, b, m (1 <= a, b, m <= 10^18).
    t = int(input())
    for _ in range(t):
        a, b, m = map(int, input().split())
        
        A = int(m / a) + 1
        
        B = int(m / b) + 1
        
        print(A + B)
        
    #State: The output state will be the sum of the ceiling divisions of m by a and m by b, for each set of inputs, printed t times.

#Overall this is what the function does:This function reads a series of input sets from standard input, where each set contains three integers: a, b, and m. For each set, it calculates the ceiling division of m by a and m by b, adds these two results together, and prints the sum. The function repeats this process for a specified number of sets, t, which is also read from standard input.

