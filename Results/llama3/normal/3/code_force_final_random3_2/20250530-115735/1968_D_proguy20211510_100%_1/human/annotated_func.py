#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains four integers (n, k, P_B, P_S) on the first line, a list of n integers (p_1 to p_n) on the second line, and a list of n integers (a_1 to a_n) on the third line. n is a positive integer, k is a non-negative integer, and 1 <= P_B, P_S <= n. The list p_1 to p_n is a permutation of integers from 1 to n, and the list a_1 to a_n contains positive integers.
    YES, NO = 'YES', 'NO'
    MOD = 10 ** 9 + 7
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for _ in range(int(input())):
        n, k, pb, ps = input().split()
        
        n, k, pb, ps = int(n), int(k), int(pb), int(ps)
        
        p = list(map(int, input().split()))
        
        a = list(map(int, input().split()))
        
        pathb, paths = [], []
        
        vis = [0] * n
        
        vis[pb - 1] = 1
        
        while True:
            pathb.append(a[pb - 1])
            pb = p[pb - 1]
            if vis[pb - 1] == 1:
                break
        
        vis = [0] * n
        
        vis[ps - 1] = 1
        
        while True:
            paths.append(a[ps - 1])
            ps = p[ps - 1]
            if vis[ps - 1] == 1:
                break
        
        resb, ress = 0, 0
        
        preb, pres = 0, 0
        
        for i in range(len(pathb)):
            if k < i + 1:
                break
            curr = preb + pathb[i] * (k - i)
            preb += pathb[i]
            resb = max(resb, curr)
        
        for i in range(len(paths)):
            if k < i + 1:
                break
            curr = pres + paths[i] * (k - i)
            pres += paths[i]
            ress = max(ress, curr)
        
        if resb > ress:
            print('Bodya')
        elif ress > resb:
            print('Sasha')
        else:
            print('Draw')
        
    #State: YES is 'YES', NO is 'NO', MOD is 1000000007, alpha is 'abcdefghijklmnopqrstuvwxyz', n is an integer, k is an integer, pb is an integer equal to the value at index pb-1 in list p, p is a list of integers, a is a list of integers, pathb is a list containing the integer at index pb-1 in list a repeated a number of times equal to the number of iterations of the loop, vis is a list of n integers with all indices set to 0 except for the ps-1th index which is set to 1, ps is the value at index p[ps-1]-1 in list p, paths is a list containing the integer at index ps-1 in list a repeated a number of times equal to the number of iterations of the loop plus the number of iterations of the loop minus one more integers at index ps-1 in list a, resb is the maximum value between its original value and the sum of preb and the product of pathb[i] and the difference between k and i, preb is the sum of its original value and pathb[i], ress is the maximum value between its original value and the sum of pres and the product of paths[i] and the difference between k and i, pres is the sum of its original value and paths[i], and i is equal to the length of paths. The program prints 'Bodya' if resb is greater than ress, 'Sasha' if ress is greater than resb, and 'Draw' otherwise.

#Overall this is what the function does:This function determines the winner of a game between two players, Bodya and Sasha, based on the maximum score they can achieve by traversing a circular path. The function takes no parameters but reads input from stdin, which contains multiple test cases. Each test case consists of four integers (n, k, P_B, P_S) and two lists of n integers (p_1 to p_n and a_1 to a_n). The function calculates the maximum score for each player by iterating through their respective paths and prints the winner ('Bodya', 'Sasha', or 'Draw') based on their maximum scores.

