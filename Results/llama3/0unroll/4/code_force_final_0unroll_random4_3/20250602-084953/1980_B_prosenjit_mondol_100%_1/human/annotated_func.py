#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains three integers: the number of cubes (n), the index of Dmitry's favorite cube (f), and the number of removed cubes (k). The second line contains n integers representing the values shown on the cubes.
    for _ in range(int(input())):
        n, f, k = map(int, input().split())
        
        f -= 1
        
        k -= 1
        
        a = list(map(int, input().split()))
        
        x = a[f]
        
        a.sort(reverse=True)
        
        if a[k] > x:
            print('NO')
        elif a[k] < x:
            print('YES')
        else:
            print('YES' if k == n - 1 or a[k + 1] < x else 'MAYBE')
        
    #State: The output state will contain the results of each test case, indicating whether Dmitry's favorite cube will be removed ('NO'), will not be removed ('YES'), or may or may not be removed ('MAYBE'), depending on the values of the cubes and the number of removed cubes.

#Overall this is what the function does:Determines whether Dmitry's favorite cube will be removed or not, based on the values of the cubes and the number of removed cubes, and prints the result for each test case.

