#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of three lines of input. The first line contains two space-separated integers n and m, where 1 <= m <= n <= 200000. The second and third lines contain n space-separated integers each.
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
        
    #State: The output state after the loop executes all the iterations is a list of integers, where each integer represents the minimum cost to reach the final position from the initial position in each test case. The list has a length equal to the number of test cases (cases). The values in the list are the results of the print statements inside the loop, which are the minimum costs calculated for each test case. The state of the other variables (cases, stdin, na_frente, pos_final, custo_pra_trocar_a, custo_pra_passar_b, total, and best) remains unchanged, as they are not affected by the loop head and body.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three lines of input. It then calculates the minimum cost to reach a final position from an initial position, considering two different costs for each position. The function prints the minimum cost for each test case. The output is a list of integers, where each integer represents the minimum cost for a test case.

