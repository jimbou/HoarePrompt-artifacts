#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two lines. The first line contains a single integer n. The second line contains n integers.
    for _ in range(int(input())):
        n = int(input())
        
        arr = list(map(int, input().split()))
        
        s = set()
        
        for i in range(n):
            s.add(arr[i])
        
        s = list(s)
        
        ans = 1
        
        s = [0] + s
        
        n = len(s)
        
        if n == 2:
            print('Alice')
        else:
            for i in range(1, n - 1):
                if s[i] - s[i - 1] > 1:
                    break
                else:
                    ans = 1 - ans
            if ans:
                print('Alice')
            else:
                print('Bob')
        
    #State: The output state will contain t lines, each containing either 'Alice' or 'Bob', depending on the outcome of the game for each test case.

#Overall this is what the function does:Determines the winner of a game for each test case by analyzing a sequence of integers and prints 'Alice' or 'Bob' accordingly.

