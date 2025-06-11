#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 1000). Each of the following t lines contains three integers k, x, and a (2 <= k <= 30, 1 <= x <= 100, 1 <= a <= 10^9).
    for _ in range(int(input())):
        k, x, a = map(int, input().split())
        
        s = 1
        
        for i in range(x):
            s += s // (k - 1) + 1
        
        print('Yes' if a >= s else 'No')
        
    #State: Output State: The output state will be a series of 'Yes' or 'No' printed on the console, each corresponding to whether the value of 'a' is greater than or equal to the calculated value of 's' for each test case.

#Overall this is what the function does:This function reads multiple lines of input from the standard input, where the first line contains the number of test cases, and each subsequent line contains three integers: k, x, and a. It then calculates a value 's' based on the given integers and prints 'Yes' if 'a' is greater than or equal to 's', and 'No' otherwise, for each test case. The function does not return any value but prints the results directly to the console.

