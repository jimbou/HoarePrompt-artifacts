#State of the program right berfore the function call: stdin contains t+1 inputs: the first input is an integer t (1 <= t <= 10^4), and the rest t inputs are two space-separated integers x and y (0 <= x, y <= 99).
    n = int(input())
    for i in range(n):
        a, b = input().split()
        
        a = int(a)
        
        b = int(b)
        
        t = b
        
        if t % 2 == 0:
            t = t // 2
        else:
            t = t // 2 + 1
        
        t1 = t * 15 - b * 4
        
        if t1 >= a:
            t = t
        else:
            t2 = a - t1
            if t2 % 15 == 0:
                t = t + t2 // 15
            else:
                t = t + t2 // 15 + 1
        
        print(t)
        
    #State: Output State: The loop will execute `n` times, and in each iteration, it will read two space-separated integers `x` and `y` from the standard input. The loop will calculate a value `t` based on `x` and `y` and print it. The output state will be the values of `t` printed in each iteration, which will be `n` values in total. The values of `n`, `x`, and `y` will remain unchanged.

#Overall this is what the function does:This function reads a series of inputs from the standard input, where the first input is an integer t representing the number of subsequent inputs, and each subsequent input is a pair of space-separated integers x and y. For each pair of integers, the function calculates a value t based on the given formula and prints it. The function does not modify the input values and only produces output values based on the calculations. The final state of the program is the output of the calculated values, which are printed to the standard output.

