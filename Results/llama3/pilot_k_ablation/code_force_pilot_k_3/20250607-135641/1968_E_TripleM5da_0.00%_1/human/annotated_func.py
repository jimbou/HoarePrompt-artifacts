#State of the program right berfore the function call: stdin contains two inputs: first an integer (1 <= t <= 50) and then t integers (2 <= n <= 10^3).
    for i in range(0, int(input())):
        n = int(input())
        
        print(1, 1)
        
        print(1, 2)
        
        for i in range(3, n + 2):
            print(i, i)
        
    #State: Output State: `i` is `n + 2`, `n` is an integer between 2 and 10^3 (inclusive), stdin contains no input, and this is printed: 1, 2, 3, 3, 4, 4, 5, 5, ..., `n + 1`, `n + 1`, and this is printed: 1, 1, and this is printed: 1, 2, and the value of `i` which is `n + 2` is being printed twice.
    #
    #The output state after the loop executes all the iterations is that the value of `i` is now `n + 2`, and the value of `n` remains unchanged. The input in stdin is still the same, and the output printed includes the initial 1, 2, followed by the pairs of numbers from 3 to `n + 1`, each number printed twice.

#Overall this is what the function does:This function reads a series of inputs from stdin, where the first input is the number of test cases (t) and each subsequent input is an integer (n) representing the number of pairs to print. The function then prints a series of pairs of numbers, starting with (1, 1) and (1, 2), followed by pairs of numbers from 3 to n+1, where each number is printed twice. The function repeats this process for each test case.

