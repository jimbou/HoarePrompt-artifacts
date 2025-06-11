#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of three lines. The first line contains two space-separated integers n and m, where 1 <= m <= n <= 200000. The second line contains n space-separated integers a_1, a_2, ..., a_n, where 1 <= a_i <= 10^9. The third line contains n space-separated integers b_1, b_2, ..., b_n, where 1 <= b_i <= 10^9.
    cases = int(input())
    for c in range(cases):
        na_frente, pos_final = map(int, input().split())
        
        custo_pra_trocar_a = list(map(int, input().split()))
        
        custo_pra_passar_b = list(map(int, input().split()))
        
        na_frente -= 1
        
        pos_final -= 1
        
        total = 0
        
        best = sys.float_info.max
        
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
        
    #State: The output state will be the minimum cost to reach the final position from the starting position for each test case. The minimum cost is calculated by considering the minimum cost to reach each position from the starting position and the cost to move from that position to the final position. The minimum cost is updated at each position if the cost to reach that position is less than the current minimum cost. The final output will be the minimum cost for each test case, printed on a new line.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three lines: two integers n and m, and two lists of n integers a and b. It calculates the minimum cost to reach the final position from the starting position for each test case by considering the minimum cost to reach each position from the starting position and the cost to move from that position to the final position. The function prints the minimum cost for each test case on a new line.

