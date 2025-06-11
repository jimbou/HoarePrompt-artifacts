#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of three lines. The first line contains two space-separated integers n and m (1 <= m <= n <= 200000). The second line contains n space-separated integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9). The third line contains n space-separated integers b_1, b_2, ..., b_n (1 <= b_i <= 10^9).
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
        
    #State: cases is 0, c is equal to its original value, na_frente is an integer equal to its original value minus the original value of cases, pos_final is an integer equal to its original value minus the original value of cases, custo_pra_trocar_a is a list of integers, custo_pra_passar_b is a list of integers, total is the sum of the minimum of custo_pra_trocar_a and custo_pra_passar_b for all indices from na_frente to 0, best is the minimum of the original value of best and the sum of total and the element at index v of custo_pra_trocar_a for all indices v from na_frente to 0, and stdin contains -original value of cases inputs, and the best is printed which is the minimum of the original value of best and the sum of total and the element at index v of custo_pra_trocar_a for all indices v from na_frente to 0

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three lines: two integers n and m, and two lists of n integers each. It then calculates the minimum cost to move from the first position to the final position, considering the costs of swapping and passing at each position. The function prints the minimum cost for each test case.

