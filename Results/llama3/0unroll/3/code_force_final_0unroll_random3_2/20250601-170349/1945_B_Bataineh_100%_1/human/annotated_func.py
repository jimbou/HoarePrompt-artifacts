#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing three integers a, b, m (1 <= a, b, m <= 10^18).
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        if m < a and m < b:
            print(2)
        elif m < a and m > b:
            print(2 + m // b)
        elif m < b and m > a:
            print(2 + m // a)
        else:
            print(m // a + m // b + 2)
        
    #State: The output state will contain t lines, each containing an integer representing the minimum number of operations required to make a and b equal to m. The integer on each line will be the result of the calculations performed inside the loop for the corresponding input values of a, b, and m.

#Overall this is what the function does:This function reads a series of input values from standard input, where each set of values consists of three integers: a, b, and m. It then calculates and prints the minimum number of operations required to make a and b equal to m, considering all possible cases where m is less than, greater than, or equal to a and b. The function processes multiple sets of input values, as specified by an initial integer t, and outputs the calculated minimum operations for each set.

