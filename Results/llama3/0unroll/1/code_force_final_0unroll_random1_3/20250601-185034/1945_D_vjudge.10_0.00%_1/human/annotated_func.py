#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of three lines. The first line contains two space-separated integers n and m, where n and m are positive integers and m is less than or equal to n. The second and third lines contain n space-separated positive integers.
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
        
    #State: Output State: stdin is empty, x is 0, custos is a list of integers representing the minimum cost for each test case.
    for c in custos:
        print(c)
        
    #State: Output State: stdin is empty, x is 0, custos is an empty list of integers representing the minimum cost for each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three lines: two space-separated integers (n and m) and two sets of n space-separated positive integers. It calculates the minimum cost for each test case by comparing and summing the integers from the two sets, following specific rules. The function then prints the minimum cost for each test case.

