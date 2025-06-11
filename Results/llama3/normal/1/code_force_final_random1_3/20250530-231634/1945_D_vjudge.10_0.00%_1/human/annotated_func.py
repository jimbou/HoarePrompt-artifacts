#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three lines of input. The first line contains two space-separated integers n and m (1 <= m <= n <= 200000). The second line contains n space-separated integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9). The third line contains n space-separated integers b_1, b_2, ..., b_n (1 <= b_i <= 10^9).
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
        
    #State: custos is a list containing the sum of the minimum values between corresponding elements in a_values and b_values from index num_fila - 1 to max_p - 1, plus the sum of b_values from index 1 to max_p - 1 if a_values[y - 1] + b_values[y] is less than or equal to a_values[y] for all y from max_p - 1 to 1, otherwise it contains all integers in the list a_values except the integer at index y where y is the smallest index such that a_values[y - 1] + b_values[y] is greater than a_values[y], and x additional elements custo have been appended to the end of the list.
    for c in custos:
        print(c)
        
    #State: `custos` is a list containing the sum of the minimum values between corresponding elements in `a_values` and `b_values` from index `num_fila - 1` to `max_p - 1`, plus the sum of `b_values` from index 1 to `max_p - 1` if `a_values[y - 1] + b_values[y]` is less than or equal to `a_values[y]` for all `y` from `max_p - 1` to 1, otherwise it contains all integers in the list `a_values` except the integer at index `y` where `y` is the smallest index such that `a_values[y - 1] + b_values[y]` is greater than `a_values[y]`, and `x` additional elements `custo` have been appended to the end of the list and must have at least `len(custos)` elements, `c` is the last element in the list, and the last element in the list which is `c` is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three lines: two space-separated integers n and m, followed by two lines of n space-separated integers. It calculates the minimum cost for each test case by comparing corresponding elements in the two lines of integers and summing the minimum values. If a certain condition is met, it also sums additional values. The function then prints the calculated minimum cost for each test case.

