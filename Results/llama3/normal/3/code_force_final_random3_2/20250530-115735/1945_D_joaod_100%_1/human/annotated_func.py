#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of three lines. The first line contains two space-separated integers n and m (1 <= m <= n <= 200000). The second and third lines contain n space-separated integers (1 <= integer <= 10^9).
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
        
    #State: cases is 0, c is equal to the initial value of cases, na_frente is -1, pos_final is -1, custo_pra_trocar_a is a list of integers, custo_pra_passar_b is a list of integers, v is -1, total is the sum of the minimum values between custo_pra_trocar_a and custo_pra_passar_b for all positions from na_frente to -1, best is the minimum value between total + custo_pra_trocar_a[v] and the current best value for all positions from na_frente to -1, and stdin is empty.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three lines. It calculates the minimum cost to move from the front to the final position by either switching to or passing through each position, and prints the minimum cost for each test case. The function iterates through the positions from the front to the final position, keeping track of the total cost and the best (minimum) cost found so far. It updates the total cost and best cost based on whether switching to or passing through each position is cheaper. After processing all test cases, the function leaves the input stream empty and returns no value.

