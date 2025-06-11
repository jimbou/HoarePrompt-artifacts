#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two lines. The first line contains an integer n. The second line contains n space-separated integers. t is a positive integer, n is a positive integer, and the integers are positive integers.
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
        
    #State: t is 0, _ is t, n is an integer, arr is a list of integers, s is a list of integers with a prepended 0, stdin contains 0 test cases, i is n-1, ans is 1.

#Overall this is what the function does:This function determines the winner of a game based on a sequence of integers. It reads input from stdin, where each test case consists of an integer n followed by n space-separated integers. The function then checks if the sequence is consecutive, and if not, it alternates between 'Alice' and 'Bob' as the winner. If the sequence is consecutive, the winner is 'Alice'. The function prints the winner for each test case.

