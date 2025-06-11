#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (1 <= n <= 2*10^5) and then n space-separated integers (1 <= a_i <= 10^9).
    for _ in range(int(input())):
        n = int(input())
        
        arr = list(map(int, input().split()))
        
        s = set()
        
        for i in range(n):
            s.add(arr[i])
        
        s = list(s)
        
        s.sort()
        
        s = [0] + s
        
        ans = 1
        
        n = len(s)
        
        if n == 2:
            print('Alice')
        else:
            for i in range(1, n - 1):
                if s[i] - s[i - 1] > 1:
                    break
                else:
                    ans ^= 1
            if ans:
                print('Alice')
            else:
                print('Bob')
        
    #State: The output state after the loop executes all the iterations will be a series of 'Alice' or 'Bob' printed to the console, each corresponding to the result of the game for each test case. The number of outputs will be equal to the number of test cases in the input.

#Overall this is what the function does:This function simulates a game for multiple test cases. For each test case, it takes an integer n and a list of n integers as input, removes duplicates, sorts the list, and then determines the winner of the game based on the differences between consecutive numbers in the sorted list. The function prints 'Alice' or 'Bob' to the console for each test case, indicating the winner of the game.

