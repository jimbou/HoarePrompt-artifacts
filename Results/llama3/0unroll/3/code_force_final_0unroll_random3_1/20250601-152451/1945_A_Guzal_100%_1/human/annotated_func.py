#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 ≤ t ≤ 10^4). Each of the following t lines contains three integers a, b, c (0 ≤ a, b, c ≤ 10^9).
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        
        k = 0
        
        if b % 3 != 0 and b % 3 + c < 3:
            print(-1)
        else:
            k += a + (b + c) // 3
            if (b + c) % 3 != 0:
                k += 1
            print(k)
        
    #State: The output will be a list of n integers, each representing the maximum number of whole pizzas that can be made from the given ingredients, or -1 if it's not possible to make whole pizzas.

#Overall this is what the function does:Calculates and prints the maximum number of whole pizzas that can be made from given ingredients for multiple test cases. For each test case, it takes three integers (a, b, c) as input and outputs the maximum number of whole pizzas or -1 if it's not possible to make whole pizzas. The function processes multiple test cases based on an initial input integer (n) that specifies the number of test cases.

