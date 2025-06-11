#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t sets of three space-separated integers a, b, and m (1 <= a, b, m <= 10^18).
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        mn = min(a, b) + m
        
        if m % a == 0 and m % b == 0 and a != 1 and b != 1:
            print(mn // a + mn // b + 1)
        else:
            print(mn // a + mn // b)
        
    #State: The output state will contain t lines, each containing a single integer. The integer on each line will be the result of the calculation (mn // a + mn // b + 1) if m is divisible by both a and b and a and b are not 1, otherwise it will be the result of (mn // a + mn // b). The values of t, a, b, and m will remain unchanged.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints output to stdout. It accepts no parameters and returns no value. It reads an integer t, followed by t sets of three integers a, b, and m. For each set, it calculates a value mn and prints the result of either (mn // a + mn // b + 1) or (mn // a + mn // b), depending on whether m is divisible by both a and b and a and b are not 1. The function does not modify the input values.

