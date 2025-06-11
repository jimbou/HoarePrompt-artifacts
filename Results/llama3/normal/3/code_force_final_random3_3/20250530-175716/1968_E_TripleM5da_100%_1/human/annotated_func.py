#State of the program right berfore the function call: stdin contains two inputs: first an integer (t) and then t integers (n). t is a positive integer and n is an integer such that 2 <= n <= 10^3.
    for i in range(0, int(input())):
        n = int(input())
        
        print(1, 1)
        
        print(1, 2)
        
        for i in range(3, n + 1):
            print(i, i)
        
    #State: Output State: `i` is `n + t - 1`, `n` is an integer that must be greater than or equal to 3 and is now equal to the integer input from stdin, `stdin` contains at least `t - 1` integers, and the output includes the initial printed values of 1 and 2, followed by the value of `n` being printed, and the value of `i` (which is now equal to `n + t - 1`) being printed `n - 1` times, and this is printed: 1, 1, and this is printed: 1, 2, and this is printed: 3, 3, and this is printed: 4, 4, and this is printed: 5, 5, and so on, until `i` is `n + t - 1`, and `input_value` is at least `t + 2`, and this is printed: 1, 1, and this is printed: 1, 2, and the current value of `i` which is `n + t - 1` and the current value of `i` which is `n + t - 1` is being printed, and this is printed: `n + t - 1`, `n + t - 1`.
    #
    #In natural language, after the loop executes all the iterations, the value of `i` will be equal to `n + t - 1`, and the value of `n` will remain unchanged. The input state of stdin will also remain unchanged. The output will include the initial printed values of 1 and 2, followed by the value of `n` being printed, and the value of `i` (which is now equal to `n + t - 1`) being printed `n - 1` times.

#Overall this is what the function does:This function reads a positive integer `t` and then `t` integers `n` from standard input, where `n` is between 2 and 10^3. It then prints a sequence of pairs of numbers, starting with (1, 1) and (1, 2), followed by pairs of identical numbers from 3 to `n`. The function does not return any value, but its output includes the initial pairs and the sequence of identical pairs up to `n`. The input state of `stdin` remains unchanged, and the output is printed to the console.

