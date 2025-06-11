#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains four integers n, k, P_B, P_S (1 <= n, k, P_B, P_S <= 2*10^5), followed by two lists of n integers p and a.
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
        
    #State: The loop will continue to execute until it has processed all test cases from the input. The output will be a series of 'Bodya', 'Sasha', or 'Draw' strings, each indicating the winner of a game or a draw, based on the maximum values of resb and ress calculated for each test case.

#Overall this is what the function does:Determines the winner of a game or a draw based on the maximum values calculated from the input test cases. The function accepts multiple test cases from the input, each containing four integers and two lists of integers. It processes each test case, calculating the maximum values for 'Bodya' and 'Sasha', and outputs 'Bodya' if the maximum value for 'Bodya' is greater, 'Sasha' if the maximum value for 'Sasha' is greater, or 'Draw' if the maximum values are equal. The function continues to execute until all test cases have been processed, producing a series of output strings indicating the winner or a draw for each test case.

