#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of three lines. The first line contains two integers n and m (1 <= m <= n <= 200,000). The second line contains n integers a_1, a_2, ..., a_n separated by spaces (1 <= a_i <= 10^9). The third line contains n integers b_1, b_2, ..., b_n separated by spaces (1 <= b_i <= 10^9). The number of test cases is given by an integer t (1 <= t <= 10^4) at the beginning of the input.
    cases = int(input())
    for c in range(cases):
        na_frente, pos_final = map(int, input().split())
        
        custo_pra_trocar_a = list(map(int, input().split()))
        
        custo_pra_passar_b = list(map(int, input().split()))
        
        na_frente -= 1
        
        pos_final -= 1
        
        total = 0
        
        best = 10 ** 12
        
        for v in range(na_frente, -1, -1):
            if v <= pos_final:
                if best > total + custo_pra_trocar_a[v]:
                    best = total + custo_pra_trocar_a[v]
                if custo_pra_trocar_a[v] < custo_pra_passar_b[v]:
                    total += custo_pra_trocar_a[v]
                else:
                    total += custo_pra_passar_b[v]
            elif custo_pra_trocar_a[v] < custo_pra_passar_b[v]:
                total += custo_pra_trocar_a[v]
            else:
                total += custo_pra_passar_b[v]
        
        print(best)
        
    #State: cases is 0, c is equal to the initial value of cases, na_frente is -1, pos_final is an integer minus one, custo_pra_trocar_a is a list of integers, custo_pra_passar_b is a list of integers, stdin contains multiple test cases minus 3*cases inputs, v is -1, total is the sum of the minimum costs between changing to option A and passing to option B at each position from na_frente to 0, and best is the minimum total cost among all possible paths, and the minimum total cost among all possible paths which is best is being printed

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three lines: two integers n and m, and two lists of n integers each. It calculates the minimum total cost of traversing from the first position to the last position, considering the costs of either changing to option A or passing to option B at each position. The function prints the minimum total cost for each test case.

