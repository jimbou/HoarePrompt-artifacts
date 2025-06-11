#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains four lines. The first line contains four integers: n, k, P_B, P_S. The second line contains a list of n integers representing the permutation p. The third line contains a list of n integers representing the array a.
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
        
    #State: Output State: The output state after the loop executes all the iterations is that the values of the variables 'n', 'k', 'pb', 'ps', 'p', 'a', 'pathb', 'paths', 'vis', 'resb', 'ress', 'preb', and 'pres' are updated according to the input provided in the stdin. The loop iterates over multiple test cases, and for each test case, it calculates the maximum value of 'resb' and 'ress' based on the given conditions. The output of the loop is a string that indicates whether 'Bodya' or 'Sasha' wins or if it's a 'Draw' based on the comparison of 'resb' and 'ress'. The values of 'YES', 'NO', 'MOD', and 'alpha' remain unchanged as they are not affected by the loop head and body.

#Overall this is what the function does:This function determines the winner of a game between 'Bodya' and 'Sasha' based on the maximum value of two calculated scores, 'resb' and 'ress', which are derived from the input arrays 'p' and 'a' and the given conditions. The function iterates over multiple test cases, each containing four lines of input, and outputs a string indicating the winner ('Bodya' or 'Sasha') or a 'Draw' if the scores are equal. The function does not modify the input arrays or any external state, and its output is solely based on the provided input.

