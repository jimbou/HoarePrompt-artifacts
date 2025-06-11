#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three lines. The first line contains two integers n and m (1 <= m <= n <= 200,000). The second line contains n integers a_1, a_2, ..., a_n separated by spaces (1 <= a_i <= 10^9). The third line contains n integers b_1, b_2, ..., b_n separated by spaces (1 <= b_i <= 10^9).
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
        
    #State: cases is at least the original value of cases, c is equal to the original value of cases minus 1, na_frente is -1, pos_final is an integer equal to its original value minus the original value of cases, custo_pra_trocar_a is a list of integers, custo_pra_passar_b is a list of integers, v is -1, best is the minimum of the total cost plus the cost to change at each position, total is the sum of the minimum cost to change or pass at each position, stdin is empty, and the best is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three lines: two integers n and m, and two lists of n integers each. It then calculates the minimum cost to reach a target position by either changing or passing through each position, and prints the minimum cost for each test case. The function iterates through each test case, updating the minimum cost and total cost as it processes each position, and finally prints the minimum cost for each test case.

