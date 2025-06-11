#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of four lines. The first line contains four integers: n, k, P_B, P_S. The second line contains n integers representing the permutation p. The third line contains n integers representing the array a. n is a positive integer, k is a positive integer, 1 <= P_B, P_S <= n. The permutation p is a list of distinct integers from 1 to n in arbitrary order. The array a is a list of positive integers.
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
        
    #State: The loop iterates over multiple test cases, and for each test case, it determines the winner of a game between Bodya and Sasha based on the maximum score they can achieve by traversing a permutation p and an array a. The output state is the result of the game for each test case, which can be either 'Bodya', 'Sasha', or 'Draw'. The values of YES, NO, MOD, and alpha remain unchanged. The stdin is empty after all test cases have been processed.

#Overall this is what the function does:This function determines the winner of a game between Bodya and Sasha based on their maximum scores achieved by traversing a permutation and an array. It processes multiple test cases from standard input, each consisting of four lines: the first line contains four integers (n, k, P_B, P_S), the second line contains a permutation p, and the third line contains an array a. The function calculates the maximum score for both Bodya and Sasha by iterating through the permutation and array, and then compares their scores to determine the winner. The function prints the result of each game, which can be either 'Bodya', 'Sasha', or 'Draw'.

