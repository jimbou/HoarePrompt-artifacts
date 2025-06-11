#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three inputs: two space-separated integers (n and m) and two lists of n space-separated integers (a_1 to a_n and b_1 to b_n). n and m are positive integers, 1 <= m <= n <= 200000. a_i and b_i are positive integers, 1 <= a_i, b_i <= 10^9.
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
        
    #State: cases is 0, c is equal to the initial value of cases, stdin is empty, na_frente is -1, pos_final is a positive integer, 0 <= pos_final <= 199999, custo_pra_trocar_a is a list of n positive integers, custo_pra_passar_b is a list of n positive integers, v is -1, total is the sum of the minimum costs between changing at each position and passing at each position from na_frente to 0, best is the minimum total cost plus the cost to change at each position from na_frente to 0, and best is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two integers (n and m) and two lists of n integers (a_1 to a_n and b_1 to b_n). It then calculates the minimum total cost to move from position n to position 0, considering the costs of changing at each position and passing at each position. The function prints the minimum total cost plus the cost to change at each position from n to 0 for each test case.

