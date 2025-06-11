#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines, each containing three integers k, x and a (2 <= k <= 30, 1 <= x <= 100, 1 <= a <= 10^9).
    for _ in range(int(input())):
        k, x, a = map(int, input().split())
        
        s = 1
        
        for i in range(x):
            s += s // (k - 1) + 1
        
        print('Yes' if a >= s else 'No')
        
    #State: The output state will be a series of 'Yes' or 'No' for each test case, indicating whether the value of 'a' is greater than or equal to the calculated value of 's'. The number of 'Yes' or 'No' will be equal to the value of 't' in the initial state.

#Overall this is what the function does:This function determines whether a given value 'a' is greater than or equal to a calculated value 's' for multiple test cases. It accepts a series of inputs from the user, where each input consists of three integers: 'k', 'x', and 'a'. The function calculates the value of 's' based on 'k' and 'x', and then prints 'Yes' if 'a' is greater than or equal to 's', and 'No' otherwise. The function repeats this process for a specified number of test cases 't', and outputs a series of 'Yes' or 'No' results.

