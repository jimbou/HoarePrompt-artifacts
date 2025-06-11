#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three lines of input: the first line contains two integers n and m (1 <= m <= n <= 200000), the second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9), and the third line contains n integers b_1, b_2, ..., b_n (1 <= b_i <= 10^9).
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
        
    #State: The loop has executed all the iterations, and the output state is the final state of the variables in the loop head and body. The variable `cases` remains unchanged, as it is not affected by the loop head and body. The variable `na_frente` has been decremented by 1 in each iteration, so its final value is `na_frente - cases`. The variable `pos_final` has also been decremented by 1 in each iteration, so its final value is `pos_final - cases`. The variable `total` has been updated in each iteration, so its final value is the sum of all the values of `custo_pra_trocar_a[v]` and `custo_pra_passar_b[v]` for all `v` in the range `na_frente` to `-1` (inclusive). The variable `best` has been updated in each iteration, so its final value is the minimum of all the values of `total + custo_pra_trocar_a[v]` for all `v` in the range `na_frente` to `-1` (inclusive). The output state is the final state of these variables after all the iterations of the loop have finished.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three lines: two integers n and m, and two lists of n integers each. It then calculates the minimum cost to move from the first position to the last position, considering the costs of swapping and passing at each position. The function prints the minimum cost for each test case.

