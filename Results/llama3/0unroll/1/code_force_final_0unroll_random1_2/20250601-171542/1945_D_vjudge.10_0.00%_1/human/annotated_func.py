#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of three lines. The first line contains two space-separated integers n and m (1 <= m <= n <= 200000). The second line contains n space-separated integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9). The third line contains n space-separated integers b_1, b_2, ..., b_n (1 <= b_i <= 10^9).
    x = int(input())
    custos = []
    for i in range(x):
        custo = 0
        
        num_fila = 0
        
        max_p = 0
        
        a_values = []
        
        b_values = []
        
        nf = input().split()
        
        num_fila = int(nf[0])
        
        max_p = int(nf[1])
        
        a = input().split()
        
        b = input().split()
        
        for y in a:
            a_values.append(int(y))
        
        for y in b:
            b_values.append(int(y))
        
        for y in range(num_fila - 1, max_p - 1, -1):
            if a_values[y] < b_values[y]:
                custo += a_values[y]
            else:
                custo += b_values[y]
        
        for y in range(max_p - 1, 0, -1):
            if a_values[y - 1] + b_values[y] <= a_values[y]:
                custo += b_values[y]
                if y == 1:
                    custo += a_values[0]
                    break
            else:
                custo += a_values[y]
                break
        
        custos.append(custo)
        
    #State: Output State: x is an integer equal to the number of test cases, stdin is empty, custos is a list containing the total cost for each test case.
    for c in custos:
        print(c)
        
    #State: Output State: x is an integer equal to the number of test cases, stdin is empty, custos is an empty list, the console output contains the total cost for each test case.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of three lines: two space-separated integers (n and m) and two lines of n space-separated integers (a_1 to a_n and b_1 to b_n). It calculates the total cost for each test case by iterating through the integers from n to m, adding the smaller of a_i and b_i to the cost, and then iterating from m to 1, adding the smaller of a_(i-1) + b_i and a_i to the cost. The function prints the total cost for each test case to the console, leaving the input stream empty and the output list (custos) empty after execution.

