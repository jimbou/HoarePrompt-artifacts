#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines, each containing three integers k, x, and a (2 <= k <= 30, 1 <= x <= 100, 1 <= a <= 10^9).
    for _ in range(int(input())):
        k, x, a = map(int, input().split())
        
        s = 1
        
        for i in range(x):
            s += s // (k - 1) + 1
        
        print('Yes' if a >= s else 'No')
        
    #State: The output state will be a sequence of 'Yes' or 'No' for each test case, indicating whether the value of 'a' is greater than or equal to the calculated value of 's' after the inner loop execution. The number of 'Yes' or 'No' outputs will be equal to the value of 't' in the initial state.

#Overall this is what the function does:This function reads a sequence of test cases from standard input, where each test case consists of three integers: k, x, and a. For each test case, it calculates a value s based on k and x, and then prints 'Yes' if a is greater than or equal to s, and 'No' otherwise. The function repeats this process for a number of test cases specified by an initial integer t, and outputs a sequence of 'Yes' or 'No' results, one for each test case.

