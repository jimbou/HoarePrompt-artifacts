#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t sets of three space-separated integers a, b, and m (1 <= a, b, m <= 10^18).
    t = int(input())
    for _ in range(t):
        a, b, m = map(int, input().split())
        
        A = int(m / a) + 1
        
        B = int(m / b) + 1
        
        print(A + B)
        
    #State: The output state will be the sum of the number of multiples of a and b that are less than or equal to m, for each set of inputs. Specifically, for each set of inputs (a, b, m), the output will be the sum of the integer division of m by a (rounded up) and the integer division of m by b (rounded up). The output will be a sequence of these sums, one for each set of inputs.

#Overall this is what the function does:The function reads a sequence of input sets from standard input, where each set contains three integers: a, b, and m. For each set, it calculates the sum of the number of multiples of a and b that are less than or equal to m, by performing integer division of m by a and b, rounding up to the nearest whole number, and adding the results together. The function then prints the calculated sum for each input set.

