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
        
    #State: The output state after the loop executes all the iterations is that the values of 'YES', 'NO', 'MOD', and 'alpha' remain unchanged as 'YES', 'NO', 1000000007, and 'abcdefghijklmnopqrstuvwxyz' respectively. The stdin is empty as all the test cases have been processed. The loop has printed the winner of each test case, either 'Bodya', 'Sasha', or 'Draw', based on the maximum value of the calculated expressions resb and ress for each test case.

#Overall this is what the function does:This function processes multiple test cases from standard input, each consisting of four lines of input. It calculates the maximum value of two expressions, resb and ress, based on the input values and prints the winner of each test case, either 'Bodya', 'Sasha', or 'Draw', depending on which expression has a higher maximum value. The function iterates through all test cases, processing each one independently, and outputs the result of each test case.

