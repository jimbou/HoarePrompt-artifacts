#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of three lines. The first line contains two space-separated integers n and m (1 <= m <= n <= 200000). The second and third lines contain n space-separated integers (1 <= integer <= 10^9).
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
        
    #State: The loop has executed all the iterations and has printed the minimum cost to reach the final position for each test case. The values of the variables `cases`, `na_frente`, `pos_final`, `custo_pra_trocar_a`, `custo_pra_passar_b`, `total`, and `best` have been updated accordingly after each iteration. The `stdin` has been consumed and is empty.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three lines. It calculates and prints the minimum cost to reach a final position from a given starting position, considering two different cost arrays. The function iterates over each test case, updating variables accordingly, and consumes the standard input. After all iterations, the function has printed the minimum cost for each test case, and the standard input is empty.

