#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three lines of input. The first line contains two space-separated integers n and m, where 1 <= m <= n <= 200000. The second line contains n space-separated integers a_1, a_2, ..., a_n, where 1 <= a_i <= 10^9. The third line contains n space-separated integers b_1, b_2, ..., b_n, where 1 <= b_i <= 10^9.
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
        
    #State: The output state will be the minimum cost to reach the final position from the initial position for each test case. The minimum cost is calculated by considering the minimum cost to reach each position from the initial position and the cost to move from that position to the final position. The minimum cost to reach each position is calculated by considering the minimum cost to reach the previous position and the cost to move from the previous position to the current position. The cost to move from one position to another is the minimum of the cost to change the current position and the cost to pass through the current position. The output will be the minimum cost to reach the final position for each test case, which will be printed on a new line for each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three lines of input. It calculates the minimum cost to reach a final position from an initial position by considering the minimum cost to reach each position and the cost to move from that position to the final position. The cost to move from one position to another is the minimum of the cost to change the current position and the cost to pass through the current position. The function prints the minimum cost to reach the final position for each test case on a new line.

