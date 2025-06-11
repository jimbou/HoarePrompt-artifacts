#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three space-separated integers p_1, p_2 and p_3 such that 0 <= p_1 <= p_2 <= p_3 <= 30.
    t = int(input())
    for _ in range(t):
        a, b, c = map(int, input().split())
        
        if (a + b + c) % 2 != 0:
            print(-1)
            continue
        
        x = (a + b + c) // 2
        
        y = a + b
        
        print(min(x, y))
        
    #State: The loop will print the minimum of the sum of the first two numbers and half of the sum of all three numbers for each test case, or -1 if the sum of the three numbers is odd. The value of `t` remains unchanged.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of three integers. For each test case, it calculates the sum of the three integers and checks if it's even. If the sum is odd, it prints -1. If the sum is even, it calculates the minimum of the sum of the first two integers and half of the sum of all three integers, and prints this minimum value. The function does not modify the input values or retain any state between test cases.

