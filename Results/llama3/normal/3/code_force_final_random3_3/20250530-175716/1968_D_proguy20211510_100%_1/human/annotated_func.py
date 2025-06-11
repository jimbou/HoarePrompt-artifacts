#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of four lines. The first line contains four space-separated integers: n, k, P_B, P_S. The second line contains n space-separated integers representing the permutation p. The third line contains n space-separated integers representing the array a.
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
        
    #State: The loop iterates over the test cases in the input, and for each test case, it calculates the maximum score that can be achieved by Bodya and Sasha by traversing the permutation p and array a. The loop prints 'Bodya' if Bodya's maximum score is higher, 'Sasha' if Sasha's maximum score is higher, and 'Draw' if their scores are equal. The loop continues until all test cases have been processed.

#Overall this is what the function does:This function determines the winner of a game between Bodya and Sasha based on their scores calculated by traversing a permutation and an array. It iterates over multiple test cases, each consisting of four lines of input, and prints the winner ('Bodya', 'Sasha', or 'Draw') for each test case. The function takes no explicit parameters but reads input from stdin and returns no value, instead printing the results directly.

