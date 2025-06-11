#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three lines. The first line contains two space-separated integers n and m (1 <= m <= n <= 200000). The second line contains n space-separated integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9). The third line contains n space-separated integers b_1, b_2, ..., b_n (1 <= b_i <= 10^9). The number of test cases is given in the first line of stdin.
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
        
    #State: `x` is 0, `i` is equal to the initial value of `x`, `a` is an empty list, `num_fila` is an integer, `max_p` is an integer, `a_values` is an empty list, `b_values` is an empty list, `b` is an empty list, `y` is 0, `nf` is a list of strings, `custos` is a list of integers increased by the sum of the minimum values between `a_values[y]` and `a_values[y - 1] + b_values[y]` for all `y` from `max_p - 1` to 1 for each test case, and stdin contains no test cases.
    for c in custos:
        print(c)
        
    #State: `x` is 0, `i` is equal to the initial value of `x`, `a` is an empty list, `num_fila` is an integer, `max_p` is an integer, `a_values` is an empty list, `b_values` is an empty list, `b` is an empty list, `y` is 0, `nf` is a list of strings, `custos` is an empty list, and all elements in `custos` have been printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three lines: two integers n and m, followed by two lists of n integers each. It calculates the minimum cost for each test case by comparing the values of the two lists and summing the minimum values. The function then prints the calculated minimum costs for all test cases.

