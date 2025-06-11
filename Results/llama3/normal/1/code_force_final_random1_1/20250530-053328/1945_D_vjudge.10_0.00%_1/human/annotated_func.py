#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of three lines. The first line contains two integers n and m (1 <= m <= n <= 200000). The second and third lines each contain n integers (1 <= a_i, b_i <= 10^9).
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
        
    #State: x is an integer equal to the initial value of x, num_fila is an integer greater than or equal to max_p, max_p is an integer greater than or equal to 1, a_values is a list containing the integer values of all elements of a, b_values is a list containing the integer values of all elements of b, stdin contains multiple test cases minus 3x lines, a is a list of strings from the second line of stdin, b is an empty list, y is 0, custo is the sum of the minimum values between corresponding elements in a_values and b_values from index num_fila - 1 to 0, plus a_values[0], and custos is a list containing the updated value of custo and the previous values of custo.
    for c in custos:
        print(c)
        
    #State: The loop has executed all iterations, printing all elements in the `custos` list. The loop variable `c` is the last element in `custos`, and this last element has been printed. All other variables remain unchanged.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three lines. It calculates the minimum cost for each test case by comparing corresponding elements in two lists of integers and summing the minimum values, then prints the calculated costs. The function iterates over all test cases, printing the minimum cost for each one.

